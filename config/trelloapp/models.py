from django.db import models

# Create your models here.
class Document(models.Model):
    FILE_CHOICES = (
    ('graphic','GRAPHIC'),
    ('code', 'CODE'),
    ('hr', 'HR'),
    ('document', 'DOCUMENT'),
    ('other', 'OTHER'),
    )

    name=models.CharField(max_length=64,default='admin')
    description = models.CharField(max_length=255)
    document = models.FileField(upload_to='documents/',default='')
    filetype = models.CharField(max_length=16   , choices=FILE_CHOICES, default='graphic')
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

