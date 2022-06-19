"""
Views for the student APIs.
"""
from django.http import Http404
from core.models import Student
from student.serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import generics
from rest_framework import filters


class CustomSearchFilter(filters.SearchFilter):
    """
    Custom search filter for StudentList api.
    """
    search_param = "name"


class StudentList(generics.CreateAPIView, generics.ListAPIView):
    """
    Retrieve all students, retrieve students whose names contain a
    particular regex, or create new student.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [CustomSearchFilter]
    search_fields = ['$name']


class StudentDetail(APIView):
    """
    Retrieve, update or delete a student instance.
    """
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request: Request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request: Request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
