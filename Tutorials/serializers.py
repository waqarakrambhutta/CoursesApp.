from rest_framework import serializers
from .models import Author

class AuthorSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['phone','user']


 