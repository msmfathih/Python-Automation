from datetime import datetime

date_string = "Feb 20 2020  5:20PM"
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(datetime_object)

