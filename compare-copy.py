import pandas as pd

import numpy as np

dffeb = pd.read_excel('files/Feb_Report.xlsx'
)

dfmar = pd.read_excel('files/Mar_Report.xlsx'
)

#print(dffeb.equals(dfmar))

comparevalues = dffeb.values == dfmar.values

print(comparevalues)

rows,cols = np.where(comparevalues==False)

for item in zip(rows,cols):
    dffeb.iloc[item[0],item[1]] = ' {} --> {} '.format(dffeb.iloc[item[0], item[1]], dfmar.iloc[item[0],item[1]])


dffeb.to_excel('files/output.xlsx', index=False,header=True)
