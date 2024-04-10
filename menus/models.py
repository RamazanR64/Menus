from django.db import models
from django.urls import resolve

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.url:
            return self.url
        else:
            return resolve(self.parent.get_absolute_url()).urlpath + self.get_relative_url()

    def get_relative_url(self):
        try:
            return f'/{self.pk}{self.get_named_url()}'
        except:
            return ''

    def get_named_url(self):
        try:
            return f'#{self.url.split("#")[1]}'
        except:
            return ''
