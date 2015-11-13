

__BASEDIR__ = 'C:/temp/'

DB = 'default'

db_prefix = 'TLR_ETL_'

QUERY_ORDER = {0: 'population',
               1: 'pcd',
               2: 'careplans',
               3: 'acr',
               4: 'egfr',
               5: 'hba1c',
               6: 'sysbp',
               7: 'diabp',
               8: 'bmi',
               9: 'tchol',
               10: 'ldl',
               11: 'cvra',
               12: 'smoking',
               13: 'drugs',
               14: 'mbs',
               15: 'pcdreview',
               16: 'caseconference'}

CSVMap = {'population': 'csvPopulation',
          'pcd': 'csvPCD',
          'careplans': 'csvCareplan',
          'acr': 'csvACR',
          'egfr': 'csvEGFR',
          'hba1c': 'csvHBA1C',
          'sysbp': 'csvSysBP',
          'diabp': 'csvDiaBP',
          'bmi': 'csvBMI',
          'tchol': 'csvTchol',
          'ldl': 'csvLDL',
          'cvra': 'csvCVRa',
          'smoking': 'csvSmoking',
          'drugs': 'csvDrugs',
          'mbs': 'csvMBS',
          'pcdreview': 'csvPCDReview',
          'caseconference': 'csvCaseConference'}

resTables = ['acr',
             'egfr',
             'hba1c',
             'sysbp',
             'diabp',
             'bmi',
             'tchol',
             'ldl',
             'cvra',
             'smoking',
             'caseconference']