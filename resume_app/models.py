from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    linkedin = models.URLField()
    github = models.URLField()

    career_objective = models.TextField()
    education = models.TextField()
    technical_skills = models.TextField()
    projects = models.TextField()
    certifications = models.TextField()
    soft_skills = models.TextField()

    def __str__(self):
        return self.name