from django.urls import path

from . import api


urlpatterns = [
    path('', api.job_list, name='job_list'),
    path('<uuid:pk>/', api.job_detail, name='job_detail'),
    path('<uuid:pk>/delete/', api.job_delete, name='job_delete'),
    path('<uuid:pk>/report/', api.job_report, name='job_report'),
    path('profile/<uuid:id>/', api.job_list_profile, name='job_list_profile'),
    path('create/', api.job_create, name='job_create'),
]