# Generated by Django 4.0.6 on 2022-07-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuasa', '0003_alter_palette_proddate_or_rechdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='palette',
            name='voltage',
            field=models.FloatField(default=12.0),
        ),
        migrations.AlterField(
            model_name='palette',
            name='prodDate_or_rechDate',
            field=models.DateField(),
        ),
    ]