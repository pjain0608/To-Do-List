from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class History(models.Model):
    htitle = models.CharField(max_length=200)
    hdescription = models.TextField()

    def __str__(self):
        return self.htitle