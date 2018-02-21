from django.urls import  path
from . import  views

urlpatterns = [
    path("", views.projectIndex, name="index"),
    path('<int:project_id>/', views.projectDetail, name='detail'),

]