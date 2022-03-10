from django.contrib import admin
from . models import *

# Register your models here.


admin.site.site_header = "U-Learn Data Visualization Administration"


@admin.register(OrgType)
class OrgTypeAdmin(admin.ModelAdmin):
    list_display = ('id','title','value')
    search_fields = ['id','title','value']


@admin.register(GeographicScope)
class GeographicScopeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'value')
    search_fields = ['id', 'title', 'value']


@admin.register(ThematicArea)
class ThematicAreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'value')
    search_fields = ['id', 'title', 'value']


@admin.register(Settlement)
class SettlementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'value')
    search_fields = ['id', 'title', 'value']


@admin.register(Dump)
class DumpAdmin(admin.ModelAdmin):
    list_display = ('id','org_code', 'organisation_name', 'website', 'org_type', 'geographic_scope', 'primary_technicalsector',
                  'secondary_technicalsector', 'third_technicalsector', 'fourth_technicalsector',
                  'fifth_technicalsector',
                  'eco_system_tag', 'eco_map_sector', 'eco_map_subsector','ulearn_subcategory',
                  'date_of_last_contact', 'primary_contact_name', 'phone', 'status_remarks', 'role', 'email',
                  'optional_contact', 'district', 'refugee_settlement', 'location_base')
    search_fields = ['org_code', 'organisation_name', 'website', 'org_type', 'geographic_scope', 'primary_technicalsector',
                  'secondary_technicalsector', 'third_technicalsector', 'fourth_technicalsector',
                  'fifth_technicalsector',
                  'eco_system_tag', 'eco_map_sector', 'eco_map_subsector',  'ulearn_subcategory',
                  'date_of_last_contact', 'primary_contact_name', 'phone', 'status_remarks', 'role', 'email',
                  'optional_contact', 'district', 'refugee_settlement', 'location_base']



@admin.register(CleanData)
class CleanDataAdmin(admin.ModelAdmin):
    list_display = ('id','org_code', 'organisation_name', 'website', 'org_type', 'geographic_scope', 'primary_technicalsector',
                  'secondary_technicalsector', 'third_technicalsector', 'fourth_technicalsector',
                  'fifth_technicalsector',
                  'eco_system_tag', 'eco_map_sector', 'eco_map_subsector', 'ulearn_subcategory',
                  'date_of_last_contact', 'primary_contact_name', 'phone', 'status_remarks', 'role', 'email',
                  'optional_contact', 'district', 'refugee_settlement', 'location_base')
    search_fields = ['org_code', 'organisation_name', 'website', 'org_type', 'geographic_scope', 'primary_technicalsector',
                  'secondary_technicalsector', 'third_technicalsector', 'fourth_technicalsector',
                  'fifth_technicalsector',
                  'eco_system_tag', 'eco_map_sector', 'eco_map_subsector',  'ulearn_subcategory',
                  'date_of_last_contact', 'primary_contact_name', 'phone', 'status_remarks', 'role', 'email',
                  'optional_contact', 'district', 'refugee_settlement', 'location_base']
