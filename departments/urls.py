from django.urls import path
from . import views

urlpatterns = (
    path('', views.department_list_create_view),
    path('<int:pk>/', views.department_read_update_delete_view),

)
