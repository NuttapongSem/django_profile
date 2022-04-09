from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('abouts/', views.abouts, name='abouts'),
    path('delete_skill/<int:id>', views.deleteSkil, name='delete-skill')
]
