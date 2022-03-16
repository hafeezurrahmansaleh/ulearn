from django.contrib import admin
from . models import *

# Register your models here.


admin.site.site_header = "U-Learn Data Visualization Administration"


@admin.register(OrgType)
class OrgTypeAdmin(admin.ModelAdmin):
    list_display = ('id','title','value')
    search_fields = ['id','title','value']


@admin.register(OrgLegalType)
class OrgLegalTypeAdmin(admin.ModelAdmin):
    list_display = ('id','title','value')
    search_fields = ['id','title','value']


# @admin.register(GeographicScope)
# class GeographicScopeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'value')
#     search_fields = ['id', 'title', 'value']


@admin.register(ThematicArea)
class ThematicAreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'value')
    search_fields = ['id', 'title', 'value']


@admin.register(Settlement)
class SettlementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'value')
    search_fields = ['id', 'title', 'value']


@admin.register(TargetDemographic)
class TargetDemographicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'value')
    search_fields = ['id', 'title', 'value']


@admin.register(Dump)
class DumpAdmin(admin.ModelAdmin):
    list_display = ("id",
            # "org_code",
            "org_name",
            "org_acronym",
            "founding_year",
            "years_active",
            "org_type",
            "org_legaltype",
            "refugee_settlement",
            "refugee_zone",
            "org_offices",
            "org_primarytechnicalarea",
            "org_activities",
            "org_secondarytechnicalarea1",
            "org_secondarytechnicalarea2",
            "org_targetgroup",
            "org_targetdemographic",
            "org_primarycontact",
            "org_email",
            "org_phone",
            "org_website",
            "org_facebook",
            "org_twitter",
            "org_logo",
            "contact_name",
            "contact_role",
            "contact_email",
            "contact_phone",)
    search_fields = ["id",
            # "org_code",
            "org_name",
            "org_acronym",
            "founding_year",
            "years_active",
            "org_type",
            "org_legaltype",
            "refugee_settlement",
            "refugee_zone",
            "org_offices",
            "org_primarytechnicalarea",
            "org_activities",
            "org_secondarytechnicalarea1",
            "org_secondarytechnicalarea2",
            "org_targetgroup",
            "org_targetdemographic",
            "org_primarycontact",
            "org_email",
            "org_phone",
            "org_website",
            "org_facebook",
            "org_twitter",
            "org_logo",
            "contact_name",
            "contact_role",
            "contact_email",
            "contact_phone",]



@admin.register(CleanData)
class CleanDataAdmin(admin.ModelAdmin):
    list_display = ("id",
            # "org_code",
            "org_name",
            "org_acronym",
            "founding_year",
            "years_active",
            "org_type",
            "org_legaltype",
            "refugee_settlement",
            "refugee_zone",
            "org_offices",
            "org_primarytechnicalarea",
            "org_activities",
            "org_secondarytechnicalarea1",
            "org_secondarytechnicalarea2",
            "org_targetgroup",
            "org_targetdemographic",
            "org_primarycontact",
            "org_email",
            "org_phone",
            "org_website",
            "org_facebook",
            "org_twitter",
            "org_logo",
            "contact_name",
            "contact_role",
            "contact_email",
            "contact_phone",)
    search_fields = ["id",
            # "org_code",
            "org_name",
            "org_acronym",
            "founding_year",
            "years_active",
            "org_type",
            "org_legaltype",
            "refugee_settlement",
            "refugee_zone",
            "org_offices",
            "org_primarytechnicalarea",
            "org_activities",
            "org_secondarytechnicalarea1",
            "org_secondarytechnicalarea2",
            "org_targetgroup",
            "org_targetdemographic",
            "org_primarycontact",
            "org_email",
            "org_phone",
            "org_website",
            "org_facebook",
            "org_twitter",
            "org_logo",
            "contact_name",
            "contact_role",
            "contact_email",
            "contact_phone",]
