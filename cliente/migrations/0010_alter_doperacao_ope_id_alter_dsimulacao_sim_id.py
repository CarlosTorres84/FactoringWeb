# Generated by Django 4.2.7 on 2024-01-25 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0009_alter_dsimulacao_sim_valortotal1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doperacao',
            name='ope_id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dsimulacao',
            name='sim_id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
