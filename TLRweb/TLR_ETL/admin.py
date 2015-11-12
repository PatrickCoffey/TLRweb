from django.contrib import admin
from .models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export import fields


class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Client Info', {'fields': ['hrn', 'name', 'age', 'gender', 'ethnicity', 'community']}),
        ('Care Plans', {'fields': ['AHCP', 'AHCDate', 'PCDP', 'PCDDate', 'RHDP', 'RHDDate', 'planMonth']}),
        ('MBS', {'fields': ['mbs715', 'mbs721', 'mbs723', 'mbs732', 'revMonth']}),
        ('CVRA', {'fields': ['CVRStatus', 'CVRDate']}),
        ('PCD\'s', {'fields': ['eligiblePCD', 'diabetes', 'cvd', 'hiCVR', 'rhd', 'lung', 'renal']}),
        ('Missed Diagnoses', {'fields': ['missedDiabetes', 'missedCKD'], 'classes': ['collapse']}),
        ('Renal CC', {'fields': ['renalCC']}),
        ('Medications', {'fields': ['asprin', 'antiHT', 'ACE', 'ARB', 'statin', 'metformin', 'sulfonurics', 'insulin', 'gliptin', 'otherDiabetes']}),
        ('Results', {'fields': ['bmi', 'sysBP', 'diaBP', 'tChol', 'ldl', 'hba1c', 'acr', 'egfr', 'smoking']}),
    ]

class CsvPopulationResource(resources.ModelResource):
    raise_errors = True
    # how to override the default column names
    Usual_Clinic_Name = fields.Field(column_name='Usual Clinic Name')
    HRN = fields.Field(column_name='HRN')
    sex = fields.Field(column_name='Sex')
    Indigenous_Status_Desc = fields.Field(column_name='Indigenous Status Desc')
    Current_Age_years = fields.Field(column_name='Current Age (years)')
    
    class meta:
        model = csvPopulation

class CsvPopulationAdmin(ImportExportModelAdmin):
    resource_class = CsvPopulationResource
    pass

class ComAliasInline(admin.StackedInline):
    model = CommunityAliases
    
class CommunityAdmin(admin.ModelAdmin):
    inlines = [ComAliasInline]


admin.site.register(csvACR)
admin.site.register(csvBMI)
admin.site.register(csvCareplan)
admin.site.register(csvCaseConference)
admin.site.register(csvCVRa)
admin.site.register(csvDiaBP)
admin.site.register(csvDrugs)
admin.site.register(csvEGFR)
admin.site.register(csvHBA1C)
admin.site.register(csvLDL)
admin.site.register(csvMBS)
admin.site.register(csvPCD)
admin.site.register(csvPCDReview)
admin.site.register(csvSmoking)
admin.site.register(csvSysBP)
admin.site.register(csvTchol)
admin.site.register(csvPopulation, CsvPopulationAdmin)    
admin.site.register(Community, CommunityAdmin)
admin.site.register(Client, ClientAdmin)