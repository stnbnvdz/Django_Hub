from django.db import models

class NameOfTutorial(models.Model):
    resources = models.CharField(max_length=100)
    def __str__(self):
        return self.resources

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

class DjangoHub(models.Model):
    name = models.ForeignKey(NameOfTutorial, on_delete=models.CASCADE)
    link = models.CharField(max_length=500)
    tags = models.CharField(max_length=100)
    format = models.CharField(max_length=50, null=True, choices=FORMAT)
    difficulty = models.CharField(max_length=50, null=True, choices=DIFFICULTY)
    time = models.CharField(max_length=50, null=True, choices=TIME)
