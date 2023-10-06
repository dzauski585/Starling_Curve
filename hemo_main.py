import patient_equations as eq

import plotly.express as px

age = 30
weight = 70
height = 170
h0 = 30
hf= 22
gender = "m"
sbp = 120
dbp = 80
cvp = 6
svr = 1000
co =5
bsa = 1.85
hr = 80
SaO2 = 99
SvO2 = 70
hgb = 14
    


print(eq.co_fick_calc(age, bsa, SaO2, SvO2, hgb))

df = {...}

starling = px.line(df, x="...", y="...", title='Starling Curve')
starling.show()


