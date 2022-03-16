from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from .forms import ImportDataForm
from .models import *
from django import forms
import django_excel as excel
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def user_login(request):
    url = request.GET.get("next", '')
    print('url' + url)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(User.objects.filter(username=username, password=password).values('username'))
        print(username)
        try:
            get_user = User.objects.get(username=username)
        except:
            get_user = None
        if get_user is not None:
            # user = User.objects.get(username=username, password=password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('/admin/')
                else:
                    return redirect('/')
            else:
                messages.error(request, 'Password is incorrect')
                return render(request, 'login.html', {'url': url})

        else:
            messages.error(request, 'User not found!')
            return render(request, 'login.html', {'url': url})

    else:
        return render(request, 'login.html', {'url': url})


def user_logout(request):
    logout(request)
    return redirect('user_login')





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
            if row_num > 1:
                if row_data[6].strip() not in ('', 'None') and row_data[6] is not None:
                    settlement = Settlement.objects.get_or_create(value=row_data[6].strip(), title=row_data[6].strip())[
                        0]
                else:
                    settlement = None
                if row_data[4].strip() not in ('', 'None') and row_data[4] is not None:
                    org_type = OrgType.objects.get_or_create(value=row_data[4].strip(), title=row_data[4].strip())[0]
                else:
                    org_type = None
                if row_data[5].strip() not in ('', 'None') and row_data[5] is not None:
                    org_legaltype = OrgLegalType.objects.get_or_create(value=row_data[5].strip(), title=row_data[5].strip())[0]
                else:
                    org_legaltype = None
                if row_data[9].strip() not in ('', 'None') and row_data[9] is not None:
                    org_primarytechnicalarea = \
                    ThematicArea.objects.get_or_create(value=row_data[9].strip(), title=row_data[9].strip())[0]
                else:
                    org_primarytechnicalarea = None
                if row_data[11].strip() not in ('', 'None') and row_data[11] is not None:
                    org_secondarytechnicalarea1 = \
                    ThematicArea.objects.get_or_create(value=row_data[11].strip(), title=row_data[11].strip())[0]
                else:
                    org_secondarytechnicalarea1 = None
                if row_data[12].strip() not in ('', 'None') and row_data[12] is not None:
                    org_secondarytechnicalarea2 = \
                    ThematicArea.objects.get_or_create(value=row_data[12].strip(), title=row_data[12].strip())[0]
                else:
                    org_secondarytechnicalarea2 = None
                if row_data[14].strip() not in ('', 'None') and row_data[14] is not None:
                    org_targetdemographic = \
                    TargetDemographic.objects.get_or_create(value=row_data[14].strip(), title=row_data[14].strip())[0]
                else:
                    org_targetdemographic = None

                if (row_data[0].strip() not in ('', 'None') and row_data[0] is not None) or (
                        row_data[1].strip() not in ('', 'None') and row_data[1] is not None):
                    Dump.objects.create(org_name=row_data[0].strip(),
                                        org_acronym=row_data[1].strip(),
                                        founding_year=row_data[2].strip(),
                                        years_active=row_data[3].strip(),
                                        org_type=org_type,
                                        org_legaltype=org_legaltype,
                                        refugee_settlement=settlement,
                                        refugee_zone=row_data[7].strip(),
                                        org_offices=row_data[8].strip(),
                                        org_primarytechnicalarea=org_primarytechnicalarea,
                                        org_activities=row_data[10].strip(),
                                        org_secondarytechnicalarea1=org_secondarytechnicalarea1,
                                        org_secondarytechnicalarea2=org_secondarytechnicalarea2,
                                        org_targetgroup=row_data[13].strip(),
                                        org_targetdemographic=org_targetdemographic,
                                        org_primarycontact=row_data[15].strip(),
                                        org_email=row_data[16].strip(),
                                        org_phone=row_data[17].strip(),
                                        org_website=row_data[18].strip(),
                                        org_facebook=row_data[19].strip(),
                                        org_twitter=row_data[20].strip(),
                                        org_logo=row_data[21].strip(),
                                        contact_name=row_data[22].strip(),
                                        contact_role=row_data[23].strip(),
                                        contact_email=row_data[24].strip(),
                                        contact_phone=row_data[25].strip(),
                                        # ,refugee_settlement_collected_from= row_data[33]
                                        )
                    cdata = CleanData.objects.filter(org_name=row_data[0].strip())
                    print(cdata.count())
                    if cdata.count() > 0:
                        cdata.update(
                            org_acronym=row_data[1].strip(),
                            founding_year=row_data[2].strip(),
                            years_active=row_data[3].strip(),
                            org_type=org_type,
                            org_legaltype=org_legaltype,
                            refugee_settlement=settlement,
                            refugee_zone=row_data[7].strip(),
                            org_offices=row_data[8].strip(),
                            org_primarytechnicalarea=org_primarytechnicalarea,
                            org_activities=row_data[10].strip(),
                            org_secondarytechnicalarea1=org_secondarytechnicalarea1,
                            org_secondarytechnicalarea2=org_secondarytechnicalarea2,
                            org_targetgroup=row_data[13].strip(),
                            org_targetdemographic=org_targetdemographic,
                            org_primarycontact=row_data[15].strip(),
                            org_email=row_data[16].strip(),
                            org_phone=row_data[17].strip(),
                            org_website=row_data[18].strip(),
                            org_facebook=row_data[19].strip(),
                            org_twitter=row_data[20].strip(),
                            org_logo=row_data[21].strip(),
                            contact_name=row_data[22].strip(),
                            contact_role=row_data[23].strip(),
                            contact_email=row_data[24].strip(),
                            contact_phone=row_data[25].strip(),
                        )
                    else:
                        CleanData.objects.create(org_name=row_data[0].strip(),
                                                 org_acronym=row_data[1].strip(),
                                                 founding_year=row_data[2].strip(),
                                                 years_active=row_data[3].strip(),
                                                 org_type=org_type,
                                                 org_legaltype=org_legaltype,
                                                 refugee_settlement=settlement,
                                                 refugee_zone=row_data[7].strip(),
                                                 org_offices=row_data[8].strip(),
                                                 org_primarytechnicalarea=org_primarytechnicalarea,
                                                 org_activities=row_data[10].strip(),
                                                 org_secondarytechnicalarea1=org_secondarytechnicalarea1,
                                                 org_secondarytechnicalarea2=org_secondarytechnicalarea2,
                                                 org_targetgroup=row_data[13].strip(),
                                                 org_targetdemographic=org_targetdemographic,
                                                 org_primarycontact=row_data[15].strip(),
                                                 org_email=row_data[16].strip(),
                                                 org_phone=row_data[17].strip(),
                                                 org_website=row_data[18].strip(),
                                                 org_facebook=row_data[19].strip(),
                                                 org_twitter=row_data[20].strip(),
                                                 org_logo=row_data[21].strip(),
                                                 contact_name=row_data[22].strip(),
                                                 contact_role=row_data[23].strip(),
                                                 contact_email=row_data[24].strip(),
                                                 contact_phone=row_data[25].strip(),
                                                 )
            row_num = row_num + 1
        return redirect('/')
        # return render(request, 'exceldata.html', {"excel_data": excel_data})


