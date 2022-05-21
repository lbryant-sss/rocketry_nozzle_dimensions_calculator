from django.db import models

# Create your models here.
class PDF(models.Model):
    pdf_name = 'Nozzle Demensions'
    slug = 'nozzle_dimensions'
    generate_pdf = models.FileField()

    def get_absolute_url(self):
        return self.pdf_name
    
    def __str__(self):
        return self.slug