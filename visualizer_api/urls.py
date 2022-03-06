from django.urls import path, include
from .views import *

urlpatterns = [
    path('filter-data/', CleanDataList.as_view()),
    path('org-types/', OrgTypeListView.as_view()),
    path('org-categories/', GeographicScopeListView.as_view()),
    path('technical-area/', ThematicAreaListView.as_view()),
    path('filter-items/', FilterItemView.as_view()),
]