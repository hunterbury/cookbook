# Generated by Django 3.2.8 on 2021-11-08 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20211105_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]