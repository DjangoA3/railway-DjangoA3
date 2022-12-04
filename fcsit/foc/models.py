from django.db import models

# Create your models here.
class fcsit(models.Model):

   first_name   = models.CharField(max_length = 30)
   last_name    = models.CharField(max_length = 30)
   reg_no       = models.CharField(max_length = 30)
   department   = models.CharField(max_length = 30)
   faculty      = models.CharField(max_length = 30)

   def __str__(self):
      return self.reg_no