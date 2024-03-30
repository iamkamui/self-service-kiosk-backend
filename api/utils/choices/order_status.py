from django.db import models


class OrderStatusChoices(models.TextChoices):
    CANCELED = "CANCELED", "Canceled"
    QUEUE = "ON QUEUE", "On queue"
    PREPARING = "PREPARING", "Preparing"
    READY = "READY", "Ready"
