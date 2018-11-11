import threading
from datetime import datetime
import ImageGrab

def printit():
	threading.Timer(900, printit).start()
	img=ImageGrab.grab()
	img.save('d:\Dropbox\Austausch\screenshot.jpg')
  
printit()




