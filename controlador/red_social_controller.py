import falcon


class RedSocialController():
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_OK
        resp.content_type = 'text/html'
        with open('../pagination/index.html', 'r') as f:
            resp.body = f.read()

