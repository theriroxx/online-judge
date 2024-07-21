from django.db import models

# Create your models here.
class CodeSubmission(models.Model):
    lang = models.CharField(max_length=100)
    code = models.TextField()
    input = models.TextField(null=True,blank=True)
    output = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)