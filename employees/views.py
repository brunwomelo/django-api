from rest_framework import generics
from .serializers import EmployeeSerializer
from .models import Employee

# Create your views here.
class EmployeeListCreateAPIView (generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

employee_list_create_view = EmployeeListCreateAPIView.as_view()

class EmployeeRetrieveUpdateDestroyAPIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

employee_read_update_delete_view = EmployeeRetrieveUpdateDestroyAPIView.as_view()

