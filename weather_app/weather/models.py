from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __srt__(self):
        return self.name

    def clean(self):
        self.name = self.name.capitalize()