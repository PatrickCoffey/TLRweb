# models.py (the database tables)

from django.db import models
    
    
class Community(models.Model):
    name = models.CharField(max_length=150)
    
    objects = models.Manager()
    
    def __unicode__(self):
        return '%s' % self.name


class CommunityAliases(models.Model):
    community = models.ForeignKey(Community)
    alias = models.CharField(max_length=150)
    
    objects = models.Manager()
    
    def __unicode__(self):
        return '%s' % self.alias    
    
    
class Client(models.Model):
    
    GENDER_CHOICE = (('m', 'Male'),('f', 'Female'), ('u', 'Unknown'), ('o', 'Other'))
    ETHNIC_CHOICE = (('a', 'ATSI'), ('n', 'Non-ATSI'))
    
    hrn = models.IntegerField()
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50, choices=GENDER_CHOICE)
    ethnicity = models.CharField(max_length=50, choices=ETHNIC_CHOICE)
    community = models.OneToOneField(Community)
        
    # CarePlans
    AHCP = models.BooleanField(default=False)
    AHCDate = models.DateTimeField()
    PCDP = models.BooleanField(default=False)
    PCDDate = models.DateTimeField()
    RHDP = models.BooleanField(default=False)
    RHDDate = models.DateTimeField()
    planMonth = models.IntegerField()
    
    # MBS
    mbs715 = models.DateTimeField()
    mbs721 = models.DateTimeField()
    mbs723 = models.DateTimeField()
    mbs732 = models.DateTimeField()
    revMonth = models.IntegerField()
    
    # CVR Status
    CVRStatus = models.CharField(max_length=50)
    CVRDate = models.DateTimeField()
    
    # PCD's
    eligiblePCD = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    cvd = models.BooleanField(default=False)
    hiCVR = models.BooleanField(default=False)
    rhd = models.BooleanField(default=False)
    lung = models.BooleanField(default=False)
    renal = models.BooleanField(default=False)
    
    # Missed PCD's
    missedDiabetes = models.BooleanField(default=False)
    missedCKD = models.BooleanField(default=False)
    
    # Renal CC's
    renalCC = models.DateTimeField()
    
    # Medications
    asprin = models.BooleanField(default=False)
    antiHT = models.BooleanField(default=False)
    ACE = models.BooleanField(default=False)
    ARB = models.BooleanField(default=False)
    statin = models.BooleanField(default=False)
    metformin = models.BooleanField(default=False)
    sulfonurics = models.BooleanField(default=False)
    insulin = models.BooleanField(default=False)
    gliptin = models.BooleanField(default=False)
    otherDiabetes = models.BooleanField(default=False)

    # Results
    bmi = models.FloatField()
    sysBP = models.IntegerField()
    diaBP = models.IntegerField()
    tChol = models.FloatField()
    ldl = models.FloatField()
    hba1c = models.FloatField()
    acr = models.FloatField()
    egfr = models.IntegerField()
    smoking = models.CharField(max_length=50)
    
    objects = models.Manager()
    
    def __unicode__(self):
        return str(self.hrn)

   
class csvPopulation(models.Model):
    """DjangoTLR_csvPopulation (Current_Age_years, HRN, Indigenous_Status_Desc, Usual_Clinic_Name, Sex)"""
    Usual_Clinic_Name = models.CharField(max_length=150, blank=True)
    HRN = models.IntegerField(blank=True)
    sex = models.CharField(max_length=50, blank=True)
    Indigenous_Status_Desc = models.CharField(max_length=50, blank=True)
    Current_Age_years = models.IntegerField(blank=True)
    
    def __unicode__(self):
        return str(self.HRN)
    
  
class csvPCD(models.Model):
    """DjangoTLR_csvPCD (Term_Description, Sex, Problem_Status_Date, HRN, Rank_by_Problem_Status_Date, Usual_Clinic_Name, Problem_Status, Latest_Problem_Status_Date)"""
    Usual_Clinic_Name = models.CharField(max_length=150, blank=True)
    HRN = models.IntegerField(blank=True)
    sex = models.CharField(max_length=50, blank=True)
    Term_Description = models.CharField(max_length=150, blank=True)
    Problem_Status_Date = models.DateTimeField()
    Rank_by_Problem_Status_Date = models.IntegerField(max_length=1)
    Problem_Status = models.CharField(max_length=25)
    Latest_Problem_Status_Date = models.DateTimeField()
    
    def __unicode__(self):
        return str(self.HRN)

    
class csvCareplan(models.Model):
    """DjangoTLR_csvCareplan (HRN, Latest_CarePlan_Activate_Date, Usual_Clinic_Name, Care_Plan_Deactivate_Date, Care_Plan_Desc, Rank_by_Careplan_Activate_Date, Sex)"""
    Usual_Clinic_Name = models.CharField(max_length=150, blank=True)
    HRN = models.IntegerField(blank=True)
    sex = models.CharField(max_length=50, blank=True)
    Latest_CarePlan_Activate_Date = models.DateTimeField()
    Care_Plan_Deactivate_Date = models.DateTimeField()
    Care_Plan_Desc = models.CharField(max_length=150, blank=True)
    Rank_by_Careplan_Activate_Date = models.IntegerField(max_length=1)
    
    def __unicode__(self):
        return str(self.HRN)


class csvACR(models.Model):
    """DjangoTLR_csvACR (Result_Component, HRN, Result_Measure, Usual_Clinic_Name, Result_Desc, RANK_Result_Date_DESC, Result_Date)"""
    Usual_Clinic_Name = models.CharField(max_length=150, blank=True)
    HRN = models.IntegerField(blank=True)
    Result_Measure = models.CharField(max_length=150, blank=True)
    Result_Component = models.CharField(max_length=150, blank=True)
    Result_Desc = models.CharField(max_length=150, blank=True)
    RANK_Result_Date_DESC = models.IntegerField(max_length=1)
    Result_Date = models.DateTimeField()
    
    def __unicode__(self):
        return str(self.HRN)


class csvEGFR(models.Model):
    """DjangoTLR_csvEGFR (Result_Component, HRN, Result_Measure, Usual_Clinic_Name, Result_Desc, RANK_Result_Date_DESC, Result_Date)"""
    Usual_Clinic_Name = models.CharField(max_length=150, blank=True)
    HRN = models.IntegerField(blank=True)
    Result_Measure = models.CharField(max_length=150, blank=True)
    Result_Component = models.CharField(max_length=150, blank=True)
    Result_Desc = models.CharField(max_length=150, blank=True)
    RANK_Result_Date_DESC = models.IntegerField(max_length=1)
    Result_Date = models.DateTimeField()
    
    def __unicode__(self):
        return str(self.HRN)  


class csvHBA1C(models.Model):
    """DjangoTLR_csvHBA1C (Result_Component, HRN, Result_Measure, Usual_Clinic_Name, Result_Desc, RANK_Result_Date_DESC, Result_Date)"""
    Usual_Clinic_Name = models.CharField(max_length=150, blank=True)
    HRN = models.IntegerField(blank=True)
    Result_Measure = models.CharField(max_length=150, blank=True)
    Result_Component = models.CharField(max_length=150, blank=True)
    Result_Desc = models.CharField(max_length=150, blank=True)    
    RANK_Result_Date_DESC = models.IntegerField(max_length=1)
    Result_Date = models.DateTimeField()
    
    def __unicode__(self):
        return str(self.HRN)


class csvSysBP(models.Model):
    """DjangoTLR_csvSysBP (Result_Component, HRN, Result_Measure, Usual_Clinic_Name, Result_Desc, RANK_Result_Date_DESC, Result_Date)"""
    Usual_Clinic_Name = models.CharField(max_length=150, blank=True)
    HRN = models.IntegerField(blank=True)
    Result_Measure = models.CharField(max_length=150, blank=True)
    Result_Component = models.CharField(max_length=150, blank=True)
    Result_Desc = models.CharField(max_length=150, blank=True)   
    RANK_Result_Date_DESC = models.IntegerField(max_length=1)
    Result_Date = models.DateTimeField()
    
    def __unicode__(self):
        return str(self.HRN)


class csvDiaBP(models.Model):
    """DjangoTLR_csvDiaBP (Result_Component, HRN, Result_Measure, Usual_Clinic_Name, Result_Desc, RANK_Result_Date_DESC, Result_Date)"""
    Usual_Clinic_Name = models.CharField(max_length=150, blank=True)
    HRN = models.IntegerField(blank=True)
    Result_Measure = models.CharField(max_length=150, blank=True)
    Result_Component = models.CharField(max_length=150, blank=True)
    Result_Desc = models.CharField(max_length=150, blank=True)    
    RANK_Result_Date_DESC = models.IntegerField(max_length=1)
    Result_Date = models.DateTimeField()
    
    def __unicode__(self):
        return str(self.HRN)


class csvBMI(models.Model):
    """DjangoTLR_csvBMI (Result_Component, HRN, Result_Measure, Usual_Clinic_Name, Result_Desc, RANK_Result_Date_DESC, Result_Date)"""
    Usual_Clinic_Name = models.CharField(max_length=150, blank=True)
    HRN = models.IntegerField(blank=True)
    Result_Measure = models.CharField(max_length=150, blank=True)
    Result_Component = models.CharField(max_length=150, blank=True)
    Result_Desc = models.CharField(max_length=150, blank=True)    
    RANK_Result_Date_DESC = models.IntegerField(max_length=1)
    Result_Date = models.DateTimeField()
    
    def __unicode__(self):
        return str(self.HRN)


class csvTchol(models.Model):
    """DjangoTLR_csvTchol (Result_Component, HRN, Result_Measure, Usual_Clinic_Name, Result_Desc, RANK_Result_Date_DESC, Result_Date)"""
    Usual_Clinic_Name = models.CharField(max_length=150, blank=True)
    HRN = models.IntegerField(blank=True)
    Result_Measure = models.CharField(max_length=150, blank=True)
    Result_Component = models.CharField(max_length=150, blank=True)
    Result_Desc = models.CharField(max_length=150, blank=True)  
    RANK_Result_Date_DESC = models.IntegerField(max_length=1)
    Result_Date = models.DateTimeField()
    
    def __unicode__(self):
        return str(self.HRN)

class csvLDL(models.Model):
    """DjangoTLR_csvLDL (Result_Component, HRN, Result_Measure, Usual_Clinic_Name, Result_Desc, RANK_Result_Date_DESC, Result_Date)"""
    Usual_Clinic_Name = models.CharField(max_length=150, blank=True)
    HRN = models.IntegerField(blank=True)
    Result_Measure = models.CharField(max_length=150, blank=True)
    Result_Component = models.CharField(max_length=150, blank=True)
    Result_Desc = models.CharField(max_length=150, blank=True)    
    RANK_Result_Date_DESC = models.IntegerField(max_length=1)
    Result_Date = models.DateTimeField()
    
    def __unicode__(self):
        return str(self.HRN)


class csvCVRa(models.Model):
    """DjangoTLR_csvCVRa (Result_Component, HRN, Result_Measure, Usual_Clinic_Name, Result_Desc, RANK_Result_Date_DESC, Result_Date)"""
    Usual_Clinic_Name = models.CharField(max_length=150, blank=True)
    HRN = models.IntegerField(blank=True)
    Result_Measure = models.CharField(max_length=150, blank=True)
    Result_Component = models.CharField(max_length=150, blank=True)
    Result_Desc = models.CharField(max_length=150, blank=True)    
    RANK_Result_Date_DESC = models.IntegerField(max_length=1)
    Result_Date = models.DateTimeField()
    
    def __unicode__(self):
        return str(self.HRN)


class csvSmoking(models.Model):
    """DjangoTLR_csvSmoking (Result_Component, HRN, Result_Measure, Usual_Clinic_Name, Result_Desc, RANK_Result_Date_DESC, Result_Date)"""
    Usual_Clinic_Name = models.CharField(max_length=150, blank=True)
    HRN = models.IntegerField(blank=True)
    Result_Measure = models.CharField(max_length=150, blank=True)
    Result_Component = models.CharField(max_length=150, blank=True)
    Result_Desc = models.CharField(max_length=150, blank=True)    
    RANK_Result_Date_DESC = models.IntegerField(max_length=1)
    Result_Date = models.DateTimeField()
    
    def __unicode__(self):
        return str(self.HRN)


class csvDrugs(models.Model):
    """DjangoTLR_csvDrugs (Usual_Clinic_Name, HRN, Medication)"""
    Usual_Clinic_Name = models.CharField(max_length=150, blank=True)
    HRN = models.IntegerField(blank=True)
    Medication = models.CharField(max_length=150, blank=True)
    
    def __unicode__(self):
        return str(self.HRN)


class csvMBS(models.Model):
    """DjangoTLR_csvMBS (Start_Date, HRN, MBS_Billing_Item_Number, Usual_Clinic_Name, Sex)"""
    Usual_Clinic_Name = models.CharField(max_length=150, blank=True)
    HRN = models.IntegerField(blank=True)
    MBS_Billing_Item_Number = models.IntegerField(max_length=10)
    Start_Date = models.DateTimeField()
    sex = models.CharField(max_length=50, blank=True)
    
    def __unicode__(self):
        return str(self.HRN)


class csvPCDReview(models.Model):
    """DjangoTLR_csvPCDReview (Comp_Result_Definition, HRN, Usual_Clinic_Name, Sex)"""
    Usual_Clinic_Name = models.CharField(max_length=150, blank=True)
    HRN = models.IntegerField(blank=True)
    Comp_Result_Definition = models.CharField(max_length=150, blank=True)
    sex = models.CharField(max_length=50, blank=True)
    
    def __unicode__(self):
        return str(self.HRN)


class csvCaseConference(models.Model):
    """DjangoTLR_csvCaseConference (Usual_Clinic_Name, HRN, Result_Component, Result_Date, RANK_Result_Date_DESC, Result_Desc)"""
    Usual_Clinic_Name = models.CharField(max_length=150, blank=True)
    HRN = models.IntegerField(blank=True)
    Result_Component = models.CharField(max_length=150, blank=True)
    Result_Desc = models.CharField(max_length=150, blank=True)    
    RANK_Result_Date_DESC = models.IntegerField(max_length=1)
    Result_Date = models.DateTimeField()
    
    def __unicode__(self):
        return str(self.HRN)