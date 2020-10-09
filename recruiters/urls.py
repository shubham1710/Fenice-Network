from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.rec_details, name='detail-recruiters'),
    path('job/add', views.add_job, name='add-job'),
    path('job/<slug>/edit/', views.edit_job, name='edit-job-post'),
    path('job/<slug>', views.job_detail, name='add-job-detail'),
    path('jobs/', views.all_jobs, name='job-list'),
    path('candidate/search/', views.search_candidates, name='search-candidates'),
    path('job/<slug>/search/', views.job_candidate_search,
         name='job-candidate-search'),
    path('job/<slug>/applicants', views.applicant_list, name='applicant-list'),
    path('job/<slug>/selected', views.selected_list, name='selected-list'),
    path('job/<job_id>/select-applicant/<can_id>/',
         views.select_applicant, name='select-applicant'),
    path('job/<job_id>>/remove-applicant/<can_id>/',
         views.remove_applicant, name='remove-applicant'),
]
