from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from .forms import ImportDataForm
from .models import *
from django import forms
import django_excel as excel

class IndexView(View):
    def get(self, request):
        data = Dump.objects.all()
        context = {
            'data': data
        }
        return render(request, 'advance_table.html', context)


class CleanDataView(View):
    def get(self, request):
        data = CleanData.objects.all()
        context = {
            'data': data
        }
        return render(request, 'clean_data.html', context)


class LoginView(View):
    def get(self, request):
        # companies = CompanyInfo.objects.all()
        context = {
            'companies': None
        }
        return render(request, 'login.html', context)


class ImportData(View):
    def post(self, request):
        # companies = CompanyInfo.objects.all()
        if request.method == 'POST':
            form = ImportDataForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                print("form is invalid")
            return redirect('/')
        else:
            form = ImportDataForm()
            context = {
                'form': form
            }
            return render(request, 'input.html', context)

    def get(self, request):
        form = ImportDataForm()
        context = {
            'form': form
        }
        return render(request, 'input.html', context)

from django.shortcuts import render
import openpyxl


def import_excel(request):
    if "GET" == request.method:
        return render(request, '/', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        row_num = 0
        # settle
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
            if row_num >1:
                if row_data[32].strip() not in ('', 'None') and row_data[32] is not None:
                    settlement = Settlement.objects.get_or_create(value=row_data[32].strip(), title =row_data[32].strip())[0]
                else:
                    settlement = None
                if row_data[4].strip() not in ('', 'None') and row_data[4] is not None:
                    org_type = OrgType.objects.get_or_create(value=row_data[4].strip(), title =row_data[4].strip())[0]
                else:
                    org_type = None
                if row_data[5].strip() not in ('', 'None') and row_data[5] is not None:
                    geographic_scope = GeographicScope.objects.get_or_create(value=row_data[5].strip(), title =row_data[5].strip())[0]
                else:
                    geographic_scope = None
                if row_data[6].strip() not in ('', 'None') and row_data[6] is not None:
                    primary_technicalsector = ThematicArea.objects.get_or_create(value=row_data[6].strip(), title =row_data[6].strip())[0]
                else:
                    primary_technicalsector = None
                if row_data[7].strip() not in ('', 'None') and row_data[7] is not None:
                    secondary_technicalsector = ThematicArea.objects.get_or_create(value=row_data[7].strip(), title =row_data[7].strip())[0]
                else:
                    secondary_technicalsector = None
                if row_data[8].strip() not in ('', 'None') and row_data[8] is not None:
                    third_technicalsector = ThematicArea.objects.get_or_create(value=row_data[8].strip(), title =row_data[8].strip())[0]
                else:
                    third_technicalsector = None
                if row_data[9].strip() not in ('', 'None') and row_data[9] is not None:
                    fourth_technicalsector = ThematicArea.objects.get_or_create(value=row_data[9].strip(), title =row_data[9].strip())[0]
                else:
                    fourth_technicalsector = None
                if row_data[10].strip() not in ('', 'None') and row_data[10] is not None:
                    fifth_technicalsector = ThematicArea.objects.get_or_create(value=row_data[10].strip(), title =row_data[10].strip())[0]
                else:
                    fifth_technicalsector = None

                if row_data[23].strip() not in ('', 'None') and row_data[23] is not None:
                    date_of_last_contact = row_data[23]
                else:
                    date_of_last_contact = None

                if (row_data[1].strip() not in ('', 'None') and row_data[1] is not None) or (row_data[2].strip() not in ('', 'None') and row_data[2] is not None):
                    Dump.objects.create(org_code=row_data[0].strip()
                                        ,organisation_name= row_data[1].strip()
                                        ,organisation_name2= row_data[2].strip()
                                        ,website= row_data[3].strip()
                                        ,org_type=org_type
                                        ,geographic_scope=geographic_scope
                                        ,primary_technicalsector=primary_technicalsector
                                        ,secondary_technicalsector=secondary_technicalsector
                                        ,third_technicalsector=third_technicalsector
                                        ,fourth_technicalsector=fourth_technicalsector
                                        ,fifth_technicalsector=fifth_technicalsector
                                        ,eco_system_tag= row_data[11].strip()
                                        ,eco_map_sector= row_data[12].strip()
                                        ,eco_map_subsector= row_data[13].strip()
                                        # ,total_number_of_interactions_ril= row_data[21]
                                        ,ulearn_subcategory= row_data[22].strip()
                                        ,date_of_last_contact= date_of_last_contact
                                        ,status_remarks= row_data[24].strip()
                                        ,primary_contact_name= row_data[25].strip()
                                        ,role= row_data[26].strip()
                                        ,email= row_data[27].strip()
                                        ,phone= row_data[28].strip()
                                        ,optional_contact= row_data[29].strip()
                                        ,location_base= row_data[30].strip()
                                        ,district= row_data[31].strip()
                                        ,refugee_settlement= settlement
                                        # ,refugee_settlement_collected_from= row_data[33]
                                        )
                    cdata = CleanData.objects.filter(org_code=row_data[0].strip(), organisation_name=row_data[1].strip())
                    print(cdata.count())
                    if cdata.count() > 0:
                        cdata.update(
                             #    org_code=row_data[0]
                             # , organisation_name=row_data[1]
                               organisation_name2=row_data[2]
                             , website=row_data[3].strip()
                             , org_type=org_type
                             , geographic_scope=geographic_scope
                             , primary_technicalsector=primary_technicalsector
                             , secondary_technicalsector=secondary_technicalsector
                             , third_technicalsector=third_technicalsector
                             , fourth_technicalsector=fourth_technicalsector
                             , fifth_technicalsector=fifth_technicalsector
                             , eco_system_tag=row_data[11].strip()
                             , eco_map_sector=row_data[12].strip()
                             , eco_map_subsector=row_data[13].strip()
                             # ,total_number_of_interactions_ril= row_data[21]
                             , ulearn_subcategory=row_data[22].strip()
                             , date_of_last_contact=date_of_last_contact
                             , status_remarks=row_data[24].strip()
                             , primary_contact_name=row_data[25].strip()
                             , role=row_data[26].strip()
                             , email=row_data[27].strip()
                             , phone=row_data[28].strip()
                             , optional_contact=row_data[29].strip()
                             , location_base=row_data[30].strip()
                             , district=row_data[31].strip()
                             , refugee_settlement=settlement
                             # ,refugee_settlement_collected_from= row_data[33]
                        )
                    else:
                        CleanData.objects.create(org_code=row_data[0].strip()
                                    , organisation_name=row_data[1].strip()
                                    , organisation_name2=row_data[2].strip()
                                    , website=row_data[3].strip()
                                    , org_type=org_type
                                    , geographic_scope=geographic_scope
                                    , primary_technicalsector=primary_technicalsector
                                    , secondary_technicalsector=secondary_technicalsector
                                    , third_technicalsector=third_technicalsector
                                    , fourth_technicalsector=fourth_technicalsector
                                    , fifth_technicalsector=fifth_technicalsector
                                    , eco_system_tag=row_data[11].strip()
                                    , eco_map_sector=row_data[12].strip()
                                    , eco_map_subsector=row_data[13].strip()
                                    # ,total_number_of_interactions_ril= row_data[21]
                                    , ulearn_subcategory=row_data[22].strip()
                                    , date_of_last_contact=date_of_last_contact
                                    , status_remarks=row_data[24].strip()
                                    , primary_contact_name=row_data[25].strip()
                                    , role=row_data[26].strip()
                                    , email=row_data[27].strip()
                                    , phone=row_data[28].strip()
                                    , optional_contact=row_data[29].strip()
                                    , location_base=row_data[30].strip()
                                    , district=row_data[31].strip()
                                    , refugee_settlement=settlement
                                    # ,refugee_settlement_collected_from= row_data[33]
                                    )
            row_num = row_num + 1
        return redirect('/')
        # return render(request, 'exceldata.html', {"excel_data": excel_data})

class UploadFileForm(forms.Form):
    file = forms.FileField()

def store(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        print(request.FILES['file'])
        if form.is_valid():
            request.FILES['file'].save_to_database(
                model=Dump,
                mapdict=['org_code', 'organisation_name', 'website', 'org_type', 'geographic_scope', 'primary_technicalsector',
              'secondary_technicalsector', 'third_technicalsector', 'fourth_technicalsector',
              'fifth_technicalsector',
              'eco_system_tag', 'eco_map_sector', 'eco_map_subsector', 'number_of_convener', 'ulearn_subcategory',
              'date_of_last_contact', 'primary_contact_name', 'phone', 'status_remarks', 'role', 'email',
              'optional_contact', 'district', 'refugee_settlement', 'location_base'])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        return render(request, 'exceldata.html', {})
