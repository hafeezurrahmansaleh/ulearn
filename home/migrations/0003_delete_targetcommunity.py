# Generated by Django 4.0.3 on 2023-03-06 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_landingpagecontent_orgdetailspagecontent_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TargetCommunity',
        ),
    ]