import urllib2
from pyquery import PyQuery as pq
import json

url="http://www.thisamericanlife.org/contributors/jack-hitt"
tal_html = urllib2.urlopen(url).read()
d=pq(tal_html)
jack_html = d('#content-inner').html()
jack_json = json.dumps(jack_html)

print "content-type:text/javascript"
print ""
print "tal_callback(%s)"%jack_json