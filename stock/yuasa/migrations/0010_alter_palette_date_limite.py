# Generated by Django 4.0.6 on 2022-07-27 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuasa', '0009_alter_palette_date_limite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palette',
            name='date_limite',
            field=models.DateTimeField(),
        ),
    ]