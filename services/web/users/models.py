from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(max_length=200, blank=True, 
                        verbose_name="Biography", null=True,
                        help_text="Краткая биография пользователя.")
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    def __str__(self):
        return self.username
    