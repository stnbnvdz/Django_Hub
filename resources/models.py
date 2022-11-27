from django.db import models

DIFFICULTY = (
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
)

TIME = (
    ('0-30 minutes', '0-30 minutes'),
    ('30 minutes - 1 hour', '30 minutes - 1 hour'),
    ('1-4 hours', '1-4 hours'),
    ('5-10 hours', '5-10 hours'),
    ('it takes days', 'it takes days'),
)

FORMAT = (
    ('Written', 'Written'),
    ('Video', 'Video'),
)

# Create your models here.
class Resources(models.Model):
  name = models.CharField(max_length=100)
  link = models.CharField(max_length=150)
  tags = models.CharField(max_length=50)
  format = models.CharField(max_length=50, null=True, choices=FORMAT)
  difficulty = models.CharField(max_length=50, null=True, choices=DIFFICULTY)
  time = models.CharField(max_length=50, null=True, choices=TIME)
