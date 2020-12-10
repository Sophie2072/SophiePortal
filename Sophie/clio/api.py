from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mis import models, permissions


@api_view(["GET", "POST"])
@login_required
@user_passes_test(permissions.is_level_4)
def checklist_api(request, pk):
    """Gets or sets the checklist for a specific job.

    GET - returns the current checklist as a JSON object
    POST - takes at least one checkbox id, and a checked boolean and updates the job's checklist
    """
    job = get_object_or_404(models.Job, pk=pk)
    checklist = job.get_checklist()
    if request.method == "GET":
        return Response({"result": checklist})
    else:
        checkboxes = request.POST.getlist(
            "checkbox", request.POST.getlist("checkbox[]", [])
        )
        checked = request.POST.get("checked")
        if checkboxes == [] or checked is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        for checkbox in checkboxes:
            if checked == "true" and checkbox not in checklist:
                checklist.append(checkbox)
            elif checked == "false" and checkbox in checklist:
                checklist.remove(checkbox)
        job.set_checklist(checklist)
        job.save()
        return Response({"result": "success"})


@api_view(["GET", "POST"])
@login_required
@user_passes_test(permissions.is_level_4)
def new_checklist_api(request, pk):
    job = get_object_or_404(models.Job, pk=pk)
    user_id = request.user.id
    checklist = job.get_checklist_completion()
    checklist = models.JobChecklist.objects.filter(job=pk)
    checkboxes = request.POST.getlist(
        "checkbox", request.POST.getlist("checkbox[]", [])
    )
    print(checkboxes)
    print(user_id)
    print(checklist)
    if request.method == 'GET':
        return Response({"result": checklist})
    else:
        item = job.add_checklist_item(checkboxes)
        print(item)

    return Response({"result": "success"})


@api_view(["GET", "POST"])
@login_required
@user_passes_test(permissions.is_level_4)
def checklist_notes_api(request, pk):
    """"Gets or sets the checklist notes field"""
    job = get_object_or_404(models.Job, pk=pk)
    if request.method == "GET":
        return Response({"result": "success", "data": job.checklist_notes})
    note = request.POST.get("note")
    if note is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    job.checklist_notes = note
    job.save()
    return Response({"result": "success"})


@api_view(["POST"])
@login_required
@user_passes_test(permissions.is_level_4)
def budget_api(request, pk):
    """Receives a line from the costing spreadsheet and upserts it to the database."""
    job = get_object_or_404(models.Job, pk=pk)
    line = request.POST.get("line")
    if line is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        field, value = line.split("\t")
    except ValueError:
        return Response(
            {"reason": "invalid row format"}, status=status.HTTP_400_BAD_REQUEST
        )
    try:
        value = value.replace("$", "").replace("%", "").replace("-", "0")
        value = float(value.strip())
    except ValueError:
        return Response(
            {"reason": "invalid value format"}, status=status.HTTP_400_BAD_REQUEST
        )
    success = False
    if field == "Direct Outcosts":
        job.budgeted_outcost = value
        job.save()
        success = True
    elif field == "Labour Discount":
        job.labour_discount = value
        job.save()
        success = True
    else:
        query = models.Role.objects.filter(title=field)
        if query:
            budget, _ = models.JobHoursEstimate.objects.get_or_create(
                job=job, role=query[0]
            )
            budget.hours = value
            budget.save()
            success = True
        else:
            query = models.Task.objects.filter(name=field)
            if query:
                budget, _ = models.JobTaskEstimate.objects.get_or_create(
                    job=job, task=query[0]
                )
                budget.hours = value
                budget.save()
                success = True
    if success:
        return Response(
            {
                "result": "success",
                "data": {"field": field, "value": "{:.2f}".format(value)},
            }
        )
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@login_required
@user_passes_test(permissions.is_level_4)
def inactive_job_api(request, pk):
    job = get_object_or_404(models.Job, pk=pk)
    status_id = request.POST.get("status")
    if status_id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        new_status = models.Status.objects.get(id=status_id)
    except models.Status.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    job.status = new_status
    job.save()
    if new_status.name in ["On hold", "Other"]:
        return Response({"result": "success", "remove": False})
    return Response({"result": "success", "remove": True})
