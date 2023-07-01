from django.contrib import admin
from .models import Author,Courses

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['phone','user']
    search_fields = ['user']


@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','language','description','author']