from django.db import models
from itertools import zip_longest




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
    LARGEST_POSSIBLE_PRIORITY =  2147483647
    priority = models.IntegerField(unique=True, default=LARGEST_POSSIBLE_PRIORITY)

    @staticmethod
    def get_next_priority():
        items = TaskItem.objects.order_by('-priority')
        if len(items) == 0:
            return 1
        else:
            return items[0].priority + 2

    @staticmethod
    def zipped():
        backlog= TaskItem.objects.filter(status=TaskItem.BACKLOG).order_by('priority')
        ready = TaskItem.objects.filter(status=TaskItem.READY).order_by('priority')
        doing = TaskItem.objects.filter(status=TaskItem.DOING).order_by('priority')
        done = TaskItem.objects.filter(status=TaskItem.DONE).order_by('priority')
        return zip_longest(backlog, ready, doing, done, fillvalue=None)

    def __str__(self):
        return "{}: {}-{}".format(self.title, self.get_status_display(), self.priority)

    def save(self,**kwargs):
        if self.priority == self.LARGEST_POSSIBLE_PRIORITY:
            self.priority = TaskItem.get_next_priority()
        if self.priority % 2 ==0:
            priorities_to_increment = TaskItem.objects.filter(priority__gt=self.priority).order_by('-priority')
            for item in priorities_to_increment:
                item.priority+=2
                item.save()
            self.priority += 1
        super(TaskItem, self).save(**kwargs)
