from django.db import models

class Header(models.Model):
    logo = models.ImageField(upload_to='travel/')
    phone = models.CharField(max_length=13)
    tg_link = models.CharField(max_length=255)

    def __str__(self):
        return self.tg_link

class Navbar(models.Model):
    image = models.ImageField(upload_to='navbar/')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Travel(models.Model):
    airline = models.CharField(max_length=255)
    duration = models.IntegerField()
    eating = models.IntegerField()
    viza = models.CharField(max_length=255)
    medical_care = models.CharField(max_length=255)
    information = models.CharField(max_length=255)
    five_liter = models.CharField(max_length=255)
    jilet = models.CharField(max_length=255)
    bag_and_badge = models.CharField(max_length=255)

    def __str__(self):
        return self.airline

class Comment(models.Model):
    text = models.TextField()
    travel = models.ForeignKey(Travel,on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Description(models.Model):
    photo = models.ImageField(upload_to='description/',null=True,blank=True)
    text = models.TextField()

    def __str__(self):
        return self.text