import pandas as pd
from datetime import datetime, timedelta

df=pd.read_excel(r'C:\Users\Spandana SY-int-219\Desktop\PYTHON_TASK\task8.xlsx')
print(df)
#Findout how many employees marked WFH, WFO for today.
today=datetime.today().strftime('%b %d')
today_col=df[today]
wfh_count_today=today_col.eq('WFH').sum()
wfo_count_today=today_col.eq('WFO').sum()

print(f"Emploees on WFH today are: {wfh_count_today}")
print(f"Emploees on WFO today are: {wfo_count_today}")

#Findout how many employees marked WFH, WFO for the previous 5 days from the current date.
five_days_filled = [datetime.today() - timedelta(days=i) for i in range (1,6)]
format_date = [date.strftime('%b %d') for date in five_days_filled]
wfh_count_filled=0
wfo_count_filled=0
print(format_date)

for date in format_date:
    if date in df.columns:
        data=df[date]
        wfh_count_filled += data.eq('WFH').sum()
        wfo_count_filled += data.eq('WFO').sum()
print(f"Employees who marked WFH in the previuos 5 days: {wfh_count_filled}")
print(f"Employees who marked WFO in the previuos 5 days: {wfo_count_filled}")

#Findout employee id who has not filled the attendance in all today and previous 5 days..
valid_columns = [col for col in format_date if col in df.columns]

no_entries = []
for index, row in df.iterrows():
    emp_id=row['Emp ID ']
    no_entries_values=row[valid_columns]
    if no_entries_values.isnull().all():
        no_entries.append(emp_id)
print("Employee ID's who has not entered for previous five days are:")
print(no_entries)

#Print the data like WFH & WFO Count on Current Date.
print(f"WFH Count on {today} : {wfh_count_today}")
print(f"WFO Count on {today} : {wfo_count_today}")
