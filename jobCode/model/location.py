from django.db import models
import uuid

class LocationModel(models.Model):
    location = models.CharField(max_length=100)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class Meta:
        db_table = "locationmodel"
        app_label = 'jobCode'

        