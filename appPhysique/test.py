import time
import datetime
from fonctions import unixconv

print("Date (DD/MM/YYYY): ")
date_0 = input()
date_1 = f"{str(int(date_0[0:2]) + 1)}/{date_0[3:5]}/{date_0[6:10]}"
print(date_1)
start = datetime.datetime.utcfromtimestamp(unixconv(date_0))
end = datetime.datetime.utcfromtimestamp(unixconv(date_1))
print(start)
print(end)
