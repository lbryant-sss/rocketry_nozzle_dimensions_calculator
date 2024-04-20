from django.db import models

# Create your models here.
class PDF(models.Model):
    slug = 'nozzle_dimensions'
    pdf_name = models.CharField(max_length=255, default='Nozzle Demensions')
    generate_pdf = models.FileField()
    file_path = models.CharField(max_length=255, default='/')

    
    
    def __str__(self):
        return self.file_path