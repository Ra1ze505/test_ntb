from django.urls import path, include

from .views import CreateUserApiView


urlpatterns = [
    path('', include('rest_framework.urls')),
    path('register/', CreateUserApiView.as_view(), name='register')
]
