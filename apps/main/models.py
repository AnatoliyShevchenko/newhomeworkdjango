from django.db import models

# Create your models here.
class Button(models.Model):
    symbol = models.CharField(
        max_length=10,
        verbose_name='символ кнопки',
        unique=True
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'кнопка'
        verbose_name_plural = 'кнопки'

    def __str__(self) -> str:
        return self.symbol

class Keyboard(models.Model):
    button = models.ForeignKey(
        Button,
        on_delete=models.CASCADE,
        verbose_name='кнопка',
        unique=True
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'клавиатура'
        verbose_name_plural = 'клавиатуры'

    def __str__(self) -> str:
        return self.button


