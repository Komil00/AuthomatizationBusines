# Generated by Django 4.1.7 on 2023-03-03 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_zavoddanolganmahsulot_remove_tarqatish_ombor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahsulot',
            name='image',
            field=models.ImageField(default=1, upload_to='media/mahsulot/'),
            preserve_default=False,
        ),
    ]
