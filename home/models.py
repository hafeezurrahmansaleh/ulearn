# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models


# class User(AbstractUser):
#     is_admin = models.BooleanField(default=False)


class OrgType(models.Model):
    title = models.CharField(max_length=250, db_column='Title')
    value = models.CharField(max_length=250, db_column='Value')

    def __str__(self):
        return self.title


class OrgLegalType(models.Model):
    title = models.CharField(max_length=250, db_column='Title')
    value = models.CharField(max_length=250, db_column='Value')

    def __str__(self):
        return self.title


class GeographicScope(models.Model):
    title = models.CharField(max_length=250, db_column='Title')
    value = models.CharField(max_length=250, db_column='Value')

    def __str__(self):
        return self.title


class ThematicArea(models.Model):
    title = models.CharField(max_length=250, db_column='Title')
    value = models.CharField(max_length=250, db_column='Value')

    def __str__(self):
        return self.title


class Settlement(models.Model):
    title = models.CharField(max_length=250, db_column='Title')
    value = models.CharField(max_length=250, db_column='Value')

    def __str__(self):
        return self.title


class TargetDemographic(models.Model):
    title = models.CharField(max_length=250, db_column='Title')
    value = models.CharField(max_length=250, db_column='Value')

    def __str__(self):
        return self.title


class Dump(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    org_code = models.CharField(max_length=250, db_column='ORG_CODE', null=True,
                                blank=True)  # Field name made lowercase.
    org_name = models.TextField(max_length=1000, null=True, blank=True)  # Field name made lowercase.
    org_acronym = models.TextField(max_length=1000, null=True, blank=True)  # Field name made lowercase.
    founding_year = models.CharField(max_length=5, null=True, blank=True)  # Field name made lowercase.
    years_active = models.CharField(max_length=5, null=True, blank=True)  # Field name made lowercase.
    org_type = models.ForeignKey(OrgType, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='org_type')  # Field name made lowercase.
    org_legaltype = models.ForeignKey(OrgLegalType, on_delete=models.CASCADE, null=True, blank=True,
                                      related_name='org_legaltype')  # Field name made lowercase.
    refugee_settlement = models.ForeignKey(Settlement, on_delete=models.CASCADE, null=True, blank=True,
                                           related_name='settlement')
    refugee_zone = models.CharField(max_length=250, null=True,
                                    blank=True)  # Field name made lowercase.
    org_offices = models.TextField(max_length=1000, null=True, blank=True)  # Field name made lowercase.
    # website = models.CharField(max_length = 250, null=True, blank=True)  # Field name made lowercase.
    #
    # geographic_scope = models.ForeignKey(GeographicScope, on_delete=models.CASCADE, null=True, blank=True, related_name='geographic_scope')  # Field name made lowercase.
    org_primarytechnicalarea = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True,
                                                 related_name='primary_thematic_area')  # Field name made lowercase.
    org_activities = models.TextField(max_length=1500, null=True, blank=True)  # Field name made lowercase.
    org_secondarytechnicalarea1 = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True,
                                                    related_name='secondary_thematic_area')  # Field name made lowercase.
    org_secondarytechnicalarea2 = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True,
                                                    related_name='third_thematic_area')  # Field name made lowercase.

    # fourth_technicalsector = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True, related_name='fourth_thematic_area')  # Field name made lowercase.
    # fifth_technicalsector = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True, related_name='fifth_thematic_area')  # Field name made lowercase.
    org_targetgroup = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    org_targetdemographic = models.ForeignKey(TargetDemographic, on_delete=models.CASCADE, null=True, blank=True,
                                              related_name='org_targetdemographic')
    org_primarycontact = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    org_email = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    org_phone = models.CharField(max_length=50, null=True, blank=True)  # Field name made lowercase.
    org_website = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    org_facebook = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    org_twitter = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    org_logo = models.TextField(max_length=1250, null=True, blank=True)  # Field name made lowercase.
    contact_name = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    contact_role = models.CharField(max_length=150, null=True, blank=True)  # Field name made lowercase.
    contact_email = models.CharField(max_length=150, null=True, blank=True)  # Field name made lowercase.
    contact_phone = models.CharField(max_length=50, null=True, blank=True)  # Field name made lowercase.

    # class Meta:
    #     managed = True
    #     # db_table = 'dump'

    def __str__(self):
        return self.org_name


class CleanData(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # org_code = models.CharField(max_length=250, db_column='ORG_CODE', null=True,
    #                             blank=True)  # Field name made lowercase.
    org_name = models.TextField(max_length=1000, null=True, blank=True)  # Field name made lowercase.
    org_acronym = models.TextField(max_length=1000, null=True, blank=True)  # Field name made lowercase.
    founding_year = models.CharField(max_length=5, null=True, blank=True)  # Field name made lowercase.
    years_active = models.CharField(max_length=5, null=True, blank=True)  # Field name made lowercase.
    org_type = models.ForeignKey(OrgType, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='cd_org_type')  # Field name made lowercase.
    org_legaltype = models.ForeignKey(OrgLegalType, on_delete=models.CASCADE, null=True, blank=True,
                                      related_name='cd_org_legaltype')  # Field name made lowercase.
    refugee_settlement = models.ForeignKey(Settlement, on_delete=models.CASCADE, null=True, blank=True,
                                           related_name='cd_settlement')
    refugee_zone = models.CharField(max_length=250, null=True,
                                    blank=True)  # Field name made lowercase.
    org_offices = models.TextField(max_length=1000, null=True, blank=True)  # Field name made lowercase.
    # website = models.CharField(max_length = 250, null=True, blank=True)  # Field name made lowercase.
    #
    # geographic_scope = models.ForeignKey(GeographicScope, on_delete=models.CASCADE, null=True, blank=True, related_name='geographic_scope')  # Field name made lowercase.
    org_primarytechnicalarea = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True,
                                                 related_name='cd_primary_thematic_area')  # Field name made lowercase.
    org_activities = models.TextField(max_length=1500, null=True, blank=True)  # Field name made lowercase.
    org_secondarytechnicalarea1 = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True,
                                                    related_name='cd_secondary_thematic_area')  # Field name made lowercase.
    org_secondarytechnicalarea2 = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True,
                                                    related_name='cd_third_thematic_area')  # Field name made lowercase.

    # fourth_technicalsector = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True, related_name='fourth_thematic_area')  # Field name made lowercase.
    # fifth_technicalsector = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, null=True, blank=True, related_name='fifth_thematic_area')  # Field name made lowercase.
    org_targetgroup = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    org_targetdemographic = models.ForeignKey(TargetDemographic, on_delete=models.CASCADE, null=True, blank=True,
                                              related_name='cd_org_targetdemographic')
    org_primarycontact = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    org_email = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    org_phone = models.CharField(max_length=50, null=True, blank=True)  # Field name made lowercase.
    org_website = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    org_facebook = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    org_twitter = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    org_logo = models.TextField(max_length=1250, null=True, blank=True)  # Field name made lowercase.
    contact_name = models.CharField(max_length=250, null=True, blank=True)  # Field name made lowercase.
    contact_role = models.CharField(max_length=150, null=True, blank=True)  # Field name made lowercase.
    contact_email = models.CharField(max_length=150, null=True, blank=True)  # Field name made lowercase.
    contact_phone = models.CharField(max_length=50, null=True, blank=True)  # Field name made lowercase.

    # class Meta:
    #     managed = True
    #     # db_table = 'dump'

    def __str__(self):
        return self.org_name


# org_name
# org_acronym
# founding_year
# years_active
# org_type
# org_legaltype
# refugee_settlement
# refugee_zone
# org_offices
# org_primarytechnicalarea
# org_activities
# org_secondarytechnicalarea1
# org_secondarytechnicalarea2
# org_targetgroup
# org_targetdemographic
# org_primarycontact
# org_email
# org_phone
# org_website
# org_facebook
# org_twitter
# org_logo
# contact_name
# contact_role
# contact_email
# contact_phone
