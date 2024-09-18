from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (0, 'Admin Niveau 0'),
        (1, 'Expert (Admin Niveau 1)'),
    )
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES, default=1)

    def is_admin_level_0(self):
        return self.user_type == 0

    def is_expert(self):
        return self.user_type == 1