from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Person(models.Model):
  name = models.CharField(null=False,max_length=50)
  age = models.IntegerField(null=False, validators=[
    MinValueValidator(0), MaxValueValidator(130)
  ])

  def __str__(self) -> str:
    return f'{self.name} {self.age}'
  
