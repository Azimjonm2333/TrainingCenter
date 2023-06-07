from django.db import models
from common.models import BaseModel


class Course(BaseModel):

    title = models.CharField("Название", max_length=70)
    description = models.TextField("Описание", max_length=4096)
    duration = models.IntegerField('Длительность')

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self) -> str:
        return self.title