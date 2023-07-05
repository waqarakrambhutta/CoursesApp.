from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Author,Courses,Chapter
from .serializers import AuthorSerialiser,CourseSerializer,ChapterSerializer

# Create your views here.
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerialiser


    

@api_view()
def CourseView(request):
    course = Courses.objects.all()
    serializer = CourseSerializer(course,many=True)
    return Response(serializer.data)

@api_view()
def ChapterView(request,id):
    try:
        chapter = Chapter.objects.get(pk=id)
        serializer = ChapterSerializer(chapter)
        return Response(serializer.data)
    except Chapter.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)