# Generated by Django 3.0.8 on 2020-07-22 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type_1', models.CharField(max_length=100)),
                ('type_2', models.CharField(blank=True, max_length=100)),
                ('total', models.DecimalField(max_digits=10, decimal_places=3)),
                ('hp', models.DecimalField(max_digits=10, decimal_places=3)),
                ('attack', models.DecimalField(max_digits=10, decimal_places=3)),
                ('defense', models.DecimalField(max_digits=10, decimal_places=3)),
                ('sp_atk', models.DecimalField(max_digits=10, decimal_places=3)),
                ('sp_def', models.DecimalField(max_digits=10, decimal_places=3)),
                ('speed', models.DecimalField(max_digits=10, decimal_places=3)),
                ('generation', models.DecimalField(max_digits=10, decimal_places=3)),
                ('legendary', models.BooleanField()),
            ],
        ),
    ]
