from django.urls import path
from . import views

urlpatterns = [
    path("employees", views.employee_list),             # GET all, POST new
    path("employees/<int:id>", views.employee_detail),  # PUT update, DELETE
]
