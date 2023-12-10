from django.db import models


class DefaultBaseModel(models.Model):
    created_at = models.DateField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)
