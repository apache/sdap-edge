import tornado.httpclient

class HttpUtility(object):
    def getResponse(self, url, callback, body=None, headers=None):
        requestHeaders = {'Connection': 'close', 'User-Agent': 'Tornado', "Accept": "*"}
        if headers is not None:
            requestHeaders.update(headers)
        if body is not None:
            request = tornado.httpclient.HTTPRequest(url, method='POST', headers=requestHeaders, request_timeout=30, body=body)
        else:
            request = tornado.httpclient.HTTPRequest(url, method='GET', headers=requestHeaders, request_timeout=30)
        httpClient = tornado.httpclient.AsyncHTTPClient()
        httpClient.fetch(request,callback=callback)
