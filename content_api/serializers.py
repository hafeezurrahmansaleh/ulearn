from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from home.models import *
from visualizer_api.serializers import SettlementOrgAssociationSerializer
from drf_extra_fields.fields import Base64ImageField

class ThematicAreaContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThematicArea
        fields = '__all__'


class OrgTypeContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgType
        fields = '__all__'


class SettlementContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settlement
        fields = '__all__'


class TargetDemographicContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetDemographic
        fields = '__all__'


class SettlementOrgAssociationContentSerializer(serializers.ModelSerializer):
    settlement = serializers.CharField(
        source="settlement.value",
        read_only=True
    )
    primary_thematic_area = serializers.StringRelatedField(many=True)

    class Meta:
        model = SettlementOrgAssociation
        fields = ('settlement',
                  'primary_thematic_area',
                  'zones',
                  'operation_offices',
                  'num_of_staffs',
                  )


class LandingPageContentDetailsSerializer(serializers.ModelSerializer):
    banner_image = serializers.SerializerMethodField()

    class Meta:
        model = LandingPageContent
        fields = '__all__'


class PartnerTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartnerType
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartnerLogo
        fields = '__all__'


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingPageContent
        fields = ('first_name',
                  'username',
                  'email',
                  'phone',
                  'is_stuff',
                  'is_superuser',
                  'password',
                  )


class SettlementOrgAssociationCreateSerializer(serializers.ModelSerializer):
    settlement = serializers.SlugRelatedField(
        many=False,
        slug_field='value',
        queryset=Settlement.objects.all()
    )
    primary_thematic_area = serializers.SlugRelatedField(
        many=True,
        slug_field='value',
        required=False,
        queryset=ThematicArea.objects.all()
    )

    class Meta:
        model = SettlementOrgAssociation
        fields = ('settlement',
                  'primary_thematic_area',
                  'zones',
                  'operation_offices',
                  'num_of_staffs',
                  )


class DataEntrySerializer(WritableNestedModelSerializer):
    org_settlement = SettlementOrgAssociationCreateSerializer(many=True,required=False)
    # theme = ThematicTagSerializer(many=True)
    # attending_organization = OrganizationSerializer(many=True)
    org_type = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field='value',
        required=False,
        queryset=OrgType.objects.all()
    )
    org_targetdemographic = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        slug_field='value',
        required=False,
        queryset=TargetDemographic.objects.all()
    )
    logo_img = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = CleanData
        fields = '__all__'
        extra_kwargs = {
            'org_settlement': {'required': False, 'read_only': False, 'many': True,
                               'queryset': SettlementOrgAssociation.objects.all()},
        }
