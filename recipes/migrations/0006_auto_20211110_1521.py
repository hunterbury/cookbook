# Generated by Django 3.2.8 on 2021-11-10 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20211110_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='cuisine',
        ),
        migrations.AddField(
            model_name='recipe',
            name='cuisine',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('Mexican', 'Mexican'), ('Asian', 'Asian'), ('American', 'American'), ('Indian', 'Indian')], default='None', max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Cuisine',
        ),
    ]
