from django.db import models

class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='Зовнішній ID користувача',
        unique=True
    )
    name = models.CharField(
        max_length=20,
        verbose_name='Им\'я користувача'
    )

    def __str__(self):
        return f'#{self.external_id} - {self.name}'

    class Meta:
        verbose_name = 'Профілі'
        verbose_name_plural = 'Профілі'


class Message(models.Model):
    profile = models.ForeignKey(
        to='my_telegram_bot.Profile',
        verbose_name='Профіль',
        on_delete=models.PROTECT,
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    created_at = models.DateTimeField(
        verbose_name='Час отримання',
        auto_now_add=True,
    )

    def __str__(self):
        return f'Повідомлення {self.pk} від {self.profile}'

    class Meta:
        verbose_name = 'Повідомлення'
        verbose_name_plural = 'Повідомлення'
