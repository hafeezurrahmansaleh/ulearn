from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('raw-data/', login_required(IndexView.as_view())),
    path('clean-data/', login_required(CleanDataView.as_view())),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('', login_required(ImportData.as_view())),
    # path('import-excel/', import_excel),
    # path('save-excel/', store),
]
