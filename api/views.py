from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializer import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    #custom API
    # Companies/{companiesID}/employees

    @action(detail = True, methods = ['get'])
    def employees(self,request,pk=None):
        company = Company.objects.get(pk=pk)
        emps = Employee.objects.filter(company=company) 
        emps_serializer = EmployeeSerializer(emps , many=True, context = {'request': request})
        return Response(emps_serializer.data)
    
class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer