# Generated by Django 3.2.8 on 2022-01-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.URLField(blank=True, default='https://i0.wp.com/images-prod.healthline.com/hlcmsresource/images/AN_images/healthy-eating-ingredients-1296x728-header.jpg?w=1155&h=1528', null=True)),
                ('cuisine', models.CharField(blank=True, choices=[('Mexican', 'Mexican'), ('Asian', 'Asian'), ('American', 'American'), ('Indian', 'Indian')], default='None', max_length=20, null=True)),
                ('meal', models.CharField(blank=True, choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Snack', 'Snack')], default='None', max_length=20, null=True)),
                ('description', models.CharField(max_length=500)),
                ('prep_time', models.DurationField()),
                ('cook_time', models.DurationField()),
                ('servings', models.IntegerField()),
                ('ingredients', models.TextField(blank=True, null=True)),
                ('instructions', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
