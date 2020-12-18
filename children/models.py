from django.db import models

class children(models.Model):
	name=models.CharField(max_length=100)
	SEX_CHOICES=[('M','Male'),('F','Female')]
	sex = models.CharField(max_length=1, choices=SEX_CHOICES)
	age=models.IntegerField(null=True)
	def __str__(self):
		return self.name