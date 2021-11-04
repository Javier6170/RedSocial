import codecs

import falcon


class RedSocialController():
    def on_get(self, req, resp):
        print("hola")
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open("C:/Users/Javier/PycharmProjects/RedSocial/controlador/index.html", 'rb') as f:
            resp.body = f.read()

