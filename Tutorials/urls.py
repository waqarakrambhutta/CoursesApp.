from django.urls import path,include
from . import views

urlpatterns = [
    path('author/',views.AuthorView),
    path('course/',views.CourseView),
    path('course/chapter/<int:id>',views.ChapterView)
]
