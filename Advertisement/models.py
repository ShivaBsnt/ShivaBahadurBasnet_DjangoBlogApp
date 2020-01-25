from django.db import models


class Ads(models.Model):
    ads_title = models.CharField(max_length=300)
    ads_image = models.ImageField(upload_to='advertisement_pics')
    ads_content = models.TextField()
    ads_href = models.CharField(max_length=300)
