from datetime import datetime, timedelta

date_str = input()
date = datetime.strptime(date_str, "%d-%m-%Y")

start_of_week = date - timedelta(days=date.weekday())

start_of_week_str = start_of_week.strftime("%d-%m-%Y")
print( start_of_week_str)