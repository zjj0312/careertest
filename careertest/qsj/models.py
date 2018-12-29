from django.db import models

# Create your models here.
class UserAdmin(models.model):
	user=models.CharField(max_length=20)
	password=models.CharField(max_length=20)
	email=models.EmailField()

class UserHR(models.model):
	user=models.CharField(max_length=20)
	password=models.CharField(max_length=20)
	email=models.EmailField()
	company_id=models.ForeignKey(to='Company',on_delete=models.CASCADE)

class UserExpert(models.model):
	user=models.CharField(max_length=20)
	password=models.CharField(max_length=20)
	email=models.EmailField()

class Company(models.model):
	logo=models.ImageField()
	name=models.CharField(max_length=100)
	info=models.TextField()
class Factor(models.model):
	name=models.FileField(max_length=100)

class Moding(models.model):
	name=models.FileField(max_length=100)
	factor1_id=models.ForeignKey(to='Factor',on_delete=models.CASCADE)
	factor2_id=models.ForeignKey(to='Factor',on_delete=models.CASCADE)
	factor3_id=models.ForeignKey(to='Factor',on_delete=models.CASCADE)
	factor4_id=models.ForeignKey(to='Factor',on_delete=models.CASCADE)
	factor5_id=models.ForeignKey(to='Factor',on_delete=models.CASCADE)
	factor6_id=models.ForeignKey(to='Factor',on_delete=models.CASCADE)
	factor7_id=models.ForeignKey(to='Factor',on_delete=models.CASCADE)
	factor8_id=models.ForeignKey(to='Factor',on_delete=models.CASCADE)
	factor1_ex_value=models.DecimalField(max_digits=5,decimal_places=2)
	factor2_ex_value=models.DecimalField(max_digits=5,decimal_places=2)
	factor3_ex_value=models.DecimalField(max_digits=5,decimal_places=2)
	factor4_ex_value=models.DecimalField(max_digits=5,decimal_places=2)
	factor5_ex_value=models.DecimalField(max_digits=5,decimal_places=2)
	factor6_ex_value=models.DecimalField(max_digits=5,decimal_places=2)
	factor7_ex_value=models.DecimalField(max_digits=5,decimal_places=2)
	factor8_ex_value=models.DecimalField(max_digits=5,decimal_places=2)


