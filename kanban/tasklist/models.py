from django.db import models




class TaskItem(models.Model):
    title = models.CharField(max_length=255)
    BACKLOG = 'BL'
    READY = 'RD'
    DOING = 'DO'
    DONE = 'DN'
    STATUS_CHOICES = (
        (BACKLOG, 'Backlog'),
        (READY, 'Ready'),
        (DOING, 'Doing'),
        (DONE, 'Done'),
        )
    status = models.CharField(max_length=2,
        choices=STATUS_CHOICES,
        default=BACKLOG,
        )
    
    @staticmethod
    def get_next_priority():
        items = TaskItem.objects.order_by('-priority')
        if len(items) == 0:
            return 1
        else:
            return items[0] + 1

    priority = models.IntegerField(unique=True, default=get_next_priority)

    def __str__(self):
        return "{}: {}-{}".format([self.title,STATUS_CHOICES[self.status], self.priority])
