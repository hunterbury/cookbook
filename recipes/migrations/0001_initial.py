# Generated by Django 3.2.8 on 2021-11-18 18:53

from django.db import migrations, models
import django.db.models.deletion


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
                ('image', models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/')),
                ('cuisine', models.CharField(blank=True, choices=[('None', 'None'), ('Mexican', 'Mexican'), ('Asian', 'Asian'), ('American', 'American'), ('Indian', 'Indian')], default='None', max_length=20, null=True)),
                ('meal', models.CharField(blank=True, choices=[('None', 'None'), ('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Snack', 'Snack')], default='None', max_length=20, null=True)),
                ('info', models.CharField(max_length=500)),
                ('prep_time', models.DurationField()),
                ('cook_time', models.DurationField()),
                ('servings', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction', models.CharField(blank=True, max_length=300, null=True)),
                ('recipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instructions', to='recipes.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('measurement', models.CharField(blank=True, choices=[('Oz', 'Oz'), ('Cup', 'Cup'), ('Tsp', 'Tsp'), ('Tbsp', 'Tbsp')], default='None', max_length=20, null=True)),
                ('recipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.recipe')),
            ],
        ),
    ]
