import json

from django.apps import apps
from django.core import serializers as sz
from django.http import JsonResponse
# from knox.auth import TokenAuthentication
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticated
)
# from urllib3.connectionpool import xrange
from rest_framework.views import APIView

from .serializers import *
# Create your views here.


class CleanDataList(generics.ListAPIView):
    """
       endpoint for retrieving all data
    """
    # permission_classes = (IsAuthenticated,)
    serializer_class = DumpDataSerializer
    # --queryset = Dump.objects.all()
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        dump_list = Dump.objects.all()
        return dump_list


class FilterCleanDatView(generics.ListAPIView):
    """
       endpoint for filtering clean data
    """
    # permission_classes = (IsAuthenticated,)
    serializer_class = DumpDataSerializer
    # --queryset = Dump.objects.all()
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        dump_list = Dump.objects.all()
        return dump_list


class OrgTypeListView(generics.ListAPIView):
    """
       endpoint for retrieving the list of organization types
    """
    # permission_classes = (IsAuthenticated,)
    serializer_class = OrgTypeSerializer
    # --queryset = Dump.objects.all()
    # pagination_class = LimitOffsetPagination

    def get_queryset(self):
        dump_list = OrgType.objects.all()
        return dump_list


class GeographicScopeListView(generics.ListAPIView):
    """
       endpoint for retrieving the list of organization categories
    """
    # permission_classes = (IsAuthenticated,)
    serializer_class = GeographicScopeSerializer
    # --queryset = Dump.objects.all()
    # pagination_class = LimitOffsetPagination

    def get_queryset(self):
        dump_list = GeographicScope.objects.all()
        return dump_list


class ThematicAreaListView(generics.ListAPIView):
    """
       endpoint for retrieving the list of technical areas
    """
    # permission_classes = (IsAuthenticated,)
    serializer_class = ThematicAreaSerializer
    # --queryset = Dump.objects.all()
    # pagination_class = LimitOffsetPagination

    def get_queryset(self):
        dump_list = ThematicArea.objects.all()
        return dump_list


class FilterItemView(APIView):
    def get(self, request):
        settlements = list(Settlement.objects.all().values('id','value').distinct())
        geographic_scopes = list(GeographicScope.objects.all().values('id','value').distinct())
        type_of_org = list(OrgType.objects.all().values('id','value').distinct())
        thematic_area_of_work = list(ThematicArea.objects.all().values('id','value').distinct())
        type_of_demographic = None
        return JsonResponse({'settlements': settlements,
                             'graphic_scopes': geographic_scopes,
                             'type_of_org': type_of_org,
                             'thematic_area_of_work': thematic_area_of_work,
                             'type_of_demographic': type_of_demographic
                             },
                            safe=False, status=status.HTTP_200_OK)
