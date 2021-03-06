# Generated by Django 4.0.3 on 2022-05-16 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_cleandata_associated_settlements_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cleandata',
            options={'ordering': ('org_name',)},
        ),
        migrations.AlterModelOptions(
            name='dump',
            options={'ordering': ('org_name',)},
        ),
        migrations.AlterModelOptions(
            name='geographicscope',
            options={'ordering': ('value',)},
        ),
        migrations.AlterModelOptions(
            name='orglegaltype',
            options={'ordering': ('value',)},
        ),
        migrations.AlterModelOptions(
            name='orgtype',
            options={'ordering': ('value',)},
        ),
        migrations.AlterModelOptions(
            name='settlement',
            options={'ordering': ('value',)},
        ),
        migrations.AlterModelOptions(
            name='targetdemographic',
            options={'ordering': ('value',)},
        ),
        migrations.AlterModelOptions(
            name='thematicarea',
            options={'ordering': ('value',)},
        ),
    ]
