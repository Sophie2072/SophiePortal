### 20201109 Test
@freeze_time(make_aware(datetime(2020, 1, 1, 12, 0, 0)))
def test_with_available_sample(self):
    sample = models.Sample.objects.create(
        project=self.project,
        quota=self.quota,
        state=self.state,
        number="12345678910",
        survey_link="https://www.google.com",
    )
    sample.save()
    self.assertStatusGET("cati_api_start_new_call", 200,
                         url_args=[self.project.id])
    self.assertJSONEqual(self.get_content(), {            # !!!
        "result": "success",
        "data": {"id": 1,
                 "number": "12345678910",
                 "quota": "Test",
                 "name": "Unknown",
                 "notes": "",
                 "survey_link": "https://www.google.com",
                 "state": "Test",
                 "old_status": "A"}
    })