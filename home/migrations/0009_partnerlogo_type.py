# Generated by Django 4.0.3 on 2023-03-06 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_partnerlogo_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnerlogo',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='partner_type', to='home.partnertype'),
            preserve_default=False,
        ),
    ]
