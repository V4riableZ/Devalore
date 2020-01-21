import datetime
import time

while True:
    time.sleep(1)
    now = datetime.datetime.now()
    print("Current date and time : " + now.strftime("%Y-%m-%d %H:%M:%S"))

