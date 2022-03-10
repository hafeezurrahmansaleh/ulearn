# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import User
from django.db import models

class OrgType(models.Model):
    title = models.CharField(max_length = 250,db_column='Title')
    value = models.CharField(max_length = 250,db_column='Value')

    def __str__(self):
        return self.title


class GeographicScope(models.Model):
    title = models.CharField(max_length = 250,db_column='Title')
    value = models.CharField(max_length = 250,db_column='Value')

    def __str__(self):
        return self.title


class ThematicArea(models.Model):
    title = models.CharField(max_length = 250,db_column='Title')
    value = models.CharField(max_length = 250,db_column='Value')

    def __str__(self):
        return self.title


class Settlement(models.Model):
    title = models.CharField(max_length = 250,db_column='Title')
    value = models.CharField(max_length = 250,db_column='Value')

    def __str__(self):
        return self.title



class Dump(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    org_code = models.CharField(max_length = 250,db_column='ORG_CODE', null=True, blank=True)  # Field name made lowercase.
    organisation_name = models.TextField(max_length = 1000, null=True, blank=True)  # Field name made lowercase.
    organisation_name2 = models.TextField(max_length = 1000, null=True, blank=True)  # Field name made lowercase.
    functionality = models.CharField(max_length = 250,null=True, blank=True)  # Field name made lowercase.
    website = models.CharField(max_length = 250, null=True, blank=True)  # Field name made lowercase.
    org_type = models.ForeignKey(OrgType, on_delete=models.CASCADE, null=True, blank=True, related_name='org_type')  # Field name made lowercase.
    geographic_scope = models.ForeignKey(GeographicScope, on_delete=models.CASCADE, null=True, blank=True, related_name='geographic_scope')  # Field name made lowercase.
    primary_technicalsector = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True, related_name='primary_thematic_area')  # Field name made lowercase.
    secondary_technicalsector = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True, related_name='secondary_thematic_area')  # Field name made lowercase.
    third_technicalsector= models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True, related_name='third_thematic_area')  # Field name made lowercase.
    fourth_technicalsector = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True, related_name='fourth_thematic_area')  # Field name made lowercase.
    fifth_technicalsector = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True, related_name='fifth_thematic_area')  # Field name made lowercase.
    eco_system_tag = models.CharField(max_length = 250, null=True, blank=True)  # Field name made lowercase.
    eco_map_sector = models.CharField(max_length = 250, null=True, blank=True)  # Field name made lowercase.
    eco_map_subsector = models.CharField(max_length = 250, null=True, blank=True)  # Field name made lowercase.
    number_of_convener = models.IntegerField( null=True, blank=True)  # Field name made lowercase.
    number_of_challenges = models.IntegerField( null=True, blank=True)  # Field name made lowercase.
    number_of_innovations = models.IntegerField( null=True, blank=True)  # Field name made lowercase.
    number_of_referrals = models.IntegerField( null=True, blank=True)  # Field name made lowercase.
    number_of_matchmaker = models.IntegerField( null=True, blank=True)  # Field name made lowercase.
    number_of_matchmaker_solution_received = models.IntegerField( null=True, blank=True)  # Field name made lowercase.
    number_of_projects_ril = models.IntegerField( null=True, blank=True)  # Field name made lowercase.
    total_number_of_interactions_ril = models.IntegerField( null=True, blank=True)  # Field name made lowercase.
    ulearn_subcategory = models.CharField(max_length = 250,null=True, blank=True)  # Field name made lowercase.
    date_of_last_contact = models.DateField( null=True, blank=True)  # Field name made lowercase.
    status_remarks = models.CharField(max_length = 250,null=True, blank=True)  # Field name made lowercase.
    primary_contact_name = models.CharField(max_length = 250, null=True, blank=True)  # Field name made lowercase.
    role = models.CharField(max_length = 250)  # Field name made lowercase.
    email = models.CharField(max_length = 250)  # Field name made lowercase.
    phone = models.CharField(max_length = 250)  # Field name made lowercase.
    optional_contact = models.CharField(max_length = 250, null=True, blank=True)  # Field name made lowercase.
    location_base = models.CharField(max_length = 250, null=True, blank=True)  # Field name made lowercase.
    district = models.CharField(max_length = 250, null=True, blank=True)  # Field name made lowercase.
    refugee_settlement = models.ForeignKey(Settlement, on_delete=models.CASCADE, null=True, blank=True,
                                           related_name='settlement')
    refugee_settlement_collected_from = models.CharField(max_length=250, null=True,
                                                         blank=True)  # Field name made lowercase.

    # class Meta:
    #     managed = True
    #     # db_table = 'dump'

    def __str__(self):
        return self.organisation_name




class CleanData(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    org_code = models.CharField(max_length=250, db_column='ORG_CODE', null=True,
                                blank=True)  # Field name made lowercase.
    organisation_name = models.TextField(max_length=1000, null=True, blank=True)  # Field name made lowercase.
    organisation_name2 = models.TextField(max_length=1000, null=True, blank=True)  # Field name made lowercase.
    functionality = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    website = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    org_type = models.ForeignKey(OrgType, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='cd_org_type')  # Field name made lowercase.
    geographic_scope = models.ForeignKey(GeographicScope, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='cd_geographic_scope')  # Field name made lowercase.
    primary_technicalsector = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True,
                                                related_name='cd_primary_thematic_area')  # Field name made lowercase.
    secondary_technicalsector = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True,
                                                  related_name='cd_secondary_thematic_area')  # Field name made lowercase.
    third_technicalsector = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True,
                                              related_name='cd_third_thematic_area')  # Field name made lowercase.
    fourth_technicalsector = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True,
                                               related_name='cd_fourth_thematic_area')  # Field name made lowercase.
    fifth_technicalsector = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True,
                                              related_name='cd_fifth_thematic_area')  # Field name made lowercase.
    eco_system_tag = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    eco_map_sector = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    eco_map_subsector = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.

    total_number_of_interactions_ril = models.IntegerField(null=True, blank=True)  # Field name made lowercase.
    ulearn_subcategory = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    date_of_last_contact = models.DateField(null=True, blank=True)  # Field name made lowercase.
    status_remarks = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    primary_contact_name = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    role = models.CharField(max_length=250)  # Field name made lowercase.
    email = models.CharField(max_length=250)  # Field name made lowercase.
    phone = models.CharField(max_length=250)  # Field name made lowercase.
    optional_contact = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    location_base = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    district = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    refugee_settlement = models.ForeignKey(Settlement, on_delete=models.CASCADE, null=True, blank=True,
                                               related_name='cd_settlement')
    refugee_settlement_collected_from = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.

    # class Meta:
    #     managed = True
    #     db_table = 'dump'

    def __str__(self):
        return self.organisation_name


