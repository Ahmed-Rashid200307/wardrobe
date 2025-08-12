from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

# category model
class Category(models.Model):

  class Meta:
    verbose_name_plural = "Categories"

  name = models.CharField(max_length=30)
  code = models.IntegerField(unique=True)

  def __str__(self):
    return self.name

### size selection for each dress

class Size(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name
    
###Each category dress

class Dress(models.Model):

  class Meta:
    verbose_name_plural = "Dresses"

  category = models.ForeignKey(Category, models.CASCADE)
  name = models.CharField(max_length=40)
  size = models.ManyToManyField(Size)
  price = models.IntegerField()
  composition = models.CharField(max_length=30)
  stock = models.IntegerField(null=True)
  inStock = models.BooleanField()
  code = models.IntegerField(unique=True)
  description = models.TextField()
  default_image = models.ImageField(unique=True,upload_to="default",blank=False,null=False)

  def clean(self):

     if Dress.objects.filter(default_image = ("default/"+self.default_image.name)):
        raise ValidationError(f"Image already selected for another dress",code="invalid")

  def save(self, *args, **kwargs):
            self.inStock = (self.stock != 0)
            super().save(*args, **kwargs)

  def __str__(self):
    return self.name
  
###Variants for each dress

class Variant(models.Model):
  dress = models.ForeignKey(Dress, models.CASCADE)
  image = models.ImageField(upload_to="variants",blank=True)
# add varient code
# add name of color
  def clean(self):
    if self.dress.default_image.name.__contains__(self.image.name):
      raise ValidationError("Image already selected for default image.\nPlease select a different image or change the default image.", code="invalid")

  def __str__(self):
    return self.dress.name+"_" + str(self.id)
  
