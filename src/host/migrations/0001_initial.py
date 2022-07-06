# Generated by Django 4.0.6 on 2022-07-06 21:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=15)),
                ('port', models.IntegerField()),
                ('host_type', models.CharField(choices=[('SQL', 'SQl'), ('Windows', 'Windows'), ('Linux', 'Linux')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('users', models.ManyToManyField(related_name='hosts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]