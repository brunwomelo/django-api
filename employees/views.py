from rest_framework import generics
from .serializers import EmployeeSerializer
from .models import Employee
from django.shortcuts import render
from django.views.generic import  ListView

# Create your views here.
class EmployeeListCreateAPIView (generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

employee_list_create_view = EmployeeListCreateAPIView.as_view()

class EmployeeRetrieveUpdateDestroyAPIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

employee_read_update_delete_view = EmployeeRetrieveUpdateDestroyAPIView.as_view()


class EmployeeList(ListView):
    template_name = 'employees.html'
    model = Employee

employee_page_view = EmployeeList.as_view()

def EmployeeListView(request):

    employees = Employee.objects.all()

    context = {
        'employees': employees,
    }
    return render(request,'employees.html', context)