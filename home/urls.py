from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(IndexView.as_view())),
    path('org-list/', login_required(CleanDataView.as_view())),
    path('sign-in/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('import-excel/', login_required(ImportData.as_view())),
    path('import-data/', import_excel),
    # path('save-excel/', store),

    path('settlements/', login_required(SettlementView.as_view())),
    path('org-type/', login_required(OrgTypeView.as_view())),
    path('thematic-area/', login_required(ThematicAreaView.as_view())),
    path('target-demographic/', login_required(TargetDemoView.as_view())),
    path('add-org/', login_required(AddOrgView.as_view())),
    path('org-details/<id>/', login_required(OrgDetailsView.as_view())),
    path('delete-org/<id>/', login_required(DeleteOrgView.as_view())),
    path('update-org-logo/<id>/', login_required(UpdateLogoView.as_view())),
    path('landing-page-content/', login_required(LandingPageContentView.as_view())),
    path('org-details-page-content/', login_required(OrgDetailsPageContentView.as_view())),
    path('create-user/', login_required(UserCreateView.as_view())),
    path('update-user/<id>/', login_required(UpdateUserView.as_view())),
    path('user-list/', login_required(UserListView.as_view())),
    path('raw-data/', login_required(RawDataView.as_view())),

    path('partner-types/', login_required(PartnerTypeListView.as_view())),
    path('partner-type-details/<id>/', login_required(PartnerTypeDetailsView.as_view())),
    path('create-partner-type/', login_required(PartnerTypeCreateView.as_view())),
    path('partners/', login_required(PartnerListView.as_view())),
    path('create-partner/', login_required(PartnerCreateView.as_view())),
    path('partner-details/<id>/', login_required(PartnerDetailsView.as_view())),
    path('change-org-status/<id>/', login_required(ChangeOrgStatusView.as_view())),
    path('download-excel-template/', login_required(download_excel_template)),
]



