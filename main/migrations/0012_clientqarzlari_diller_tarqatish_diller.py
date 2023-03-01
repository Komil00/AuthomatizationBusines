# Generated by Django 4.1.7 on 2023-03-01 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0011_zavoddanolganmahsulot_diller'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientqarzlari',
            name='diller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='diller_clientqarzlari', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarqatish',
            name='diller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='diller_tarqatish', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
