from django.urls import path
from . import views

urlpatterns = (
    path('', views.employee_list_create_view),
    path('<int:pk>/', views.employee_read_update_delete_view),
    path('page/', views.EmployeeListView),
)
