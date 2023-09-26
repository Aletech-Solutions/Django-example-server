import uuid
from django.db import models

class LoggerModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    endpoint = models.CharField(max_length=255)
    payload = models.TextField()
    method = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "loggermodel"
        app_label = 'jobCode'

    def __str__(self):
        return f'{self.method} {self.endpoint} ({self.timestamp})'