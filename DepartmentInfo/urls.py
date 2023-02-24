from django.urls import path
from .views import departmentApi

urlpatterns=[
     path('', departmentApi.as_view()),
     path('/<int:pk>', departmentApi.as_view())
]