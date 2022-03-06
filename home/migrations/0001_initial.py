# Generated by Django 4.0.3 on 2022-03-03 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GeographicScope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='Title', max_length=250)),
                ('value', models.CharField(db_column='Value', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='OrgType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='Title', max_length=250)),
                ('value', models.CharField(db_column='Value', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Settlement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='Title', max_length=250)),
                ('value', models.CharField(db_column='Value', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ThematicArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='Title', max_length=250)),
                ('value', models.CharField(db_column='Value', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Dump',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_code', models.CharField(blank=True, db_column='ORG_CODE', max_length=250, null=True)),
                ('organisation_name', models.CharField(blank=True, max_length=250, null=True)),
                ('functionality', models.CharField(blank=True, max_length=250, null=True)),
                ('website', models.CharField(blank=True, max_length=250, null=True)),
                ('eco_system_tag', models.CharField(blank=True, max_length=250, null=True)),
                ('eco_map_sector', models.CharField(blank=True, max_length=250, null=True)),
                ('eco_map_subsector', models.CharField(blank=True, max_length=250, null=True)),
                ('number_of_convener', models.IntegerField(blank=True, null=True)),
                ('number_of_challenges', models.IntegerField(blank=True, null=True)),
                ('number_of_innovations', models.IntegerField(blank=True, null=True)),
                ('number_of_referrals', models.IntegerField(blank=True, null=True)),
                ('number_of_matchmaker', models.IntegerField(blank=True, null=True)),
                ('number_of_matchmaker_solution_received', models.IntegerField(blank=True, null=True)),
                ('number_of_projects_ril', models.IntegerField(blank=True, null=True)),
                ('total_number_of_interactions_ril', models.IntegerField(blank=True, null=True)),
                ('ulearn_subcategory', models.CharField(blank=True, max_length=250, null=True)),
                ('date_of_last_contact', models.DateField(blank=True, null=True)),
                ('status_remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('primary_contact_name', models.CharField(blank=True, max_length=250, null=True)),
                ('role', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('optional_contact', models.CharField(blank=True, max_length=250, null=True)),
                ('location_base', models.CharField(blank=True, max_length=250, null=True)),
                ('district', models.CharField(blank=True, max_length=250, null=True)),
                ('refugee_settlement_collected_from', models.CharField(blank=True, max_length=250, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fifth_technicalsector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fifth_thematic_area', to='home.thematicarea')),
                ('fourth_technicalsector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fourth_thematic_area', to='home.thematicarea')),
                ('geographic_scope', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geographic_scope', to='home.geographicscope')),
                ('org_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_type', to='home.orgtype')),
                ('primary_technicalsector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_thematic_area', to='home.thematicarea')),
                ('refugee_settlement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='settlement', to='home.settlement')),
                ('secondary_technicalsector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_thematic_area', to='home.thematicarea')),
                ('third_technicalsector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third_thematic_area', to='home.thematicarea')),
            ],
        ),
        migrations.CreateModel(
            name='CleanData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_code', models.CharField(blank=True, db_column='ORG_CODE', max_length=250, null=True)),
                ('organisation_name', models.CharField(blank=True, max_length=250, null=True)),
                ('organisation_name2', models.CharField(blank=True, max_length=250, null=True)),
                ('functionality', models.CharField(blank=True, max_length=250, null=True)),
                ('website', models.CharField(blank=True, max_length=250, null=True)),
                ('eco_system_tag', models.CharField(blank=True, max_length=250, null=True)),
                ('eco_map_sector', models.CharField(blank=True, max_length=250, null=True)),
                ('eco_map_subsector', models.CharField(blank=True, max_length=250, null=True)),
                ('total_number_of_interactions_ril', models.IntegerField(blank=True, null=True)),
                ('ulearn_subcategory', models.CharField(blank=True, max_length=250, null=True)),
                ('date_of_last_contact', models.DateField(blank=True, null=True)),
                ('status_remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('primary_contact_name', models.CharField(blank=True, max_length=250, null=True)),
                ('role', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('optional_contact', models.CharField(blank=True, max_length=250, null=True)),
                ('location_base', models.CharField(blank=True, max_length=250, null=True)),
                ('district', models.CharField(blank=True, max_length=250, null=True)),
                ('refugee_settlement_collected_from', models.CharField(blank=True, max_length=250, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fifth_technicalsector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cd_fifth_thematic_area', to='home.thematicarea')),
                ('fourth_technicalsector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cd_fourth_thematic_area', to='home.thematicarea')),
                ('geographic_scope', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cd_geographic_scope', to='home.geographicscope')),
                ('org_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cd_org_type', to='home.orgtype')),
                ('primary_technicalsector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cd_primary_thematic_area', to='home.thematicarea')),
                ('refugee_settlement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cd_settlement', to='home.settlement')),
                ('secondary_technicalsector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cd_secondary_thematic_area', to='home.thematicarea')),
                ('third_technicalsector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cd_third_thematic_area', to='home.thematicarea')),
            ],
        ),
    ]
