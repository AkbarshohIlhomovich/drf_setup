from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.conf import settings


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan sana")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_created",
        verbose_name="Yaratgan foydalanuvchi"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_updated",
        verbose_name="Yangilagan foydalanuvchi"
    )

    class Meta:
        abstract = True


class StateChoices(models.TextChoices):
    ACTIVE = 'active', 'Faol'
    INACTIVE = 'inactive', 'Nofaol'
    DELETED = 'deleted', 'O\'chirilgan'
    PENDING = 'pending', 'Kutilmoqda'
    SUSPENDED = 'suspended', 'To\'xtatilgan'


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefon raqami")
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True, verbose_name="Profil rasmi")

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username


