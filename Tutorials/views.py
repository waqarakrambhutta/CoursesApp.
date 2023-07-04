from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerialiser

# Create your views here.
@api_view()
def AuthorView(request):
    author = Author.objects.all()
    serializer = AuthorSerialiser(author,many=True)
    return Response(serializer.data)