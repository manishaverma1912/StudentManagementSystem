from django.db import models

class Review(models.Model):
    name =models.CharField(max_length = 200)
    email = models.EmailField(max_length = 100)
    message = models.CharField(max_length = 500)


    def __Str__(self):
        return  f"{self.name} ({self.email})" 



    
