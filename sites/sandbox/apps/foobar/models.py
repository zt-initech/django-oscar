from django.db import models


class MyNewModel(models.Model):
    foo = models.CharField(max_length=128)
    bar = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.foo
