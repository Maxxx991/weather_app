from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __srt__(self):
        return self.name

    def clean(self):
        self.name = self.name.capitalize()
        
    def check_luck_of_numbers(self, x):
        flag = True
        for i in x.cleaned_data['name']:
            try:
                if int(i):
                    flag = False
                    return flag
            except:
                continue
        if flag:
            return flag
