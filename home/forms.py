from django import forms
from .models import Dump


class ImportDataForm(forms.ModelForm):
    class Meta:
        model = Dump
        fields = ('org_code', 'organisation_name', 'website', 'org_type', 'geographic_scope', 'primary_technicalsector',
                  'secondary_technicalsector', 'third_technicalsector', 'fourth_technicalsector',
                  'fifth_technicalsector',
                  'eco_system_tag', 'eco_map_sector', 'eco_map_subsector', 'number_of_convener', 'ulearn_subcategory',
                  'date_of_last_contact', 'primary_contact_name', 'phone', 'status_remarks', 'role', 'email',
                  'optional_contact', 'district', 'refugee_settlement', 'location_base')

        # date_of_last_contact = forms.DateField(widget=forms.DateInput(
        #     attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Username'
        #     }
        # ))
        # widgets = {
        #     'org_code': forms.TextInput(attrs={'class': 'form-control'}),
        #     'organisation_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'website': forms.TextInput(attrs={'class': 'form-control'})
        # }


