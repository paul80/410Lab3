#!/usr/bin/env python
import cgi
form= cgi.FieldStorage()
val1= form.getvalue("birthdate") #val1= form["first"].value
val2= form.getvalue("hobby")

print """Content-type:text/html

<form method="post" action="page2.py">
Name: <br/> <input type="text/html" name="name" <br/> 
<br/>Family: <br><input type="text/html" name="family" <br/>
<input type="submit" value="Submit">
</form>"""

print
print "<html><head><title>Test URL Encoding</title></head><body>The birthdate is %s <br/> The hobby is %s."%(val1,val2)




