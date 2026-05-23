from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import JobOpportunity


class JobOpportunitySerializer(serializers.ModelSerializer):
    employer_name = serializers.CharField(
        source='employer.organisation_name',
        read_only=True
    )

    class Meta:
        model = JobOpportunity
        fields = [
            'id',
            'title',
            'description',
            'salary_range',
            'status',
            'employer_name',
        ]


class JobOpportunityListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JobOpportunitySerializer
    queryset = JobOpportunity.objects.filter(
        status='open'
    ).select_related('employer')