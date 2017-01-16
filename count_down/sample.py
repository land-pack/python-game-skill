from datetime import datetime
future = datetime.strptime('2017-1-17 8:13:01','%Y-%m-%d %H:%M:%S')
now = datetime.now()
delta = future - now
hour = delta.seconds/60/60
minute = (delta.seconds - hour*60*60)/60
seconds = delta.seconds - hour*60*60 - minute*60
print delta.days, hour, minute, seconds
