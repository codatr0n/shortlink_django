from django.db import models
from datetime import datetime

class Tag(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    code = models.TextField()
    type_choice = [
        (1, 'Retargeting'),
        (2, 'Analytics'),
        (3, 'Tracking'),
        (4, 'Tag manager'),
    ]
    tag_type = models.IntegerField(choices=type_choice, default=1)

    def __str__(self):
        return self.title + ' - type: ' + str(self.get_tag_type_display())


class Link(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=2000)
    shortcode = models.CharField(max_length=10, blank=True, null=True)
    date_created = models.DateTimeField('date published', default=datetime.now)
    tags = models.ManyToManyField('Tag', related_name='tags')

    def __str__(self):
        return self.title + ' - ' + self.url



