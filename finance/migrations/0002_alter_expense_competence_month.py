# Generated by Django 5.1.7 on 2025-03-26 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='competence_month',
            field=models.DateField(help_text='Competence Sample (ie: 2025-03-01)'),
        ),
    ]
