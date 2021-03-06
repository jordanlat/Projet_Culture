# Generated by Django 4.0.3 on 2022-03-24 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appfilms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='film_acteurs',
            new_name='acteurs',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='film_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='film_date_ajout',
            new_name='date_ajout',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='film_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='film_liens',
            new_name='liens',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='film_moy_note',
            new_name='moy_note',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='film_par_qui',
            new_name='par_qui',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='film_platforme',
            new_name='platforme',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='film_resume',
            new_name='resume',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='film_statut',
            new_name='statut',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='film_titre',
            new_name='titre',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='film_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='statut',
            old_name='statut_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='statut',
            old_name='statut_label',
            new_name='label',
        ),
    ]
