from django.db import models
from django.conf import settings

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    phone = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.user.username

class Courses(models.Model):
    title = models.CharField(max_length=64)
    language = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               null=False,
                               related_name='+'
                               )
    
    def __str__(self) -> str:
        return self.language
    

class Chapter(models.Model):
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    chapterNo = models.PositiveIntegerField(unique=True,primary_key=True)
    content = models.TextField()