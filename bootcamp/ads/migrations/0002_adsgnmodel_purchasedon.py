# Generated by Django 3.2.3 on 2021-05-26 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adsgnmodel',
            name='purchasedOn',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]