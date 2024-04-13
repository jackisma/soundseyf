from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    subject = models.CharField(max_length = 255,blank=True,null=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on =  models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
       return '{} - {}'.format(self.name, self.id)