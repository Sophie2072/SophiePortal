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

def test_time_filter(self):
    query = models.Hour.objects.filter(start__gte="2020-01-01T08:00:00+00")\
        .filter(end__lte="2020-01-02T8:00:00+00")\
        .order_by("start")
    self.assertStatusGET(
        "timesheet_api_get_events",
        200,
        data={"start": "2020-01-01 8:00:00", "end": "2020-01-02 8:00:00"},
    )
    # self.get_content() 得到的是网页的response content，是 string ，
    # 这里花了很长时间去compare格式，其实只要把strin 变成json就可以了，json.loads()
    self.assertEqual(json.loads(self.get_content()), [x.as_json() for x in query])

   def test_created_hour_is_correct(self):
        self.assertStatusPOST(
            "timesheet_api_create_event",
            200,
            data={
                "start": "2020-01-01T12:00:00+00:00",
                "end": "2020-01-01T16:00:00+00:00",
                "job": self.job.id,
                "task": self.task.id,
            },
        )
        self.hour.refresh_from_db()  # This will update the existing hour object from the database, a cleaner way than using a query.
        self.assertEqual(hour.job.name, self.job.name)
        self.assertEqual(hour.task.name, self.task.name)
        self.assertEqual(hour.start, datetime.datetime(2020, 1, 1, 12, 0, 0, tzinfo=pytz.utc))
        self.assertEqual(hour.end, datetime.datetime(2020, 1, 1, 16, 0, 0, tzinfo=pytz.utc))


