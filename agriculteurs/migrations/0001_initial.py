# Generated by Django 5.0.3 on 2024-03-23 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agriculteurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_agriculteur', models.CharField(max_length=15)),
                ('prenom_agriculteur', models.CharField(max_length=15)),
                ('borne', models.IntegerField()),
                ('solde_en_dt', models.FloatField(default=0.0)),
                ('nbre_des_versements', models.IntegerField(default=0)),
            ],
        ),
    ]
