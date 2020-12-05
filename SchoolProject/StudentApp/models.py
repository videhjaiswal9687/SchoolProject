from django.db import models
from django.db.models import Model
from django.utils import timezone

# Create your models here.
class Student(models.Model):
      name=models.CharField(max_length=100)
      rollno=models.IntegerField(default=0)
      course=models.CharField(max_length=100)
      fee=models.FloatField(default=0.0)
      pub_date=models.DateTimeField('date published',default=timezone.now())

      def __str__(self):
        return "{0}, {1}, {2}, {3}, {4}".format(self.name,self.rollno,self.course,self.fee,self.pub_date)  