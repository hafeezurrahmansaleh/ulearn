# Generated by Django 4.0.3 on 2022-05-29 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_rename_num_of_staffs_dump_total_num_of_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dump',
            name='created_by',
        ),
    ]
