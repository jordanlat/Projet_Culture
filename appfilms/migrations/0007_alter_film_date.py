# Generated by Django 4.0.3 on 2022-03-29 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfilms', '0006_film_acteurs_film_date_film_date_ajout_film_liens_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='date',
            field=models.IntegerField(null=True),
        ),
    ]
