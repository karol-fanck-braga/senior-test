from django.db import models
from django.db import models

class Task(models.Model):
    STATUS = (
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    status = models.CharField(max_length=12, choices=STATUS, default='in_progress')
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add_date=True)
