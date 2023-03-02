# Generated by Django 4.0.3 on 2022-03-31 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_orglegaltype_alter_cleandata_org_legaltype_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(blank=True, max_length=250, null=True)),
                ('description1', models.TextField(blank=True, max_length=2050, null=True)),
                ('title2', models.CharField(blank=True, max_length=250, null=True)),
                ('description2', models.TextField(blank=True, max_length=2050, null=True)),
                ('disclaimer', models.TextField(blank=True, max_length=2050, null=True)),
                ('access_form_url', models.CharField(blank=True, max_length=250, null=True)),
                ('banner_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('future_use1', models.CharField(blank=True, max_length=250, null=True)),
                ('future_use2', models.CharField(blank=True, max_length=250, null=True)),
                ('future_use3', models.TextField(blank=True, max_length=2050, null=True)),
            ],
        ),
    ]
