from django.db import models
class Task(models.Model):
   TaskTitle = models.CharField(max_length=30)
   TaskDescription = models.TextField()
   time = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.TaskTitle
   
