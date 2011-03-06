import sys

def makeResponse():
	import urllib2
	from pyquery import PyQuery as pq
	import json

	url="http://www.thisamericanlife.org/contributors/jack-hitt"
	tal_html = urllib2.urlopen(url).read()
	d=pq(tal_html)
	jack_html = d('#content-inner').html()
	jack_json = json.dumps(jack_html)
	return "tal_callback(%s)"%jack_json	


def application(environ,start_response):

	#print >> environ['wsgi.errors'],'error out'
	#print >> environ['wsgi.errors'],sys.path	
	status = '200 OK'
	response_body=makeResponse()

	response_headers=[('Content-Type','text/javascript'),
			('Content-Length',str(len(response_body)))]
	start_response(status,response_headers)
	
	return [response_body]

if __name__=="__main__":
	print makeResponse()
