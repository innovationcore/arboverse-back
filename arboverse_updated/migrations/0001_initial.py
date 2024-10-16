# Generated by Django 5.1.2 on 2024-10-14 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Borning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borne_type', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FeedingPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Habitat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Landscape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VectorFamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VectorOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VirusFamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VirusGenus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VectorGenus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('family', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='arboverse_updated.vectorfamily')),
            ],
        ),
        migrations.AddField(
            model_name='vectorfamily',
            name='order',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='arboverse_updated.vectororder'),
        ),
        migrations.CreateModel(
            name='VectorSpecies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('arthropod_type', models.TextField(blank=True, null=True)),
                ('genome', models.BooleanField(blank=True, null=True)),
                ('reference_genome', models.TextField(blank=True, null=True)),
                ('genome_size', models.IntegerField(blank=True, null=True)),
                ('survival_temperature_ranges', models.TextField(blank=True, null=True)),
                ('survival_humidity_percent', models.TextField(blank=True, null=True)),
                ('distribution', models.TextField(blank=True, null=True)),
                ('adult_life_expectancy_days', models.TextField(blank=True, null=True)),
                ('anthropophilic_behaviour', models.BooleanField(blank=True, null=True)),
                ('eggs_viability_days', models.TextField(blank=True, null=True)),
                ('lifecycle_time_days', models.TextField(blank=True, null=True)),
                ('experimental_infection', models.TextField(blank=True, null=True)),
                ('blood_meal', models.ManyToManyField(to='arboverse_updated.bloodmeal')),
                ('feeding_period', models.ManyToManyField(to='arboverse_updated.feedingperiod')),
                ('genus', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='arboverse_updated.vectorgenus')),
                ('habitat', models.ManyToManyField(to='arboverse_updated.habitat')),
                ('landscape', models.ManyToManyField(to='arboverse_updated.landscape')),
                ('location', models.ManyToManyField(to='arboverse_updated.location')),
            ],
        ),
        migrations.CreateModel(
            name='VectorSubFamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('family', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='arboverse_updated.vectorfamily')),
            ],
        ),
        migrations.AddField(
            model_name='vectorgenus',
            name='sub_family',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='arboverse_updated.vectorsubfamily'),
        ),
        migrations.CreateModel(
            name='Virus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('specie', models.TextField(default='')),
                ('abbreviation', models.TextField(default='')),
                ('collection_date', models.TextField(default='')),
                ('genome_type', models.TextField(default='')),
                ('enveloped', models.BooleanField(blank=True, null=True)),
                ('reference_strain', models.TextField(default='')),
                ('genome_length_nt', models.IntegerField(blank=True, null=True)),
                ('host_amplifier', models.TextField(default='')),
                ('human_fatal_disease', models.BooleanField(blank=True, null=True)),
                ('veterinary_diseases', models.BooleanField(blank=True, null=True)),
                ('veterinary_fatal_diseases', models.BooleanField(blank=True, null=True)),
                ('no_cases', models.TextField(default='')),
                ('level_of_disease', models.TextField(default='')),
                ('vaccine', models.TextField(default='')),
                ('vero_cells', models.BooleanField(blank=True, null=True)),
                ('C6_36_cells', models.BooleanField(blank=True, null=True)),
                ('cpe_vero', models.TextField(default='')),
                ('plaques_vero', models.TextField(default='')),
                ('animal_model', models.TextField(default='')),
                ('sals_level', models.TextField(default='')),
                ('borning', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='arboverse_updated.borning')),
                ('country', models.ManyToManyField(to='arboverse_updated.country')),
                ('diseases', models.ManyToManyField(to='arboverse_updated.disease')),
                ('family', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='arboverse_updated.virusfamily')),
                ('genus', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='arboverse_updated.virusgenus')),
            ],
        ),
        migrations.CreateModel(
            name='VirusVector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_vector', models.BooleanField(blank=True, null=True)),
                ('vector', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='arboverse_updated.vectorspecies')),
                ('virus', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='arboverse_updated.virus')),
            ],
        ),
        migrations.AddField(
            model_name='vectorspecies',
            name='virus',
            field=models.ManyToManyField(related_name='virus', through='arboverse_updated.VirusVector', to='arboverse_updated.virus'),
        ),
    ]
