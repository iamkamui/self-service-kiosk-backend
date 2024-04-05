from django.db import models


class OrderStatusChoices(models.TextChoices):
    ORDERING = "ORDERING", "Ordering"
    CANCELED = "CANCELED", "Canceled"
    QUEUE = "ON QUEUE", "On queue"
    PREPARING = "PREPARING", "Preparing"
    READY = "READY", "Ready"


class OrderConsumptionChoices(models.TextChoices):
    TAKE_HOME = "TAKE HOME", "Take home"
    EAT_IN = "EAT IN", "Eat in"
    DELIVERY = "DELIVERY", "Delivery"
