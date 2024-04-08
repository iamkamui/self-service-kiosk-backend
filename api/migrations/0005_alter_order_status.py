# Generated by Django 5.0.3 on 2024-04-01 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_order_options_order_consumption_order_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("ORDERING", "Ordering"),
                    ("CANCELED", "Canceled"),
                    ("ON QUEUE", "On queue"),
                    ("PREPARING", "Preparing"),
                    ("READY", "Ready"),
                ],
                default="ORDERING",
                max_length=20,
                verbose_name="order status",
            ),
        ),
    ]