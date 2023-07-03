from django.urls import path

from . import views


api_urls = [
    path('persons/', views.PersonView.as_view()),

    path('projects/', views.ProjectView.as_view()),
    path('projects/<int:project_id>', views.ProjectDetailsView.as_view())
    ]