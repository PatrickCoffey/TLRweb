# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hrn', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50, choices=[(b'm', b'Male'), (b'f', b'Female'), (b'u', b'Unknown'), (b'o', b'Other')])),
                ('ethnicity', models.CharField(max_length=50, choices=[(b'a', b'ATSI'), (b'n', b'Non-ATSI')])),
                ('AHCP', models.BooleanField(default=False)),
                ('AHCDate', models.DateTimeField()),
                ('PCDP', models.BooleanField(default=False)),
                ('PCDDate', models.DateTimeField()),
                ('RHDP', models.BooleanField(default=False)),
                ('RHDDate', models.DateTimeField()),
                ('planMonth', models.IntegerField()),
                ('mbs715', models.DateTimeField()),
                ('mbs721', models.DateTimeField()),
                ('mbs723', models.DateTimeField()),
                ('mbs732', models.DateTimeField()),
                ('revMonth', models.IntegerField()),
                ('CVRStatus', models.CharField(max_length=50)),
                ('CVRDate', models.DateTimeField()),
                ('eligiblePCD', models.BooleanField(default=False)),
                ('diabetes', models.BooleanField(default=False)),
                ('cvd', models.BooleanField(default=False)),
                ('hiCVR', models.BooleanField(default=False)),
                ('rhd', models.BooleanField(default=False)),
                ('lung', models.BooleanField(default=False)),
                ('renal', models.BooleanField(default=False)),
                ('missedDiabetes', models.BooleanField(default=False)),
                ('missedCKD', models.BooleanField(default=False)),
                ('renalCC', models.DateTimeField()),
                ('asprin', models.BooleanField(default=False)),
                ('antiHT', models.BooleanField(default=False)),
                ('ACE', models.BooleanField(default=False)),
                ('ARB', models.BooleanField(default=False)),
                ('statin', models.BooleanField(default=False)),
                ('metformin', models.BooleanField(default=False)),
                ('sulfonurics', models.BooleanField(default=False)),
                ('insulin', models.BooleanField(default=False)),
                ('gliptin', models.BooleanField(default=False)),
                ('otherDiabetes', models.BooleanField(default=False)),
                ('bmi', models.FloatField()),
                ('sysBP', models.IntegerField()),
                ('diaBP', models.IntegerField()),
                ('tChol', models.FloatField()),
                ('ldl', models.FloatField()),
                ('hba1c', models.FloatField()),
                ('acr', models.FloatField()),
                ('egfr', models.IntegerField()),
                ('smoking', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CommunityAliases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alias', models.CharField(max_length=150)),
                ('community', models.ForeignKey(to='TLR_ETL.Community')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='csvACR',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Usual_Clinic_Name', models.CharField(max_length=150, blank=True)),
                ('HRN', models.IntegerField(blank=True)),
                ('Result_Measure', models.CharField(max_length=150, blank=True)),
                ('Result_Component', models.CharField(max_length=150, blank=True)),
                ('Result_Desc', models.CharField(max_length=150, blank=True)),
                ('RANK_Result_Date_DESC', models.IntegerField(max_length=1)),
                ('Result_Date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='csvBMI',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Usual_Clinic_Name', models.CharField(max_length=150, blank=True)),
                ('HRN', models.IntegerField(blank=True)),
                ('Result_Measure', models.CharField(max_length=150, blank=True)),
                ('Result_Component', models.CharField(max_length=150, blank=True)),
                ('Result_Desc', models.CharField(max_length=150, blank=True)),
                ('RANK_Result_Date_DESC', models.IntegerField(max_length=1)),
                ('Result_Date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='csvCareplan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Usual_Clinic_Name', models.CharField(max_length=150, blank=True)),
                ('HRN', models.IntegerField(blank=True)),
                ('sex', models.CharField(max_length=50, blank=True)),
                ('Latest_CarePlan_Activate_Date', models.DateTimeField()),
                ('Care_Plan_Deactivate_Date', models.DateTimeField()),
                ('Care_Plan_Desc', models.CharField(max_length=150, blank=True)),
                ('Rank_by_Careplan_Activate_Date', models.IntegerField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='csvCaseConference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Usual_Clinic_Name', models.CharField(max_length=150, blank=True)),
                ('HRN', models.IntegerField(blank=True)),
                ('Result_Component', models.CharField(max_length=150, blank=True)),
                ('Result_Desc', models.CharField(max_length=150, blank=True)),
                ('RANK_Result_Date_DESC', models.IntegerField(max_length=1)),
                ('Result_Date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='csvCVRa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Usual_Clinic_Name', models.CharField(max_length=150, blank=True)),
                ('HRN', models.IntegerField(blank=True)),
                ('Result_Measure', models.CharField(max_length=150, blank=True)),
                ('Result_Component', models.CharField(max_length=150, blank=True)),
                ('Result_Desc', models.CharField(max_length=150, blank=True)),
                ('RANK_Result_Date_DESC', models.IntegerField(max_length=1)),
                ('Result_Date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='csvDiaBP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Usual_Clinic_Name', models.CharField(max_length=150, blank=True)),
                ('HRN', models.IntegerField(blank=True)),
                ('Result_Measure', models.CharField(max_length=150, blank=True)),
                ('Result_Component', models.CharField(max_length=150, blank=True)),
                ('Result_Desc', models.CharField(max_length=150, blank=True)),
                ('RANK_Result_Date_DESC', models.IntegerField(max_length=1)),
                ('Result_Date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='csvDrugs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Usual_Clinic_Name', models.CharField(max_length=150, blank=True)),
                ('HRN', models.IntegerField(blank=True)),
                ('Medication', models.CharField(max_length=150, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='csvEGFR',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Usual_Clinic_Name', models.CharField(max_length=150, blank=True)),
                ('HRN', models.IntegerField(blank=True)),
                ('Result_Measure', models.CharField(max_length=150, blank=True)),
                ('Result_Component', models.CharField(max_length=150, blank=True)),
                ('Result_Desc', models.CharField(max_length=150, blank=True)),
                ('RANK_Result_Date_DESC', models.IntegerField(max_length=1)),
                ('Result_Date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='csvHBA1C',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Usual_Clinic_Name', models.CharField(max_length=150, blank=True)),
                ('HRN', models.IntegerField(blank=True)),
                ('Result_Measure', models.CharField(max_length=150, blank=True)),
                ('Result_Component', models.CharField(max_length=150, blank=True)),
                ('Result_Desc', models.CharField(max_length=150, blank=True)),
                ('RANK_Result_Date_DESC', models.IntegerField(max_length=1)),
                ('Result_Date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='csvLDL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Usual_Clinic_Name', models.CharField(max_length=150, blank=True)),
                ('HRN', models.IntegerField(blank=True)),
                ('Result_Measure', models.CharField(max_length=150, blank=True)),
                ('Result_Component', models.CharField(max_length=150, blank=True)),
                ('Result_Desc', models.CharField(max_length=150, blank=True)),
                ('RANK_Result_Date_DESC', models.IntegerField(max_length=1)),
                ('Result_Date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='csvMBS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Usual_Clinic_Name', models.CharField(max_length=150, blank=True)),
                ('HRN', models.IntegerField(blank=True)),
                ('MBS_Billing_Item_Number', models.IntegerField(max_length=10)),
                ('Start_Date', models.DateTimeField()),
                ('sex', models.CharField(max_length=50, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='csvPCD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Usual_Clinic_Name', models.CharField(max_length=150, blank=True)),
                ('HRN', models.IntegerField(blank=True)),
                ('sex', models.CharField(max_length=50, blank=True)),
                ('Term_Description', models.CharField(max_length=150, blank=True)),
                ('Problem_Status_Date', models.DateTimeField()),
                ('Rank_by_Problem_Status_Date', models.IntegerField(max_length=1)),
                ('Problem_Status', models.CharField(max_length=25)),
                ('Latest_Problem_Status_Date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='csvPCDReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Usual_Clinic_Name', models.CharField(max_length=150, blank=True)),
                ('HRN', models.IntegerField(blank=True)),
                ('Comp_Result_Definition', models.CharField(max_length=150, blank=True)),
                ('sex', models.CharField(max_length=50, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='csvPopulation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Usual_Clinic_Name', models.CharField(max_length=150, blank=True)),
                ('HRN', models.IntegerField(blank=True)),
                ('sex', models.CharField(max_length=50, blank=True)),
                ('Indigenous_Status_Desc', models.CharField(max_length=50, blank=True)),
                ('Current_Age_years', models.IntegerField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='csvSmoking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Usual_Clinic_Name', models.CharField(max_length=150, blank=True)),
                ('HRN', models.IntegerField(blank=True)),
                ('Result_Measure', models.CharField(max_length=150, blank=True)),
                ('Result_Component', models.CharField(max_length=150, blank=True)),
                ('Result_Desc', models.CharField(max_length=150, blank=True)),
                ('RANK_Result_Date_DESC', models.IntegerField(max_length=1)),
                ('Result_Date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='csvSysBP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Usual_Clinic_Name', models.CharField(max_length=150, blank=True)),
                ('HRN', models.IntegerField(blank=True)),
                ('Result_Measure', models.CharField(max_length=150, blank=True)),
                ('Result_Component', models.CharField(max_length=150, blank=True)),
                ('Result_Desc', models.CharField(max_length=150, blank=True)),
                ('RANK_Result_Date_DESC', models.IntegerField(max_length=1)),
                ('Result_Date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='csvTchol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Usual_Clinic_Name', models.CharField(max_length=150, blank=True)),
                ('HRN', models.IntegerField(blank=True)),
                ('Result_Measure', models.CharField(max_length=150, blank=True)),
                ('Result_Component', models.CharField(max_length=150, blank=True)),
                ('Result_Desc', models.CharField(max_length=150, blank=True)),
                ('RANK_Result_Date_DESC', models.IntegerField(max_length=1)),
                ('Result_Date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='client',
            name='community',
            field=models.OneToOneField(to='TLR_ETL.Community'),
            preserve_default=True,
        ),
    ]
