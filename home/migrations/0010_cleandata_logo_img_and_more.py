# Generated by Django 4.0.3 on 2022-05-08 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_cleandata_uuid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cleandata',
            name='logo_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='landingpagecontent',
            name='description1_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='orgtype',
            name='exclude_from_filter',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='targetdemographic',
            name='exclude_from_filter',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='thematicarea',
            name='exclude_from_filter',
            field=models.BooleanField(default=True),
        ),
    ]
