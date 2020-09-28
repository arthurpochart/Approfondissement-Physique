import time
import datetime

def unixconv(date_0):

    t = f"{date_0}"
    timestamp = time.mktime(datetime.datetime.strptime(date_0, "%d/%m/%Y").timetuple())

    return timestamp


