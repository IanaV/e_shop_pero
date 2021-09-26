

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    city = models.CharField(max_length=64, default='', verbose_name='Город')
    phone = models.CharField(max_length=64, default='', verbose_name='Телефон')
    # avatar = models.ImageField(upload_to='profile_avatars/%Y/%m/%d', blank=True, null=True, verbose_name='Аватар',
    #                            default='media/profile_avatars/base.jpg')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    # @property
    # def image_url(self):
    #     if self.avatar and hasattr(self.avatar, 'url'):
    #         return self.avatar.url
    #     else:
    #         return "'media/profile_avatars/base.jpg"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

