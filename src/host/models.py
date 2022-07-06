from django.contrib.auth import get_user_model
from django.db import models


HOST_TYPES = (
    ('SQL', 'SQl'),
    ('Windows', 'Windows'),
    ('Linux', 'Linux')
)


class Host(models.Model):
    ip_address = models.CharField(max_length=15)
    port = models.IntegerField()
    host_type = models.CharField(choices=HOST_TYPES, max_length=10)
    users = models.ManyToManyField(get_user_model(), blank=True, related_name='hosts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.host_type} {self.ip_address}:{self.port}'
