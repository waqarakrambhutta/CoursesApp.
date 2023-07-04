from rest_framework import serializers
from .models import Author,Courses,Chapter

class AuthorSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['phone','user']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['title','language','description','author']

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['course','chapterNo','content']

