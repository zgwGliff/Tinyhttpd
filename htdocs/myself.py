#!/usr/bin/python

import cgi

form = cgi.FieldStorage()

print "Content-type:text/html\n\n"

print "<body>welcome<br>"


print form["key"].value

print "</body>"