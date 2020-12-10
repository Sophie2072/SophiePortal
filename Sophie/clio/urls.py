from django.urls import path


from .import views,api

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:pk>/costing/api/", api.budget_api, name="job_costing_api"),
    path("<int:pk>/checklist/api/", api.new_checklist_api, name="job_checklist_api"),
    path(
        "<int:pk>/checklist/api/note/",
        api.checklist_notes_api,
        name="job_checklist_notes_api",
    ),
]