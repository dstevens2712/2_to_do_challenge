from django.db import models
from datetime import date
# Create your models here.

class Task(models.Model):
    # An ID field is automatically added to all Django models
    description = models.CharField(max_length=255)


class Comment(models.Model):
    comment = models.CharField(max_length=255)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateField(default=date.today)

    def __str__(self):
        return self.comment

        class Meta:
            ordering = ['comment']
            

