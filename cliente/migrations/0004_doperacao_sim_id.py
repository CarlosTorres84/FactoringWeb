# Generated by Django 4.2.7 on 2023-12-29 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_alter_doperacao_ope_bairro1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doperacao',
            name='sim_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cliente.dsimulacao'),
            preserve_default=False,
        ),
    ]