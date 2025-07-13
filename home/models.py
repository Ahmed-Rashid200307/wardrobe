from django.db import models

# Create your models here.


# color model

# size model

# category model
class Category(models.Model):

  class Meta:
    verbose_name_plural = "Categories"

  name = models.CharField(max_length=30)
  code = models.IntegerField()

  def __str__(self):
    return self.name

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
    Extra_Small:"Extra Small",
    Small:"Small",
    Medium:"Medium",
    Large:"Large",
    Extra_Large:"Extra Large",
    Extra_Extra_Large:"Extra Extra Large",
  }

  size = models.CharField(choices=choices, default=Medium)
  price = models.IntegerField()
  composition = models.CharField(max_length=30)
  stock = models.IntegerField(null=True)
  inStock = models.BooleanField()
  code = models.IntegerField()
  description = models.TextField()

  def save(self, *args, **kwargs):
            self.inStock = (self.stock != 0)
            super().save(*args, **kwargs)

  def __str__(self):
    return self.name

class Variant(models.Model):
  dress = models.ForeignKey(Dress, models.CASCADE)
  image = models.ImageField(upload_to="images/variants")

  def __str__(self):
    return self.dress.name+"_" + str(self.id)