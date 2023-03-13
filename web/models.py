from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
from tinymce.models import HTMLField

# Create your models here.
class Property (models.Model):
    property_name=models.CharField(max_length=20)
    property_location=models.CharField(max_length=50)
    property_image=models.ImageField()
    # property_feature=models.CharField(max_length=100)
    property_items=models.TextField()
    property_tag=models.TextField()
    
    def __str__(self):
        return self.property_name
    
class Banner(models.Model):
    Banner_image=models.ImageField()

class Testimonial(models.Model):
    Testimonial_image=models.ImageField()
    Testimonial_name=models.CharField(max_length=100)
    Testimonial_profession=models.CharField(max_length=30)
    Testimonial_sentence=models.TextField()


class Blog(models.Model):
    title=models.CharField(max_length=225)
    summary=models.CharField(max_length=335)
    date = models.DateField(auto_now=True)
    image = VersatileImageField('Image',upload_to='update/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')
    content= HTMLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Property1(models.Model):
    property_name=models.CharField(max_length=20)
    property_image=models.ImageField()
    property_items=models.TextField()

class professionals(models.Model):
    professionals_name=models.CharField(max_length=50)
    professionals_image=models.ImageField()
    professionals_post=models.CharField(max_length=50)

    def __str__(self):
        return self.professionals_name
    

class Agent(models.Model):
    agent_name=models.CharField(max_length=20)
    agent_image=models.ImageField()
    agent_post=models.CharField(max_length=20)

    def __str__(self):
        return self.agent_name
    

class professionalservices(models.Model):
    professionalservices_image=models.ImageField()
    professionalservices_title=models.CharField(max_length=50)
    professionalservices_sentence=models.TextField()

    def __str__(self):
        return self.professionalservices_title
    

# class contact(models.Model):
#     name=models.CharField(max_length=50)
#     email=models.EmailField()
#     subject=models.CharField(max_length=50)
#     phone=models.IntegerField()
#     message=models.TextField()

#     def __str__(self):
#         return self.name
    


class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.name



class services(models.Model):
    services_id=models.CharField(max_length=30)
    services_title=models.CharField(max_length=50)
    services_sentence=models.TextField()

    def __str__(self):
        return self.services_title
    

class brandspartners(models.Model):
    brandspartners_image=models.ImageField()

    def __str__(self) -> str:
        return super().__str__()
    
class Popularplaces(models.Model):
    Popularplaces_image=models.ImageField()
    Popularplaces_title=models.CharField(max_length=40)
    Popularplaces_details=models.CharField(max_length=100)
    










    