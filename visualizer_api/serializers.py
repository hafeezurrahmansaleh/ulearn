from rest_framework import serializers
from home.models import *


class ThematicAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThematicArea
        fields = '__all__'


class OrgTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgType
        fields = '__all__'


class GeographicScopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeographicScope
        fields = '__all__'


class DumpDataSerializer(serializers.ModelSerializer):
    # cover_image = Base64ImageField(required=True)
    org_type = serializers.CharField(
        source="org_type.value",
        read_only=True
    )
    geographic_scope = serializers.CharField(
        source="geographic_scope.value",
        read_only=True
    )
    primary_technicalsector = serializers.CharField(
        source="primary_technicalsector.value",
        read_only=True
    )
    secondary_technicalsector = serializers.CharField(
        source="secondary_technicalsector.value",
        read_only=True
    )
    third_technicalsector = serializers.CharField(
        source="third_technicalsector.value",
        read_only=True
    )
    fourth_technicalsector = serializers.CharField(
        source="fourth_technicalsector.value",
        read_only=True
    )
    fifth_technicalsector = serializers.CharField(
        source="fifth_technicalsector.value",
        read_only=True
    )
    refugee_settlement = serializers.CharField(
            source="refugee_settlement.value",
            read_only=True
        )


    class Meta:
        model = Dump
        fields = (
            "id",
            "org_type",
            "geographic_scope",
            "org_code",
            "organisation_name",
            "functionality",
            "website",
            "eco_system_tag",
            "eco_map_sector",
            "eco_map_subsector",
            "total_number_of_interactions_ril",
            "ulearn_subcategory",
            "date_of_last_contact",
            "status_remarks",
            "primary_contact_name",
            "role",
            "email",
            "phone",
            "optional_contact",
            "location_base",
            "district",
            "refugee_settlement",
            "primary_technicalsector",
            "secondary_technicalsector",
            "third_technicalsector",
            "fourth_technicalsector",
            "fifth_technicalsector"
        )
        # fields = '__all__'
        read_only_fields = (
            'id',
            'publisher',
            'created',
            'updated'
        )
