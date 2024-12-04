from django.contrib.auth.models import User
from django.db import models


class UserProfile(User):
    group = models.ForeignKey(
        "group_service.Group", on_delete=models.DO_NOTHING, null=True, blank=True
    )

    def __str__(self):
        return f"{self.username}"


class Account(models.Model):
    employee_id = models.CharField(max_length=16, unique=True)
    user = models.OneToOneField(
        UserProfile,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="account",
    )

    def __str__(self):
        return f"{getattr(self.user, 'username', 'user not assigned')} | {self.employee_id}"
