from django.db import models
from common.models import BaseModel


class Student(BaseModel):

    name = models.CharField("Имя", max_length=70, blank=True)
    surname = models.CharField("Фамилия", max_length=70, blank=True)
    email = models.EmailField("Почта", max_length=70, unique=True, blank=True)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self) -> str:
        return self.fullname
    
    @property
    def fullname(self) -> str:
        return f"{self.name} {self.surname}"

