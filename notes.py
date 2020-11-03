### FOR Take Note Purpose

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