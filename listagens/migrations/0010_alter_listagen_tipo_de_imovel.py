# Generated by Django 3.2.4 on 2021-06-25 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listagens', '0009_listagen_tipo_de_imovel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listagen',
            name='tipo_de_imovel',
            field=models.CharField(blank=True, choices=[('URBANO', 'Urbano'), ('RURAL', 'Rural')], max_length=100),
        ),
    ]
