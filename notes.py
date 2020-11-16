### FOR Take Note Purpose

# 20201116 hasattr()

@api_view(["POST"])
@login_required
@user_passes_test(permissions.is_level_4)
def inactive_job_api(request, pk):
    job = get_object_or_404(models.Job, pk=pk)
    status_id = request.POST.get('status')  # 'status' get from HTML form-select name, HTML select pass data from name
    if status_id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        new_status = models.Status.objects.get(id=status_id)
    except models.Status.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    job.status = new_status
    job.save()
    return Response({"result": "success"})

def get_sample_history(request, sample_id):
    sample = get_object_or_404(models.Sample, id=sample_id)
    query = models.Call.objects.filter(
        sample=sample
    ).order_by("-end_time").select_related("caller", "outcome", "appointment")[:10]
    if query:
        data = []
        for call in query:
            datum = {
                "Caller": call.caller.get_full_name(),
                "Time": call.get_start_time().isoformat(),
                "Outcome": call.outcome.name,
            }
            if call.outcome.result == models.Sample.Status.APPOINTMENT and hasattr(call, "appointment"):     ### hasattr(object, attrname), can check has attribute or not
                datum["Appointment Time"] = call.appointment.time.isoformat()
                datum["Appointment Notes"] = call.appointment.notes
            data.append(datum)
        df = pd.DataFrame.from_records(data)
        return HttpResponse(df.to_html(
            na_rep="N/A",
            classes=["table", "table-hover"],
            border=0,
            justify="start",
            index=False
        ))
    else:
        return HttpResponse("No calls have been made to this number.")