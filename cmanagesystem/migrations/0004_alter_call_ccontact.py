# Generated by Django 4.0 on 2021-12-10 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmanagesystem', '0003_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='cContact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cont', to='cmanagesystem.product'),
        ),
    ]
