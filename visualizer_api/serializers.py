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


# class GeographicScopeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GeographicScope
#         fields = '__all__'


class CleanDataSerializer(serializers.ModelSerializer):
    # cover_image = Base64ImageField(required=True)
    org_type = serializers.CharField(
        source="org_type.value",
        read_only=True
    )
    # geographic_scope = serializers.CharField(
    #     source="geographic_scope.value",
    #     read_only=True
    # )
    org_primarytechnicalarea = serializers.CharField(
        source="org_secondarytechnicalarea1.value",
        read_only=True
    )
    org_secondarytechnicalarea1 = serializers.CharField(
        source="org_secondarytechnicalarea1.value",
        read_only=True
    )
    org_secondarytechnicalarea2 = serializers.CharField(
        source="org_secondarytechnicalarea2.value",
        read_only=True
    )

    refugee_settlement = serializers.CharField(
            source="refugee_settlement.value",
            read_only=True
        )
    org_targetdemographic = serializers.CharField(
                source="org_targetdemographic.value",
                read_only=True
            )


    class Meta:
        model = CleanData
        fields = (
            "id",
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
            "contact_phone",
        )
        # fields = '__all__'
        read_only_fields = (
            'id',
            'publisher',
            'created',
            'updated'
        )


# data = {
#     "settlement": ['Adjumani','BidiBi'],
#     "type_of_org":['LNGO','Private Sector'],
#     ...............
#     ...............
# }
