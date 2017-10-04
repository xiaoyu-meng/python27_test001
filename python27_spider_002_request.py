# -*- coding: utf-8 -*-
import urllib2
import urllib

def request_post_debug():
    # POST
    data = {'username':'kamidox','password':'xxxxxxxx'}
    # headers = {'User-Agent':'Mozilla/5.0','Content-Type':'plain/ext'}
    headers = {'User-Agent':'Mozilla/5.0'}
    req = urllib2.Request('http://www.douban.com',data=urllib.urlencode(data),headers=headers)
    opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))
    s = opener.open(req)
    print(s.read(100))
    s.close()





if __name__=='__main__':
    # urlopen()
    request_post_debug()