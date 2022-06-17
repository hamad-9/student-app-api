"""
URL mapping for the student app.
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from student import views

urlpatterns = [
    path('students/', views.StudentList.as_view()),
    path('students/<int:pk>/', views.StudentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
