from django.db import models
# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETE', 'Complete'),
    )
    user_id = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    status = models.CharField(choices=STATUS_CHOICES, default="NEW")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return JsonRespone(self.title, self.description)



