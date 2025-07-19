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

###Each category dress

class Dress(models.Model):

  class Meta:
    verbose_name_plural = "Dresses"

  category = models.ForeignKey(Category, models.CASCADE)
  name = models.CharField(max_length=40)

  Extra_Small = "XS"
  Small = "S"
  Medium = "M"
  Large = "L"
  Extra_Large = "XL"
  Extra_Extra_Large = "XXL"
  
  choices = {
    (Extra_Small,"Extra Small"),
    (Small,"Small"),
    (Medium,"Medium"),
    (Large,"Large"),
    (Extra_Large,"Extra Large"),
    (Extra_Extra_Large,"Extra Extra Large"),
  }

  size = models.CharField(choices=choices, default=Medium, max_length=4)
  price = models.IntegerField()
  composition = models.CharField(max_length=30)
  stock = models.IntegerField(null=True)
  inStock = models.BooleanField()
  code = models.IntegerField(unique=True)
  description = models.TextField()
  default_image = models.ImageField(unique=True,upload_to="images/default",blank=True)

  def collision(self):
     if Variant.objects.filter(image = self.default_image).exists():
        raise ValidationError({"image":"Image already selected for variant image.\nPlease select a different image."})
     

  def save(self, *args, **kwargs):
            self.collision()
            self.inStock = (self.stock != 0)
            super().save(*args, **kwargs)

  def __str__(self):
    return self.name
  
###Variants for each dress

class Variant(models.Model):
  dress = models.ForeignKey(Dress, models.CASCADE)
  image = models.ImageField(upload_to="images/variants",blank=True)

  def collision(self):
    if Dress.objects.filter(default_image = self.image).exists():
      raise ValidationError({"image":"Image already selected for default image.\nPlease select a different image."})

  def __str__(self):
    return self.dress.name+"_" + str(self.id)
  
  def save(self, *args, **kwargs):
          self.collision()
          super().save(*args, **kwargs)