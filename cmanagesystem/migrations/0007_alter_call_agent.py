# Generated by Django 4.0 on 2021-12-10 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmanagesystem', '0006_alter_product_customername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='agent',
            field=models.CharField(max_length=20),
        ),
    ]
