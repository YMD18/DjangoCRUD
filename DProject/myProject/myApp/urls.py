from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewStudents),

    path('addStudent/', views.addStudent, name='addStudent'),

    path('editStudent/<int:studentID>/', views.editStudent, name='editStudent'),

    path('delete/<int:studentID>/', views.deleteStudent, name='deleteStudent'),

    path('confirmDelete/<int:studentID>', views.confirmDelete, name='confirmDelete'),
]