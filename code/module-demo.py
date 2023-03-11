# import the "sys" module, which has a good many attributes like platfrom, version ...
import sys
print ("The kernel name of the device is:", sys.platform)
print ("The python version:", sys.version)
# import the os module: system-independent way for your Python code to interact with the underlying operating system

import os
print ("The current directory:", os.getcwd())
print ("The envrionment key and vaule of the os system:", os.environ)
print ("The HOME directory:", os.getenv('HOME'))

import datetime
# the date.today() function of the module datetime is used to offer the date of the present 
print ("Today is:", datetime.date.today())
print ("The isoformat of today's date:" ,datetime.date.isoformat(datetime.date.today()))
# ways to specify the present day, month, and year
print ("The present day is:", datetime.date.today().day)
print ("The present month is:", datetime.date.today().month)
print ("The present year is:", datetime.date.today().year)

import time
# import the time module, the strftime function is used to display the time: %Y = year; %b = month abbreviated name; %d =current date; %H = hour; %M = minute; %A = weekday; %p= AM/PM 
print ("The current time is:", time.strftime ("%Y %b %d %H:%M %A %p"))

import html
# import the html module; see https://docs.python.org/zh-tw/3.7/library/html.html for "escape" and "unescape" function. 
print ("The 'escape' function of HTML fucntion:", html.escape ("This HTML fragment contains a <script>script</script> tag."))
print ("The 'unescape' function of HTML fucntion:", html.unescape (html.unescape("I &hearts; Python's &lt;standard library&gt;.")))