# Generated by Django 5.1.3 on 2024-12-04 11:30

import django.db.models.deletion
import task_service.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("group_service", "0001_initial"),
        ("location_service", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=task_service.models.get_statuses, max_length=16
                    ),
                ),
                ("start", models.DateTimeField(auto_now_add=True)),
                ("end", models.DateTimeField(blank=True, null=True)),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to="group_service.group",
                    ),
                ),
                (
                    "location",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to="location_service.location",
                    ),
                ),
            ],
        ),
    ]