from django.db import models

# Create your models here.
class Categorie(models.Model):
    name = models.CharField(max_length = 50)
    icon = models.ImageField(upload_to="categories-icons")
    def __str__(self):
        return self.name
    

class Pages(models.Model):
    url = models.TextField()
    name = models.CharField(max_length = 50)
    categories = models.ForeignKey(Categorie,on_delete=models.PROTECT)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
    