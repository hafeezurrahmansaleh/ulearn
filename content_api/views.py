
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticated, AllowAny
)
# from urllib3.connectionpool import xrange
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *

import csv
#
from django.http import HttpResponse, JsonResponse
#
from rest_framework.views import APIView
import datetime as dt


class OrgTypeCreateView(generics.CreateAPIView):
    """
       endpoint for retrieving the list of organization types
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = OrgTypeContentSerializer


class OrgTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
       endpoint for retrieving the list of organization types
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = OrgTypeContentSerializer
    lookup_field = 'pk'
    queryset = OrgType.objects.all()


class ThematicAreaCreateView(generics.CreateAPIView):
    """
       endpoint for creating the list of technical areas
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = ThematicAreaContentSerializer


class ThematicAreaDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
       endpoint for creating the list of technical areas
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = ThematicAreaContentSerializer
    lookup_field = 'pk'
    queryset = ThematicArea.objects.all()


class SettlementCreateView(generics.CreateAPIView):
    """
       endpoint for creating the list of settlement
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = SettlementContentSerializer


class SettlementDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
       endpoint for updating the list of settlement
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = SettlementContentSerializer
    lookup_field = 'pk'
    queryset = Settlement.objects.all()


class TargetDemographicCreateView(generics.CreateAPIView):
    """
       endpoint for creating the list of technical areas
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = TargetDemographicContentSerializer


class TargetDemographicDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
       endpoint for creating the list of technical areas
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = TargetDemographicContentSerializer
    lookup_field = 'pk'
    queryset = TargetDemographic.objects.all()


class LandingPageContentCreateView(APIView):
    """
       endpoint for retrieving the list of technical areas
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = LandingPageContentDetailsSerializer


class LandingPageContentDetailsView(APIView):
    """
       endpoint for retrieving the list of technical areas
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = LandingPageContentDetailsSerializer
    lookup_field = 'pk'
    queryset = LandingPageContent.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
       endpoint for creating the list of technical areas
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = UserDetailsSerializer
    lookup_field = 'username'
    queryset = User.objects.all()


class DropdownItemView(APIView):
    def get(self, request):
        settlements = list(Settlement.objects.all().values('id', 'value').distinct())
        # geographic_scopes = list(GeographicScope.objects.all().values('id','value').distinct())
        type_of_org = list(OrgType.objects.filter(exclude_from_filter=False).values('id', 'value').distinct())
        thematic_area_of_work = list(
            ThematicArea.objects.filter(exclude_from_filter=False).values('id', 'value').distinct())
        type_of_demographic = list(
            TargetDemographic.objects.filter(exclude_from_filter=False).values('id', 'value').distinct())
        target_community = list(
            TargetCommunity.objects.filter(exclude_from_filter=False).values('id', 'value').distinct())
        zone = list(
            SettlementZone.objects.all().values('id', 'settlement_id', 'value').distinct())
        # new_dict = {'id': -1,'value': 'Other'}
        # c = new_dict.copy()
        # type_of_org.append(c)
        # thematic_area_of_work.append(c)
        # type_of_demographic.append(c)
        # type_of_org = type_of_org.append("{'id': -1, 'value': 'Other'}" )
        return JsonResponse({'settlements': settlements,
                             'zone': zone,
                             'type_of_org': type_of_org,
                             'thematic_area_of_work': thematic_area_of_work,
                             'target_demographic': type_of_demographic,
                             'target_community': target_community,
                             },
                            safe=False, status=status.HTTP_200_OK)


class DataEntryView(generics.ListCreateAPIView):
    """
       endpoint for retrieving the list of technical areas
    """

    permission_classes = (AllowAny,)
    serializer_class = DataEntrySerializer
    queryset = CleanData.objects.filter(data_source='Form Submission')

    def create(self, request, *args, **kwargs):
        target_demographics = request.data.pop('org_targetdemographic', [])
        org_type = request.data.pop('org_type', '')
        target_demographic_instances = []
        for t in target_demographics:
            instance, created = TargetDemographic.objects.get_or_create(value=t, defaults={'title': t, 'exclude_from_filter': True})
            target_demographic_instances.append(instance)

        ot_instance, created = OrgType.objects.get_or_create(value=org_type,
                                                                    defaults={'title': org_type, 'exclude_from_filter': True})
        request.data['org_targetdemographic'] = [instance.value for instance in target_demographic_instances]
        request.data['org_type'] = ot_instance.value
        return super().create(request, *args, **kwargs)

class PartnerTypeListView(generics.ListCreateAPIView):
    """
       endpoint for creating the list of technical areas
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = PartnerTypeSerializer
    queryset = PartnerType.objects.all()


class PartnerTypeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
       endpoint for creating the list of technical areas
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = PartnerTypeSerializer
    lookup_field = 'id'
    queryset = PartnerType.objects.all()


class PartnerListView(generics.ListCreateAPIView):
    """
       endpoint for creating the list of technical areas
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = PartnerSerializer
    queryset = PartnerLogo.objects.all()


class PartnerDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
       endpoint for creating the list of technical areas
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = PartnerSerializer
    lookup_field = 'id'
    queryset = PartnerLogo.objects.all()