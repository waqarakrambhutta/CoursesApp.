from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('author',views.AuthorViewSet)



urlpatterns = [
    path('course/',views.CourseView),
    path('course/chapter/<int:id>',views.ChapterView)
] + router.urls
