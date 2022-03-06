from django.urls import path, include
from .views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('clean-data/', CleanDataView.as_view()),
    path('login/', LoginView.as_view()),
    path('import-data/', ImportData.as_view()),
    path('import-excel/', import_excel),
    path('save-excel/', store),
]