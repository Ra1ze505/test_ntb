from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Host
from .serializers import HostSerializer, HostAdminSerializer


class HostApiView(viewsets.ModelViewSet):
    """View, create and update hosts"""
    model = Host
    serializer_class = HostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.hosts.all()

    def perform_create(self, serializer):
        serializer.save(users=[self.request.user])


class HostAdminApiView(viewsets.ModelViewSet):
    """
    View, create and update host for all users.
    Only for admin user
    """
    model = Host
    permission_classes = [IsAdminUser]
    queryset = Host.objects.all().prefetch_related('users')
    serializer_class = HostAdminSerializer

