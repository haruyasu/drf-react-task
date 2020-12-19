from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet, CreateUserView, MyProfileView

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
    path('myself/', MyProfileView.as_view(), name='myself'),
    path('register/', CreateUserView.as_view(), name='register'),
]