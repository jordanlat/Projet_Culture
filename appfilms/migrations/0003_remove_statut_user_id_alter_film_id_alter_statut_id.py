# Generated by Django 4.0.3 on 2022-03-29 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfilms', '0002_rename_film_acteurs_film_acteurs_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statut',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='film',
            name='id',
            field=models.DecimalField(auto_created=True, decimal_places=1, max_digits=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='statut',
            name='id',
            field=models.DecimalField(auto_created=True, decimal_places=1, max_digits=5, primary_key=True, serialize=False),
        ),
    ]
