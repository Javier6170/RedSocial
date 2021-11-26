import codecs
import falcon

from dominio.usuarioTemporal import UsuarioTemporal
from infraestructura.persistencia_usuario import PersistenciaUsuario

from dominio.Usuario import Usuario
from dominio.UserInicioSesion import UsuarioInicioSesion
import tempfile
from servicios.Util import get_dir_project


class RedSocialController():
    temporalNombre = tempfile.TemporaryFile()
    temporalApellido = tempfile.TemporaryFile()

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'

        with open(get_dir_project()+"/controlador/index.html", 'rb') as f:
            resp.body = f.read()

    def on_post(self, req, resp):
        cuenta = UsuarioInicioSesion(**req.media)
        if not cuenta.validar():
            resp.status = falcon.HTTP_200
            resp.content_type = 'text/html'
            with open(get_dir_project()+"/controlador/PersonaNoRegistrada.html", 'rb') as f:
                resp.body = f.read()
        else:

            resp.status = falcon.HTTP_200
            resp.content_type = 'text/html'
            with open(get_dir_project()+"/controlador/paginaPrincipal.html", 'rb') as f:
                resp.body = f.read()
            #resp.status = falcon.HTTP_200
            #resp.content_type = 'application/json'
            
            #resp.body = {"status":"ok"}
            if RedSocialController.temporalNombre.closed or RedSocialController.temporalApellido.closed:
                RedSocialController.temporalNombre = tempfile.TemporaryFile()
                RedSocialController.temporalApellido = tempfile.TemporaryFile()
            nombre_usuario = cuenta.validar().nombre
            apellido_usuario = cuenta.validar().apellido
            bnombreUsuario = bytes(nombre_usuario, encoding="utf-8")
            bapellidoUsuario = bytes(apellido_usuario, encoding="utf-8")
            RedSocialController.temporalNombre.write(bnombreUsuario)
            RedSocialController.temporalApellido.write(bapellidoUsuario)

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
        with open(get_dir_project()+"/controlador/Registro.html", 'rb') as f:
            resp.body = f.read()

    def on_post(self, req, resp):
        cuenta = Usuario(**req.media)
        if cuenta.guardar() is None:
            resp.status = falcon.HTTP_200
            resp.content_type = 'text/html'
            with open(get_dir_project()+"/controlador/falloRegistro.html", 'rb') as f:
                resp.body = f.read()
        else:
            resp.status = falcon.HTTP_200
            resp.content_type = 'text/html'
            with open(get_dir_project()+"/controlador/correctoRegistro.html", 'rb') as f:
                resp.body = f.read()
