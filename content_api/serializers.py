from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from home.models import *
from visualizer_api.serializers import SettlementOrgAssociationSerializer


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
    settlement = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Settlement.objects.all()
    )
    primary_thematic_area = serializers.PrimaryKeyRelatedField(
        many=True,
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
        slug_field='id',
        required=False,
        queryset=OrgType.objects.all()
    )
    org_targetdemographic = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        slug_field='id',
        required=False,
        queryset=TargetDemographic.objects.all()
    )

    class Meta:
        model = CleanData
        fields = '__all__'
        extra_kwargs = {
            'org_settlement': {'required': False, 'read_only': False, 'many': True,
                               'queryset': SettlementOrgAssociation.objects.all()},
        }

    # def create(self, validated_data):
    #     # print(validated_data)
    #     try:
    #         items = []
    #         if 'settlements' in validated_data:
    #             items = validated_data.pop('settlements')
    #             # print(items)
    #         convener = Convener.objects.create(name=validated_data["name"],
    #                                            convener_date=validated_data["convener_date"])
    #         challenge_list = []
    #         for item_data in items:
    #             challenge_ins = Challenges.objects.create(name=item_data['name'], statement=item_data['statement'],
    #                                                       document_links=item_data['document_links'])
    #             challenge_ins.theme.add(*item_data['theme'])
    #             challenge_ins.challenge_holders.add(*item_data['challenge_holders'])
    #             challenge_ins.save()
    #             challenge_list.append(challenge_ins)
    #         convener.challenges.set(challenge_list)
    #         convener.theme.set(validated_data['theme'])
    #         # print(validated_data['attending_organizations'])
    #         convener.save()
    #         # attendance
    #
    #         attendance = []
    #         if 'attending_organizations' in validated_data:
    #             attendance = validated_data.pop('attending_organizations')
    #         for a in attendance:
    #             attendance_ins = ConvenerOrgAttendance.objects.create(convener=convener, organization=a['organization'],
    #                                                                   total_attendance=a['total_attendance'])
    #
    #         return convener
    #     except Exception as e:
    #         raise serializers.ValidationError({
    #             'error': ['invalid data']
    #         })

    # def to_internal_value(self, data):
    #     if 'challenges' in data:
    #         if not isinstance(data.get('challenges', []), list):
    #             raise serializers.ValidationError({
    #                 'challenges': ['Expected a list of items but got type {input_type}'.format(
    #                     input_type=type(data.get('challenges')).__name__)]
    #             })
    #     return super().to_internal_value(data)
