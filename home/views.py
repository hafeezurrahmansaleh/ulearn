import datetime

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
from titlecase import titlecase


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
                return render(request, 'sign-in.html', {'url': url})

        else:
            messages.error(request, 'User not found!')
            return render(request, 'sign-in.html', {'url': url})

    else:
        return render(request, 'sign-in.html', {'url': url})


def user_logout(request):
    logout(request)
    return redirect('user_login')


class IndexView(View):
    def get(self, request):
        data = Dump.objects.all()
        context = {
            'data': data
        }
        return render(request, 'index_ulearn.html', context)


class CleanDataView(View):
    def get(self, request):
        data = CleanData.objects.all()
        context = {
            'data': data
        }
        return render(request, 'cleandata.html', context)


class LoginView(View):
    def get(self, request):
        # companies = CompanyInfo.objects.all()
        context = {
            'companies': None
        }
        return render(request, 'sign-in.html', context)


class SettlementView(View):
    def get(self, request):
        data = Settlement.objects.all()
        context = {
            'data': data
        }
        return render(request, 'settlements.html', context)


class OrgTypeView(View):
    def get(self, request):
        data = OrgType.objects.all()
        context = {
            'data': data
        }
        return render(request, 'org-type.html', context)


class AddOrgView(View):
    def get(self, request):
        data = OrgType.objects.all()
        context = {
            'data': data
        }
        return render(request, 'org-details.html', context)


class TargetDemoView(View):
    def get(self, request):
        data = TargetDemographic.objects.all()
        context = {
            'data': data
        }
        return render(request, 'target-demographic.html', context)


class ThematicAreaView(View):
    def get(self, request):
        data = ThematicArea.objects.all()
        context = {
            'data': data
        }
        return render(request, 'thematic-area.html', context)


class LandingPageContentView(View):
    def get(self, request):
        data = LandingPageContent.objects.all().first()
        context = {
            'data': data
        }
        return render(request, 'landing-page-content.html', context)


class OrgDetailsPageContentView(View):
    def get(self, request):
        data = OrgDetailsPageContent.objects.all().first()
        context = {
            'data': data
        }
        return render(request, 'orgdetails-page-content.html', context)


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
            return render(request, 'import-excel.html', context)

    def get(self, request):
        # form = ImportDataForm()
        # context = {
        #     'form': form
        # }
        return render(request, 'import-excel.html')


from django.shortcuts import render
import openpyxl


def import_excel(request):
    if "GET" == request.method:
        return render(request, '/', {})
    else:
        excel_file = request.FILES["excel_file"]

        import pandas as pd

        df = pd.read_excel(excel_file, sheet_name=0)

        alt_logos = AlternativeLogo.objects.all()

        for _, d in df.iterrows():
            start = d['start']
            end = d['end']
            today = d['today']
            logo = None  # d['logo']
            name_personal = titlecase(str(d['name_personal']).replace('nan', ''))
            job_title = str(d['job_title']).replace('nan', '')
            email_address = str(d['email_address']).replace('nan', '')
            respondent_telephone = str(d['respondent_telephone']).replace('nan', '').replace('.0', '')
            org_name = titlecase(str(d['org_name']).replace('nan', ''))
            org_acronym = str(d['org_acronym']).replace('nan', '')
            org_email = str(d['org_email']).replace('nan', '')
            org_telephone = str(d['org_telephone']).replace('nan', '').replace('.0', '')
            org_website = str(d['org_website']).replace('nan', '')
            org_facebook = str(d['org_facebook']).replace('nan', '')
            org_twitter = str(d['org_twitter']).replace('nan', '')
            org_logo = str(d['org_logo']).replace('nan', '')
            img = str(d['img']).replace('nan', '')
            img_URL = str(d['img_URL']).replace('nan', '')
            founding_year = str(d['founding_year']).replace('nan', '').replace('_', '')[:4]
            if founding_year.isnumeric():
                print('Founding Year: ' + founding_year)
                years_active = int(datetime.datetime.today().year) - int(founding_year) + 1
            else:
                founding_year = None
                years_active = None

            org_contact = str(d['org_contact']).replace('nan', '')
            org_type = str(d['org_type']).replace('nan', '')
            org_type_other = str(d['org_type_other']).replace('nan', '')
            org_legal_type = titlecase(str(d['org_legal_type']).replace('nan', '').strip().replace('_', ' '))
            org_legal_type_other = titlecase(
                str(d['org_legal_type_other']).replace('nan', '').strip().replace('_', ' '))
            org_target_community = titlecase(
                str(d['org_target_community']).replace('nan', '').strip().replace('_', ' '))
            org_target_community_other = titlecase(
                str(d['org_target_community_other']).replace('nan', '').strip().replace('_',
                                                                                        ' '))
            org_target_demographic = str(d['org_target_demographic']).replace('nan', '')
            org_target_demographic_other = str(d['org_target_demographic_other']).replace('nan', '')
            settlement_operation = str(d['settlement_operation']).replace('nan', '')
            org_primary_technical_area_focus = str(d['org_primary_technical_area_focus']).replace('nan', '')
            refugee_settlement = str(d['refugee_settlement']).replace('nan', '')

            other_actors_in_settlement = str(d['other_actors_in_settlement']).replace('nan', '')

            contact_name = str(d['contact_name']).replace('nan', '')
            contact_role = str(d['contact_role']).replace('nan', '')
            contact_telephone = str(d['contact_telephone']).replace('nan', '').replace('.0', '')
            contact_email = str(d['contact_email']).replace('nan', '')

            _id = d['_id']
            _uuid = d['_uuid']
            _submission_time = d['_submission_time']
            _validation_status = d['_validation_status']
            _notes = d['_notes']
            _status = d['_status']
            _submitted_by = d['_submitted_by']
            _tags = d['_tags']
            _index = d['_index']

            if org_name is None or org_name.strip() == '':
                continue

            if org_type.strip() not in ('', 'None', 'Other', 'other', 'nan') and org_type is not None:
                org_type_ins = OrgType.objects.get_or_create(value=titlecase(org_type.strip().replace('_', ' ')),
                                                             title=titlecase(org_type.strip().replace('_', ' ')),
                                                             exclude_from_filter=False
                                                             )[0]
            elif org_type.strip() in ('Other', 'other') and org_type_other is not None and org_type_other not in (
                    '', 'None'):
                org_type_ins = \
                    OrgType.objects.get_or_create(value=titlecase(org_type_other.strip().replace('_', ' ')),
                                                  title=titlecase(org_type_other.strip().replace('_', ' ')))[0]
            else:
                org_type_ins = None

            target_demo_list = []
            if org_target_demographic.strip() not in (
                    '', 'None', 'NaN', 'Nan', 'nan') and org_target_demographic is not None:
                target_demos = str(org_target_demographic.strip()).split(' ')
                for td in target_demos:
                    if td not in ('', 'None', 'Other', 'other', 'NaN') and org_target_demographic is not None:
                        target_demo_list.append(
                            TargetDemographic.objects.get_or_create(value=titlecase(td.strip().replace('_', ' ')),
                                                                    title=titlecase(td.strip().replace('_', ' ')),
                                                                    exclude_from_filter=False
                                                                    )[0].id
                        )
                    # else:
                    #     target_demo_list.append(TargetDemographic.objects.get_or_create(
                    #         value=titlecase(org_target_demographic_other.strip()),
                    #         title=titlecase(org_target_demographic_other.strip()))[0].id)
            else:
                org_target_demographic_ins = None

            if org_target_community.strip() not in (
                    '', 'None', 'Other', 'other', 'nan') and org_target_community is not None:
                org_target_community_val = titlecase(org_target_community.strip().replace('_', ' '))
            else:
                org_target_community_val = titlecase(org_target_community_other.replace('nan', '').replace('_', ' '))

            # # ORG logo cleanup
            # if img_URL not in ('', 'nan', 'None') and img_URL is not None:
            #     print("Image URL" + img_URL)
            #     pass
            # else:
            #     alt_logo_ins = alt_logos.filter(org_type__title=org_type).first()
            #     if alt_logo_ins is not None:
            #         img_URL = request.build_absolute_uri(alt_logo_ins.logo.url)
            #
            #     print("Image URL" + img_URL)

            # Insert Org data to Clean Data
            cdata = CleanData.objects.filter(org_name=org_name)
            print(cdata.count())
            if cdata.count() > 0:
                cdata.update(
                    respondent_name=name_personal,
                    respondent_job_title=job_title,
                    respondent_email_address=email_address,
                    respondent_telephone=respondent_telephone,
                    org_name=org_name,
                    org_acronym=org_acronym,
                    org_email=org_email,
                    org_phone=org_telephone,
                    org_website=org_website,
                    org_facebook=org_facebook,
                    org_twitter=org_twitter,
                    org_logo=img_URL,
                    founding_year=founding_year,
                    years_active=years_active,
                    org_primarycontact=org_contact,
                    org_type=org_type_ins,
                    org_legaltype=org_legal_type,
                    org_primary_technical_area_focus=org_primary_technical_area_focus,
                    org_targetgroup=org_target_community_val,
                    other_actors_in_settlement=other_actors_in_settlement,
                    contact_name=contact_name,
                    contact_role=contact_role,
                    contact_phone=contact_telephone,
                    contact_email=contact_email,
                    uuid=_uuid
                )
                SettlementOrgAssociation.objects.filter(org=cdata[0]).delete()
                cleandata_ins = cdata[0]
            else:
                cleandata_ins = CleanData(respondent_name=name_personal,
                                          respondent_job_title=job_title,
                                          respondent_email_address=email_address,
                                          respondent_telephone=respondent_telephone,
                                          org_name=org_name,
                                          org_acronym=org_acronym,
                                          org_email=org_email,
                                          org_phone=org_telephone,
                                          org_website=org_website,
                                          org_facebook=org_facebook,
                                          org_twitter=org_twitter,
                                          org_logo=img_URL,
                                          founding_year=founding_year,
                                          years_active=years_active,
                                          org_primarycontact=org_contact,
                                          org_type=org_type_ins,
                                          org_legaltype=org_legal_type,
                                          org_primary_technical_area_focus=org_primary_technical_area_focus,
                                          org_targetgroup=org_target_community_val,
                                          other_actors_in_settlement=other_actors_in_settlement,
                                          contact_name=contact_name,
                                          contact_role=contact_role,
                                          contact_phone=contact_telephone,
                                          contact_email=contact_email,
                                          uuid=_uuid
                                          )
                cleandata_ins.save()
            cleandata_ins.org_targetdemographic.set(target_demo_list)

            refugee_settlement = str(refugee_settlement).strip()
            settlement_list = refugee_settlement.split(' ')
            for l in settlement_list:
                if l is not None and l != '':
                    if '_camp' in l:
                        l = l.replace('_camp', '')
                    settlement_name = l.strip()
                    zone_col_nm = l + "_one"
                    print(zone_col_nm)
                    if zone_col_nm != 'nan_one' and zone_col_nm != '_one':
                        try:
                            l_zones = str(d[zone_col_nm]).replace('nan', '')
                            l_zones = l_zones.strip()
                            l_zones = l_zones.replace(' ', ', ')
                            l_zones = titlecase(l_zones.replace('_', ' '))
                        except:
                            l_zones = None
                        print(l_zones)
                    else:
                        l_zones = None

                    operations_col_nm = l + "_two"
                    if operations_col_nm != 'nan_two' and operations_col_nm != '_two':
                        try:
                            l_operation_offices = d[operations_col_nm].strip().replace('nan', '')
                            l_operation_offices = l_operation_offices.strip()
                            l_operation_offices = l_operation_offices.replace(' ', ', ')
                            l_operation_offices = l_operation_offices.replace(',,', ',')
                            l_operation_offices = titlecase(l_operation_offices.replace('_', ' '))
                        except:
                            l_operation_offices = None
                        print(l_operation_offices)
                    else:
                        l_operation_offices = None

                    staff_col_nm = l + "_three"
                    if staff_col_nm != 'nan_three' and staff_col_nm != '_three':
                        try:
                            l_staffs = int(str(d[staff_col_nm]).replace('nan', '0').replace('.0', ''))
                        except:
                            l_staffs = None
                        print("This is Stuff number: " + str(l_staffs))
                    else:
                        l_staffs = None
                    primary_thematic_area_col_nm = l + "_four"
                    pta_id_list = []
                    if primary_thematic_area_col_nm != 'nan_four' and staff_col_nm != '_four':
                        try:
                            l_primary_thematic_areas = str(d[primary_thematic_area_col_nm]).replace('nan', '')
                            primary_thematic_list = str(l_primary_thematic_areas).split(' ')
                            for pta in primary_thematic_list:
                                if str(pta) in ('Other', 'other'):
                                    pta_other = d[primary_thematic_area_col_nm + '_other'].strip().replace('nan', '')
                                    # if pta_other != '':
                                    #     pta_id_list.append(
                                    #         ThematicArea.objects.get_or_create(
                                    #             value=titlecase(pta_other.replace('_', ' ')),
                                    #             title=titlecase(pta_other.replace('_', ' ')))[
                                    #             0].id)
                                elif pta not in ('', 'nan'):
                                    pta_id_list.append(
                                        ThematicArea.objects.get_or_create(value=titlecase(pta.replace('_', ' ')),
                                                                           title=titlecase(pta.replace('_', ' ')),
                                                                           exclude_from_filter=False
                                                                           )[0].id)
                        except:
                            l_primary_thematic_areas = None
                        print(l_primary_thematic_areas)

                    settlement_ins = \
                        Settlement.objects.get_or_create(value=titlecase(settlement_name.replace('_', ' ')),
                                                         title=titlecase(settlement_name.replace('_', ' ')))[
                            0]
                    sttlmnt_org_ins = SettlementOrgAssociation(
                        settlement=settlement_ins,
                        org=cleandata_ins,
                        num_of_staffs=l_staffs,
                        operation_offices=l_operation_offices,
                        zones=l_zones
                    )
                    sttlmnt_org_ins.save()
                    sttlmnt_org_ins.primary_thematic_area.set(pta_id_list)

                # print(d['rhino_one'])
                # print(d["'"+l.split('_')[0]+"_one"])
        messages.error(request, 'File imported successfully!')
        return redirect('/')

# return redirect('/')
# return render(request, 'exceldata.html', {"excel_data": excel_data})
