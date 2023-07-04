from django.contrib import admin
from .models import Author,Courses,Chapter

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['phone','user']
    autocomplete_fields = ['user']
    search_fields = ['user__istartswith']
    autocomplete_fields = ['user']

@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','language','description','author']
    search_fields = ['language__istartswith']
    autocomplete_fields = ['author']

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['course','chapterNo','content']
    autocomplete_fields= ['course']