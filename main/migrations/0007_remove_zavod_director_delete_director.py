# Generated by Django 4.1.7 on 2023-03-01 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_director_diller_alter_zavod_diller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zavod',
            name='director',
        ),
        migrations.DeleteModel(
            name='Director',
        ),
    ]
