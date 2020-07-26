import math

from packages.inputs \
    import get_daily_working_hours, \
    get_number_of_resources, \
    get_xls_file_path

from packages.calculation import get_total_working_hrs_by_project
from packages.calculation import get_sheet_sum

default_path = "/home/mahdy/Downloads/MasterBussiness-Timesheet.xlsx"
working_hrs_per_day = 6.5

file_path = get_xls_file_path()
daily_working_hours = get_daily_working_hours()
number_of_resources = get_number_of_resources()
total_spent_hrs = get_total_working_hrs_by_project(file_path)
months_number = get_sheet_sum(file_path)
total_monthly_working_hrs = (daily_working_hours * int(number_of_resources) * 22) * months_number

print(
f"\nTotal Working Hrs on that project: {total_spent_hrs} \n"
+ f"Total Resources Working hrs: {total_monthly_working_hrs}\n"
)

time_usage_percentage = (total_spent_hrs * 100) / float(total_monthly_working_hrs)

print(f"Time Usage: {math.floor(time_usage_percentage)}%")
