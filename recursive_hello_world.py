import threading
from datetime import datetime


def printit():
	x=datetime.today()
	y=x.replace(day=x.day+1, hour=7, minute=0, second=0, microsecond=0)
	delta_t=y-x
	secs=delta_t.seconds+1
	threading.Timer(secs, printit).start()
	print "Hello, World!"
  
printit()