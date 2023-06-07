from django.db import models
from common.models import BaseModelCreate


class Estimation(BaseModelCreate):

    estimation = models.IntegerField("Оценка")
    course = models.ForeignKey("course.Course", verbose_name="Курс", on_delete=models.CASCADE)
    student = models.ForeignKey("student.Student", verbose_name="Студент", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"

    def __str__(self) -> str:
        return self.student.fullname