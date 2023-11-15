# Generated by Django 4.2.6 on 2023-11-15 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0016_alter_band_year_formed'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.CharField(default='description indisponible', max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='sold',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('CL', 'Clothing'), ('PS', 'Posters'), ('MI', 'Miscellaneous')], default='pas de type specifié', max_length=5),
        ),
    ]