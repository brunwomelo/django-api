from rest_framework import generics
from .serializers import DepartmentSerializer
from .models import Department

# Create your views here.
class DepartmentListCreateAPIView (generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

department_list_create_view = DepartmentListCreateAPIView.as_view()

class DepartmentRetrieveUpdateDestroyAPIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

department_read_update_delete_view = DepartmentRetrieveUpdateDestroyAPIView.as_view()

