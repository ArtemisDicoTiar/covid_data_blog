from django.db import models


# Create your models here.

class FacebookSubscription_model(models.Model):
    recipient_id = models.TextField(primary_key=True, unique=True)
    name = models.TextField()
    locale = models.TextField()
    timezone = models.IntegerField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'Facebook_subscription'
