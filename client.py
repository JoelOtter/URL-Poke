import sys
import socket
import httplib

args = sys.argv

if (len(args) < 3):
    print "Error. Need arguments: [ip] [url]"
else:
    ip = args[1]
    url = args[2]
    headers = {"link": url}
    content = "URL-Poke!"

    try:
        conn = httplib.HTTPConnection(ip + ":2144")
        conn.request("POST", "", content, headers)
        resp = conn.getresponse()
        conn.close()
        msg = resp.getheader('msg')
        print msg
    except socket.error:
        print "Couldn't connect, sorry."