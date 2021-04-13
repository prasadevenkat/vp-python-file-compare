#import pandas as pd

#import numpy as np

import filecmp as filecmp

unwanted_columns = ['Rep','Units']
wanted_columns = [i for i in range(10) if i not in unwanted_columns ]

#dffeb = pd.read_excel('files/Feb_Report.xlsx',usecols=lambda x: unwanted_columns not in x)

#dffeb = pd.read_excel('files/Feb_Report.xlsx',usecols=lambda x: x not in unwanted_columns)

#dfmar = pd.read_excel('files/Mar_Report.xlsx', usecols=lambda x: unwanted_columns not in x)
#dfmar = pd.read_excel('files/Mar_Report.xlsx', usecols=lambda x: x not in unwanted_columns)
#print(dffeb.equals(dfmar))
#print(dffeb)

#comparevalues = dffeb.values == dfmar.values

#print(comparevalues)

compareOutput = filecmp.cmp('files/Feb_Report.xlsx', 'files/Apr_Report.xlsx', shallow=False)

compareOutput = filecmp
print( compareOutput)

#rows,cols = np.where(comparevalues==False)

#for item in zip(rows,cols):
 #   dffeb.iloc[item[0],item[1]] = ' {} --> {} '.format(dffeb.iloc[item[0], item[1]], dfmar.iloc[item[0],item[1]])


#dffeb.to_excel('files/output.xlsx', index=False,header=True)
