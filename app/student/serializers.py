"""
Serializers for students APIs
"""
from rest_framework import serializers
from core.models import Student


class StudentSerializer(serializers.ModelSerializer):
    """Serializer for students."""

    class Meta:
        model = Student
        fields = ['id', 'number', 'name', 'faculty_name']
        read_only_fields = ['id']
