# Generated by Django 3.2.8 on 2021-11-10 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20211110_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine', models.CharField(blank=True, choices=[('None', 'None'), ('Mexican', 'Mexican'), ('Asian', 'Asian'), ('American', 'American'), ('Indian', 'Indian')], default='None', max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='cuisine',
        ),
        migrations.AddField(
            model_name='recipe',
            name='cuisine',
            field=models.ManyToManyField(to='recipes.Cuisine'),
        ),
    ]
