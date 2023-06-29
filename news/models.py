from django.db import models

# Create your models here.



# class StrudentInfo(models.Model):
#     lastName = models.CharField(max_length=200)
#     firstName = models.CharField(max_length=250)
#     phone_number = models.TextField()
#     b_day = models.DateField()

#     def _str_(self):
#         return self.lastName




class Course(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title



class Teacher(models.Model):
    full_name = models.TextField()
    image = models.ImageField(null=True)
    teaching_course = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.full_name




# Forma uchun model

class Application(models.Model):
    client_name = models.CharField(max_length=200)
    client_last_name = models.CharField('Familiya', max_length=255, null=True)
    client_phone_number = models.CharField(max_length=50)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"client_name: {self.client_name}, phone number: {self.client_phone_number}"








