from django.db import models

# Create your models here.

CATGORY_CHOICES = (
    ('A','ACTION'),
    ('D','DRAMA'),
    ('C','COMEDY'),
    ('R','ROMANCE')
)

LANGUAGE_CHOICES = (
    ('EN','ENGLISH'),
    ('GR','GERMAN')
)

STATUS_CHOICES = (
    ('RA', 'RECENTLY ADDED'),
    ('MW', 'MOST WATHCED'),
    ('TR', 'TOP RATED')
)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movie')
    category = models.CharField(choices=CATGORY_CHOICES, max_length=1)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    year_of_production = models.DateField()
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

#   - tags
#    - downloads link
#   - watch links