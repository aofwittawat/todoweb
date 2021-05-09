from django.db import models

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.project_name


class Alltask(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    task_desc = models.TextField(null=True, blank=True)
    task_status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}  ({})'.format(self.task_name, self.project.project_name)
