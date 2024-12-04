from django.db import models


class Location(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    coordinates = models.CharField(max_length=32)
    group = models.ForeignKey(
        "group_service.Group", on_delete=models.CASCADE, related_name="locations"
    )

    def __str__(self):
        return f"Group {self.group.name} at {self.date_time}"
