# Generated by Django 4.0.6 on 2022-07-27 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Palette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=20)),
                ('date_code', models.CharField(max_length=20)),
                ('prodDate_or_rechDate', models.DateTimeField()),
                ('quantity', models.IntegerField()),
                ('type', models.CharField(choices=[('Industrielle', 'Indus'), ('Auto standard', 'Auto'), ('Auto AGM', 'Auto Agm'), ('Moto Wet', 'Moto Wet')], max_length=20)),
            ],
        ),
    ]
