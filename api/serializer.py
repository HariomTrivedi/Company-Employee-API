from rest_framework import serializers
from api.models import Company, Employee

# Create serializers
class CompanySerializer(serializers.HyperlinkedModelSerializer):  # Corrected class name
    company_id = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = "__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = "__all__"
