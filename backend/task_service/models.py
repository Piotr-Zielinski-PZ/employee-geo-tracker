from django.conf import settings
from django.db import models


def get_statuses():
    return {i: i for i in settings.STATUSES}


class Task(models.Model):
    description = models.TextField()
    group = models.ForeignKey(
        "group_service.Group", on_delete=models.CASCADE, related_name="tasks"
    )
    location = models.OneToOneField(
        "location_service.Location", on_delete=models.CASCADE, related_name="tasks"
    )
    status = models.CharField(max_length=16, choices=get_statuses)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return (
            f"{self.group.name:=^3} | "
            f"{self.status:-^3} | "
            f"{self.description[:30]}"
        )

    @property
    def duration(self):
        if self.end:
            self.status = settings.statuses[1]
            return
        return self.end - self.start
