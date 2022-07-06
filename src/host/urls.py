from django.urls import path

from . import views
from .views import HostAdminApiView


urlpatterns = [
    path('', views.HostApiView.as_view({
        'get': 'list',
        'post': 'create'}), name='view-create'),

    path('<int:pk>/', views.HostApiView.as_view({'patch': 'partial_update'}), name='update'),

    path('admin/', HostAdminApiView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='admin-view-create'),

    path('admin/<int:pk>/', views.HostAdminApiView.as_view({'patch': 'partial_update'}), name='admin-update')
]
