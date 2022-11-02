from django.urls import include
from django.urls import path
from . import views


#router
from rest_framework import routers
router = routers.DefaultRouter()
router.register('questions', views.QuestionViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('index/', views.index, name='index'),
]