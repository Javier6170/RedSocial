import codecs
import falcon
from infraestructura.persistencia_usuario import PersistenciaUsuario

from dominio.Usuario import Usuario
from dominio.UserInicioSesion import UsuarioInicioSesion


class RedSocialController():
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open("C:/Users/Javier/PycharmProjects/RedSocial/controlador/index.html", 'rb') as f:
            resp.body = f.read()

    def on_post(self, req, resp):
        cuenta  = UsuarioInicioSesion(**req.media)
        if not cuenta.validar():
            resp.status = falcon.HTTP_200
            resp.content_type = 'text/html'
            with open("C:/Users/Javier/PycharmProjects/RedSocial/controlador/PersonaNoRegistrada.html", 'rb') as f:
                resp.body = f.read()
        else:
            resp.status = falcon.HTTP_200
            resp.content_type = 'text/html'
            with open("C:/Users/Javier/PycharmProjects/RedSocial/controlador/Bienvenido.html", 'rb') as f:
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


class Registro():
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 't      ext/html'
        with open("C:/Users/Javier/PycharmProjects/RedSocial/controlador/Registro.html", 'rb') as f:
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
