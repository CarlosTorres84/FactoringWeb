# Generated by Django 4.2.7 on 2024-02-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dcarteira',
            name='car_titulonumero',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
