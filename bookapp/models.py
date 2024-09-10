from django.db import models

# Create your models here.
def get_image_filename(instance, filename):
    return f'book_media/{filename}'

class bookapp(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    author=models.CharField(max_length=200)
    quantity=models.IntegerField()
    image=models.ImageField(upload_to=get_image_filename,null=True,blank=True)

    
    def __str__(self):
        return self.name