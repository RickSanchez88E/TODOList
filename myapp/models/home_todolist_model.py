# models.py

from django.db import models

class home_todolist_model(models.Model):
    STATUS_CHOICES = (
        (1, 'Done'),
        (2, 'In Progress'),
        (3, 'Not Start'),
    )

    status = models.IntegerField(choices=STATUS_CHOICES)
    task_name = models.CharField(max_length=200)
    due_date = models.DateField()

    def __str__(self):
        return self.task_name
    # 可以根据需要添加其他字段，如 tags, priority 等