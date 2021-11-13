import codecs
import falcon
from infraestructura.persistencia_usuario import PersistenciaUsuario

from dominio.Usuario import Usuario


class RedSocialController():
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open("C:/Users/Javier/PycharmProjects/RedSocial/controlador/index.html", 'rb') as f:
            resp.body = f.read()

    def on_post(self, req, resp):
        cuenta = Usuario(**req.media)
        if cuenta.guardar() is None:
            resp.status = falcon.HTTP_200
            resp.content_type = 'text/html'
            with open("C:/Users/Javier/PycharmProjects/RedSocial/controlador/falloRegistro.html", 'rb') as f:
                resp.body = f.read()
        else:
            resp.status = falcon.HTTP_200
            resp.content_type = 'text/html'
            with open("C:/Users/Javier/PycharmProjects/RedSocial/controlador/correctoRegistro.html", 'rb') as f:
                resp.body = f.read()

    def on_put(self, req, resp, id):
        cuenta_repositorio = PersistenciaUsuario()
        usuario = cuenta_repositorio.cargar(id)
        usuario.update(req.media)
        usuario.id = id
        usuario.guardar()
        resp.body = usuario.__dict__

    def on_delete(self):
        pass
