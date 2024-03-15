from django.db import models
from django.db import models

class Task(models.Model):
    STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    )
    PRIORITY_CHOICES = (
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='in_progress')
    priority = models.IntegerField(choices=(PRIORITY_CHOICES), default=1)
    created_at = models.DateTimeField(auto_now_add_date=True)
