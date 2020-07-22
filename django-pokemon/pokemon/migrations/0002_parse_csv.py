from django.db import migrations
from django.apps import apps as django_apps
import os
import csv

def load_data_fromCsv(apps, schema_editor):
    Pokemon = apps.get_model("pokemon", "Pokemon")  

    path = django_apps.get_app_config("pokemon").path
    filepath = os.path.join(path, "Data", "pokemon.csv")

    def change_dict_key(key: str):
        key = key.lower()
        key = key.replace(" ", "_")
        key = key.replace(".", "")
        return key
    
    with open(filepath, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for dict_row in csv_reader:
            # Pop "# key from dict"
            dict_row.pop("#", None)
            # Edit dictionary keys to fit data model
            dict_row = { change_dict_key(k): v for k, v in dict_row.items()}

            p=Pokemon(**dict_row)

            # TODO: before save, apply changes


            p.save()       


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data_fromCsv),
    ]
