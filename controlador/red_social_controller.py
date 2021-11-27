import codecs
import falcon

from dominio.usuarioTemporal import UsuarioTemporal
from infraestructura.persistencia_usuario import PersistenciaUsuario

from dominio.Usuario import Usuario
from dominio.Publicacion import Publicacion
from dominio.UserInicioSesion import UsuarioInicioSesion
import tempfile
from servicios.Util import get_dir_project
from bs4 import BeautifulSoup

class RedSocialController():
    temporalNombre = tempfile.TemporaryFile()
    temporalApellido = tempfile.TemporaryFile()

    def __get_publications(self):
        cuenta = Publicacion()
        publicaciones = cuenta.traer_publicaciones()
        html_page = open(get_dir_project()+"/controlador/paginaPrincipal.html", 'rb')
        soup = BeautifulSoup(html_page, 'html.parser')
        publis= soup.find(id="publis")
        for pub in publicaciones:
            new_div = soup.new_tag("div",attrs={"class":"card"})
            new_head = soup.new_tag("div",attrs={"class":"card-header"})
            new_head.string = pub.nombre_usuario + " " + pub.apellido_usuario
            new_div_body = soup.new_tag("div",attrs={"class":"card-body"})
            new_div_body.string = str(pub.publicacion)
            new_div.append(new_head)
            new_div.append(new_div_body)
            publis.append(new_div)
        return soup.prettify()

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
            resp.body = self.__get_publications()
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
        resp.content_type = 'text/html'
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
