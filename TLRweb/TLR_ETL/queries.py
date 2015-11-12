
# Queries for extratin data from temp DB...

SELECT_ALL = """
SELECT DISTINCT
       DjangoTLR_csvpopulation.[Usual_Clinic_Name],
       DjangoTLR_csvpopulation.[HRN],       
       DjangoTLR_csvpopulation.[Current_Age_years],     
       DjangoTLR_csvpopulation.[sex],
       DjangoTLR_csvpopulation.[Indigenous_Status_Desc],
       DjangoTLR_csvcareplan.[Care_Plan_Desc], 
       DjangoTLR_csvcareplan.[Latest_CarePlan_Activate_Date],
       
       CSV715.[Start_Date] AS MBS715_Date,
       CSV715.[MBS_Billing_Item_Number] as MBS715,
       CSV721.[Start_Date] AS MBS721_Date,
       CSV721.[MBS_Billing_Item_Number] as MBS721,
       CSV723.[Start_Date] AS MBS723_Date,
       CSV723.[MBS_Billing_Item_Number] as MBS723,
       CSV732.[Start_Date] AS MBS732_Date,
       CSV732.[MBS_Billing_Item_Number] as MBS732,
       
       DjangoTLR_csvcvra.[Result_Date] AS CVRa_Date,       
       DjangoTLR_csvcvra.[Result_Desc] AS CVRa_Status,
       DjangoTLR_csvpcd.[Problem_Status_Date],      
       DjangoTLR_csvpcd.[Term_Description],      
       DjangoTLR_csvpcd.[Problem_Status],
       DjangoTLR_csvcaseconference.[Result_Date] AS RenalCC_Date,
       DjangoTLR_csvcaseconference.[Result_Component] AS RenalCC_Res,
       CSVASPIRIN.[Medication] AS CSVAspirinMedication,
       CSVANTIHT.[Medication] AS CSVAntiHTMedication,
       CSVACR.[Result_Component] AS CSVACRResultsComp,             
       CSVACR.[Result_Measure] AS CSVACRResultsMeasure,       
       CSVACR.[Result_Date] AS CSVACRResultsDate,       
       CSVBMI.[Result_Component] AS CSVBMIResultsComp,             
       CSVBMI.[Result_Measure] AS CSVBMIResultsMeasure,       
       CSVBMI.[Result_Date] AS CSVBMIResultsDate,        
       CSVDIABP.[Result_Component] AS CSVDIABPResultsComp,             
       CSVDIABP.[Result_Measure] AS CSVDIABPResultsMeasure,       
       CSVDIABP.[Result_Date] AS CSVDIABPResultsDate,  
       CSVSYSBP.[Result_Component] AS CSVSYSBPResultsComp,             
       CSVSYSBP.[Result_Measure] AS CSVSYSBPResultsMeasure,       
       CSVSYSBP.[Result_Date] AS CSVSYSBPResultsDate,      
       CSVEGFR.[Result_Component] AS CSVEGFRResultsComp,             
       CSVEGFR.[Result_Measure] AS CSVEGFRResultsMeasure,       
       CSVEGFR.[Result_Date] AS CSVEGFRResultsDate,       
       CSVHBA1C.[Result_Component] AS CSVHBA1CResultsComp,             
       CSVHBA1C.[Result_Measure] AS CSVHBA1CResultsMeasure,       
       CSVHBA1C.[Result_Date] AS CSVHBA1CResultsDate,       
       CSVLDL.[Result_Component] AS CSVLDLResultsComp,             
       CSVLDL.[Result_Measure] AS CSVLDLResultsMeasure,       
       CSVLDL.[Result_Date] AS CSVLDLResultsDate,       
       CSVSMOKE.[Result_Component] AS CSVSMOKEResultsComp,             
       CSVSMOKE.[Result_Desc] AS CSVSMOKEResultsDesc,       
       CSVSMOKE.[Result_Date] AS CSVSMOKEResultsDate,       
       CSVTCHOL.[Result_Component] AS CSVTCHOLResultsComp,             
       CSVTCHOL.[Result_Measure] AS CSVTCHOLResultsMeasure,       
       CSVTCHOL.[Result_Date] AS CSVTCHOLResultsDate      
FROM
       DjangoTLR_csvpopulation,
       DjangoTLR_csvcareplan,
       DjangoTLR_csvmbs,
       (SELECT DISTINCT
               DjangoTLR_csvmbs.[Start_Date],      
               DjangoTLR_csvmbs.[MBS_Billing_Item_Number]
        FROM DjangoTLR_csvmbs
        WHERE DjangoTLR_csvmbs.[MBS_Billing_Item_Number] = '715'
        ORDER BY DjangoTLR_csvmbs.[Start_Date] DESC
        LIMIT 1 ) as CSV715,
       (SELECT DISTINCT
               DjangoTLR_csvmbs.[Start_Date],      
               DjangoTLR_csvmbs.[MBS_Billing_Item_Number]
        FROM DjangoTLR_csvmbs
        WHERE DjangoTLR_csvmbs.[MBS_Billing_Item_Number] = '721'
        ORDER BY DjangoTLR_csvmbs.[Start_Date] DESC
        LIMIT 1 ) as CSV721,
       (SELECT DISTINCT
               DjangoTLR_csvmbs.[Start_Date],      
               DjangoTLR_csvmbs.[MBS_Billing_Item_Number]
        FROM DjangoTLR_csvmbs
        WHERE DjangoTLR_csvmbs.[MBS_Billing_Item_Number] = '723'
        ORDER BY DjangoTLR_csvmbs.[Start_Date] DESC
        LIMIT 1 ) as CSV723,
       (SELECT DISTINCT
               DjangoTLR_csvmbs.[Start_Date],      
               DjangoTLR_csvmbs.[MBS_Billing_Item_Number]
        FROM DjangoTLR_csvmbs
        WHERE DjangoTLR_csvmbs.[MBS_Billing_Item_Number] = '732'
        ORDER BY DjangoTLR_csvmbs.[Start_Date] DESC
        LIMIT 1 ) as CSV732,
       DjangoTLR_csvcvra,
       DjangoTLR_csvpcd,
       DjangoTLR_csvcaseconference,
      (SELECT DISTINCT
               DjangoTLR_csvdrugs.[HRN],
               DjangoTLR_csvdrugs.[Medication]
       FROM DjangoTLR_csvdrugs
       WHERE DjangoTLR_csvdrugs.[Medication] IN ('Aspirin (100mg)')
        LIMIT 1) as CSVASPIRIN,
        
       (SELECT DISTINCT
               DjangoTLR_csvacr.[Usual_Clinic_Name],       
               DjangoTLR_csvacr.[HRN],       
               DjangoTLR_csvacr.[Result_Component],       
               DjangoTLR_csvacr.[Result_Desc],       
               DjangoTLR_csvacr.[Result_Measure],       
               DjangoTLR_csvacr.[Result_Date]       
        FROM
               DjangoTLR_csvacr) AS CSVACR,        
        (SELECT DISTINCT
               DjangoTLR_csvbmi.[Usual_Clinic_Name],       
               DjangoTLR_csvbmi.[HRN],       
               DjangoTLR_csvbmi.[Result_Component],       
               DjangoTLR_csvbmi.[Result_Desc],       
               DjangoTLR_csvbmi.[Result_Measure],       
               DjangoTLR_csvbmi.[Result_Date]       
        FROM
               DjangoTLR_csvbmi) AS CSVBMI,       
        (SELECT DISTINCT
               DjangoTLR_csvdiabp.[Usual_Clinic_Name],       
               DjangoTLR_csvdiabp.[HRN],       
               DjangoTLR_csvdiabp.[Result_Component],       
               DjangoTLR_csvdiabp.[Result_Desc],       
               DjangoTLR_csvdiabp.[Result_Measure],       
               DjangoTLR_csvdiabp.[Result_Date]       
        FROM
               DjangoTLR_csvdiabp) AS CSVDIABP,      
        (SELECT DISTINCT
               DjangoTLR_csvegfr.[Usual_Clinic_Name],       
               DjangoTLR_csvegfr.[HRN],       
               DjangoTLR_csvegfr.[Result_Component],       
               DjangoTLR_csvegfr.[Result_Desc],       
               DjangoTLR_csvegfr.[Result_Measure],       
               DjangoTLR_csvegfr.[Result_Date]       
        FROM
               DjangoTLR_csvegfr) AS CSVEGFR,      
        (SELECT DISTINCT
               DjangoTLR_csvhba1c.[Usual_Clinic_Name],       
               DjangoTLR_csvhba1c.[HRN],       
               DjangoTLR_csvhba1c.[Result_Component],       
               DjangoTLR_csvhba1c.[Result_Desc],       
               DjangoTLR_csvhba1c.[Result_Measure],       
               DjangoTLR_csvhba1c.[Result_Date]       
        FROM
               DjangoTLR_csvhba1c) AS CSVHBA1C,          
        (SELECT DISTINCT
               DjangoTLR_csvldl.[Usual_Clinic_Name],       
               DjangoTLR_csvldl.[HRN],       
               DjangoTLR_csvldl.[Result_Component],       
               DjangoTLR_csvldl.[Result_Desc],       
               DjangoTLR_csvldl.[Result_Measure],       
               DjangoTLR_csvldl.[Result_Date]       
        FROM
               DjangoTLR_csvldl) AS CSVLDL,  
        (SELECT DISTINCT
               DjangoTLR_csvsmoking.[Usual_Clinic_Name],       
               DjangoTLR_csvsmoking.[HRN],       
               DjangoTLR_csvsmoking.[Result_Component],       
               DjangoTLR_csvsmoking.[Result_Desc],       
               DjangoTLR_csvsmoking.[Result_Measure],       
               DjangoTLR_csvsmoking.[Result_Date]       
        FROM
               DjangoTLR_csvsmoking) AS CSVSMOKE,           
        (SELECT DISTINCT
               DjangoTLR_csvsysbp.[Usual_Clinic_Name],       
               DjangoTLR_csvsysbp.[HRN],       
               DjangoTLR_csvsysbp.[Result_Component],       
               DjangoTLR_csvsysbp.[Result_Desc],       
               DjangoTLR_csvsysbp.[Result_Measure],       
               DjangoTLR_csvsysbp.[Result_Date]       
        FROM
               DjangoTLR_csvsysbp) AS CSVSYSBP,            
        (SELECT DISTINCT
               DjangoTLR_csvtchol.[Usual_Clinic_Name],       
               DjangoTLR_csvtchol.[HRN],       
               DjangoTLR_csvtchol.[Result_Component],       
               DjangoTLR_csvtchol.[Result_Desc],       
               DjangoTLR_csvtchol.[Result_Measure],       
               DjangoTLR_csvtchol.[Result_Date]       
        FROM
               DjangoTLR_csvtchol) AS CSVTCHOL

WHERE

       
       DjangoTLR_csvpopulation.[HRN] = DjangoTLR_csvcareplan.[HRN]       
       AND
       DjangoTLR_csvpopulation.[HRN] = DjangoTLR_csvmbs.[HRN]
       AND
       DjangoTLR_csvpopulation.[HRN] = DjangoTLR_csvcvra.[HRN]
       AND
       DjangoTLR_csvpopulation.[HRN] = DjangoTLR_csvpcd.[HRN]
       AND
       DjangoTLR_csvpopulation.[HRN] = DjangoTLR_csvcaseconference.[HRN]
       AND
       DjangoTLR_csvpopulation.[HRN] = DjangoTLR_csvdrugs.[HRN]
       AND
       DjangoTLR_csvpopulation.[HRN] = CSVACR.[HRN]
       AND
       DjangoTLR_csvpopulation.[HRN] = CSVBMI.[HRN]       
       AND
       DjangoTLR_csvpopulation.[HRN] = CSVDIABP.[HRN]       
       AND
       DjangoTLR_csvpopulation.[HRN] = CSVEGFR.[HRN]       
       AND
       DjangoTLR_csvpopulation.[HRN] = CSVHBA1C.[HRN]       
       AND
       DjangoTLR_csvpopulation.[HRN] = CSVLDL.[HRN]       
       AND
       DjangoTLR_csvpopulation.[HRN] = CSVSMOKE.[HRN]       
       AND
       DjangoTLR_csvpopulation.[HRN] = CSVSYSBP.[HRN]       
       AND
       DjangoTLR_csvpopulation.[HRN] = CSVTCHOL.[HRN]
       AND
       DjangoTLR_csvpcd.[Problem_Status] = 'Confirmed'

ORDER BY

       DjangoTLR_csvpopulation.Usual_Clinic_Name
       
"""



"""
DjangoTLR_csvcareplan.[Care_Plan_Desc] = "*Adult Health Check"               
AND          
DjangoTLR_csvcareplan.[Rank_by_Careplan_Activate_Date] = 1
AND
DjangoTLR_csvcareplan.[Care_Plan_Deactivate_Date] = ""

AND

DjangoTLR_csvmbs.[MBS_Billing_Item_Number] IN (715,721,723,732)
       
AND

DjangoTLR_csvpcd.[Rank_by_Problem_Status_Date] = 1      
AND      
DjangoTLR_csvpcd.[Latest_Problem_Status_Date] = DjangoTLR_csvpcd.[Problem_Status_Date]

AND

DjangoTLR_csvcaseconference.[RANK_Result_Date_DESC] = 1       
AND       
DjangoTLR_csvcaseconference.[Result_Component] = "CASE CONF. TYPE : RENAL"
       
AND

"""




SELECT_POP = """
SELECT DISTINCT
       DjangoTLR_csvpopulation.Usual_Clinic_Name,
       DjangoTLR_csvpopulation.HRN,       
       DjangoTLR_csvpopulation.Current_Age_years,     
       DjangoTLR_csvpopulation.sex,
       DjangoTLR_csvpopulation.Indigenous_Status_Desc       
FROM
       DjangoTLR_csvpopulation       

ORDER BY 
       DjangoTLR_csvpopulation.Usual_Clinic_Name ASC
"""


SELECT_CP = """
SELECT DISTINCT
       DjangoTLR_csvcareplan.[Usual_Clinic_Name],
       DjangoTLR_csvcareplan.[HRN],
       DjangoTLR_csvcareplan.[Care_Plan_Desc], 
       DjangoTLR_csvcareplan.[Latest_CarePlan_Activate_Date]
FROM        
       DjangoTLR_csvcareplan
WHERE
       DjangoTLR_csvcareplan.[Care_Plan_Desc] = "*Adult Health Check"               
       AND          
       DjangoTLR_csvcareplan.[Rank_by_Careplan_Activate_Date] = 1
       AND
       DjangoTLR_csvcareplan.[Care_Plan_Deactivate_Date] = ""
ORDER BY        
       DjangoTLR_csvcareplan.[Usual_Clinic_Name] ASC
"""


SELECT_715 = """
SELECT DISTINCT
      DjangoTLR_csvmbs.[Usual_Clinic_Name],      
      DjangoTLR_csvmbs.[HRN],      
      DjangoTLR_csvmbs.[sex],      
      DjangoTLR_csvmbs.[Start_Date],      
      DjangoTLR_csvmbs.[MBS_Billing_Item_Number]      
FROM
      DjangoTLR_csvmbs      
WHERE
      DjangoTLR_csvmbs.[MBS_Billing_Item_Number] = 715
ORDER BY        
      DjangoTLR_csvmbs.[Usual_Clinic_Name] ASC
"""


SELECT_721 = """
SELECT DISTINCT
      DjangoTLR_csvmbs.[Usual_Clinic_Name],      
      DjangoTLR_csvmbs.[HRN],      
      DjangoTLR_csvmbs.[sex],      
      DjangoTLR_csvmbs.[Start_Date],      
      DjangoTLR_csvmbs.[MBS_Billing_Item_Number]      
FROM
      DjangoTLR_csvmbs      
WHERE
      DjangoTLR_csvmbs.[MBS_Billing_Item_Number] = 721
ORDER BY        
      DjangoTLR_csvmbs.[Usual_Clinic_Name] ASC
"""


SELECT_723 = """
SELECT DISTINCT
      DjangoTLR_csvmbs.[Usual_Clinic_Name],      
      DjangoTLR_csvmbs.[HRN],      
      DjangoTLR_csvmbs.[sex],      
      DjangoTLR_csvmbs.[Start_Date],      
      DjangoTLR_csvmbs.[MBS_Billing_Item_Number]      
FROM
      DjangoTLR_csvmbs      
WHERE
      DjangoTLR_csvmbs.[MBS_Billing_Item_Number] = 723
ORDER BY        
      DjangoTLR_csvmbs.[Usual_Clinic_Name] ASC
"""


SELECT_732 = """
SELECT DISTINCT
      DjangoTLR_csvmbs.[Usual_Clinic_Name],      
      DjangoTLR_csvmbs.[HRN],      
      DjangoTLR_csvmbs.[sex],      
      DjangoTLR_csvmbs.[Start_Date],      
      DjangoTLR_csvmbs.[MBS_Billing_Item_Number]      
FROM
      DjangoTLR_csvmbs      
WHERE
      DjangoTLR_csvmbs.[MBS_Billing_Item_Number] = 732
ORDER BY        
      DjangoTLR_csvmbs.[Usual_Clinic_Name] ASC
"""


SELECT_CVR = """
SELECT DISTINCT
       DjangoTLR_csvcvra.[Usual_Clinic_Name],       
       DjangoTLR_csvcvra.[HRN],       
       DjangoTLR_csvcvra.[Result_Date],       
       DjangoTLR_csvcvra.[Result_Desc]       
FROM
       DjangoTLR_csvcvra
WHERE
       DjangoTLR_csvcvra.[Result_Desc] != ""
ORDER BY
       DjangoTLR_csvcvra.[Usual_Clinic_Name] ASC
"""


SELECT_PCD = """
SELECT DISTINCT
      DjangoTLR_csvpcd.[Usual_Clinic_Name],      
      DjangoTLR_csvpcd.[HRN],      
      DjangoTLR_csvpcd.[Problem_Status_Date],      
      DjangoTLR_csvpcd.[Term_Description],      
      DjangoTLR_csvpcd.[Problem_Status]      
FROM
      DjangoTLR_csvpcd      
WHERE
      DjangoTLR_csvpcd.[Rank_by_Problem_Status_Date] = 1      
      AND      
      DjangoTLR_csvpcd.[Latest_Problem_Status_Date] = DjangoTLR_csvpcd.[Problem_Status_Date]      
ORDER BY
      DjangoTLR_csvpcd.[Usual_Clinic_Name] ASC
"""


SELECT_RCC = """
SELECT DISTINCT
       DjangoTLR_csvcaseconference.[Usual_Clinic_Name],       
       DjangoTLR_csvcaseconference.[HRN],       
       DjangoTLR_csvcaseconference.[Result_Component],     
       DjangoTLR_csvcaseconference.[Result_Date]       
FROM
       DjangoTLR_csvcaseconference       
WHERE
       DjangoTLR_csvcaseconference.[RANK_Result_Date_DESC] = 1       
       AND       
       DjangoTLR_csvcaseconference.[Result_Component] = "CASE CONF. TYPE : RENAL"       
ORDER BY
       DjangoTLR_csvcaseconference.[Usual_Clinic_Name] ASC
"""


SELECT_MED = """
SELECT DISTINCT
       DjangoTLR_csvdrugs.[Usual_Clinic_Name],       
       DjangoTLR_csvdrugs.[HRN],       
       DjangoTLR_csvdrugs.[Medication]       
FROM
       DjangoTLR_csvdrugs       
WHERE
       DjangoTLR_csvdrugs.[Medication] != ""       
ORDER BY
       DjangoTLR_csvdrugs.[Usual_Clinic_Name] ASC
"""


SELECT_RES = """
SELECT DISTINCT
       DjangoTLR_csvacr.[Usual_Clinic_Name],       
       DjangoTLR_csvacr.[HRN],       
       DjangoTLR_csvacr.[Result_Component],       
       DjangoTLR_csvacr.[Result_Desc],       
       DjangoTLR_csvacr.[Result_Measure],       
       DjangoTLR_csvacr.[Result_Date]       
FROM
       DjangoTLR_csvacr       
WHERE
       DjangoTLR_csvacr.[Result_Desc] = DjangoTLR_csvacr.[Result_Measure]         

UNION

SELECT DISTINCT
       DjangoTLR_csvbmi.[Usual_Clinic_Name],       
       DjangoTLR_csvbmi.[HRN],       
       DjangoTLR_csvbmi.[Result_Component],       
       DjangoTLR_csvbmi.[Result_Desc],       
       DjangoTLR_csvbmi.[Result_Measure],       
       DjangoTLR_csvbmi.[Result_Date]       
FROM
       DjangoTLR_csvbmi       
WHERE
       DjangoTLR_csvbmi.[Result_Desc] = DjangoTLR_csvbmi.[Result_Measure]         

UNION

SELECT DISTINCT
       DjangoTLR_csvdiabp.[Usual_Clinic_Name],       
       DjangoTLR_csvdiabp.[HRN],       
       DjangoTLR_csvdiabp.[Result_Component],       
       DjangoTLR_csvdiabp.[Result_Desc],       
       DjangoTLR_csvdiabp.[Result_Measure],       
       DjangoTLR_csvdiabp.[Result_Date]       
FROM
       DjangoTLR_csvdiabp       
WHERE
       DjangoTLR_csvdiabp.[Result_Desc] = DjangoTLR_csvdiabp.[Result_Measure]            

UNION

SELECT DISTINCT
       DjangoTLR_csvegfr.[Usual_Clinic_Name],       
       DjangoTLR_csvegfr.[HRN],       
       DjangoTLR_csvegfr.[Result_Component],       
       DjangoTLR_csvegfr.[Result_Desc],       
       DjangoTLR_csvegfr.[Result_Measure],       
       DjangoTLR_csvegfr.[Result_Date]       
FROM
       DjangoTLR_csvegfr       
WHERE
       DjangoTLR_csvegfr.[Result_Desc] = DjangoTLR_csvegfr.[Result_Measure]         

UNION

SELECT DISTINCT
       DjangoTLR_csvhba1c.[Usual_Clinic_Name],       
       DjangoTLR_csvhba1c.[HRN],       
       DjangoTLR_csvhba1c.[Result_Component],       
       DjangoTLR_csvhba1c.[Result_Desc],       
       DjangoTLR_csvhba1c.[Result_Measure],       
       DjangoTLR_csvhba1c.[Result_Date]       
FROM
       DjangoTLR_csvhba1c       
WHERE
       DjangoTLR_csvhba1c.[Result_Desc] = DjangoTLR_csvhba1c.[Result_Measure]           

UNION

SELECT DISTINCT
       DjangoTLR_csvldl.[Usual_Clinic_Name],       
       DjangoTLR_csvldl.[HRN],       
       DjangoTLR_csvldl.[Result_Component],       
       DjangoTLR_csvldl.[Result_Desc],       
       DjangoTLR_csvldl.[Result_Measure],       
       DjangoTLR_csvldl.[Result_Date]       
FROM
       DjangoTLR_csvldl       
WHERE
       DjangoTLR_csvldl.[Result_Desc] = DjangoTLR_csvldl.[Result_Measure]           

UNION

SELECT DISTINCT
       DjangoTLR_csvsmoking.[Usual_Clinic_Name],       
       DjangoTLR_csvsmoking.[HRN],       
       DjangoTLR_csvsmoking.[Result_Component],       
       DjangoTLR_csvsmoking.[Result_Desc],       
       DjangoTLR_csvsmoking.[Result_Measure],       
       DjangoTLR_csvsmoking.[Result_Date]       
FROM
       DjangoTLR_csvsmoking       
WHERE
       DjangoTLR_csvsmoking.[Result_Desc] = DjangoTLR_csvsmoking.[Result_Measure]           

UNION

SELECT DISTINCT
       DjangoTLR_csvsysbp.[Usual_Clinic_Name],       
       DjangoTLR_csvsysbp.[HRN],       
       DjangoTLR_csvsysbp.[Result_Component],       
       DjangoTLR_csvsysbp.[Result_Desc],       
       DjangoTLR_csvsysbp.[Result_Measure],       
       DjangoTLR_csvsysbp.[Result_Date]       
FROM
       DjangoTLR_csvsysbp       
WHERE
       DjangoTLR_csvsysbp.[Result_Desc] = DjangoTLR_csvsysbp.[Result_Measure]            

UNION

SELECT DISTINCT
       DjangoTLR_csvtchol.[Usual_Clinic_Name],       
       DjangoTLR_csvtchol.[HRN],       
       DjangoTLR_csvtchol.[Result_Component],       
       DjangoTLR_csvtchol.[Result_Desc],       
       DjangoTLR_csvtchol.[Result_Measure],       
       DjangoTLR_csvtchol.[Result_Date]       
FROM
       DjangoTLR_csvtchol       
WHERE
       DjangoTLR_csvtchol.[Result_Desc] = DjangoTLR_csvtchol.[Result_Measure]
     
ORDER BY
       [Usual_Clinic_Name] ASC
"""


QUERIES = [
    SELECT_POP,
    SELECT_CP,
    SELECT_715,
    SELECT_721,
    SELECT_723,
    SELECT_732,
    SELECT_CVR,
    SELECT_PCD,
    SELECT_RCC,
    SELECT_MED,
    SELECT_RES
]