from django.db import models
from django.utils import timezone


class Post(models.Model):
    file = models.ImageField(upload_to='img/')
    text = models.TextField()


    def publish(self):
        self.save()

        def image_img(self):
            if self.file:
                return u'< img src="%s" width="100"/>' % self.file.url
            else:
                return '(none)'

        image_img.short_description = 'Thumb'
        image_img.allow_tags = True



