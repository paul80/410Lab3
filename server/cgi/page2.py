#!/usr/bin/env python
import cgi 
form= cgi.FieldStorage()
val1= form.getvalue("name") #val1= form["first"].value
val2= form.getvalue("family")
print "Content-type:text/html"
print
print "<html><head><title>Test URL Encoding</title></head><body>The name is %s <br/> The family is %s."%(val1,val2)

#added stuff here
print """<form method="post" action="page1.py"> Birthdate: <br/> <input type=text/html" name="birthdate"> <br/> 
Main hobby: <br/> <input type="text/html" name="hobby" <br/>
<input type="submit" value="Submit">
</form>"""
print "</body></html>"

