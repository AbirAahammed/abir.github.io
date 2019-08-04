#!/usr/bin/python
import sys
from os import environ
str = ""
# if (environ.has_key('QUERY_STRING')):
#   str = environ['QUERY_STRING']
queryText = sys.stdin.readline()

print
print """\
<html>
<body>
<h2>Hello World!</h2>
<p>{0}</p>
</body>
</html>
""".format(queryText)
