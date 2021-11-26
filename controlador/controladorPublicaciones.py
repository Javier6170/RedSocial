import falcon

from dominio.Publicacion import Publicacion
from controlador.red_social_controller import RedSocialController
from json import dumps
from servicios.Util import get_dir_project
from bs4 import BeautifulSoup

class ControlerPublicacion():
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open(get_dir_project()+"/controlador/paginaPrincipal.html", 'rb') as f:
            resp.body = f.read()

    def on_post(self, req, resp):
        nombreTemporal = RedSocialController.temporalNombre
        apellidoTemporal = RedSocialController.temporalApellido
        nombreTemporal.seek(0)
        apellidoTemporal.seek(0)
        lecturaNombre = nombreTemporal.read()
        lecturaApellido = apellidoTemporal.read()
        n = lecturaNombre.decode('UTF-8')
        a = lecturaApellido.decode('UTF-8')
        dict = {'publicacion': req.media.get('publicacion'), 'nombre_usuario': n, 'apellido_usuario': a}
        cuenta = Publicacion(**dict)
        cuenta.guardarPublicacion()
        publicaciones = cuenta.traer_publicaciones()
        html_page = open(get_dir_project()+"/controlador/paginaPrincipal.html", 'rb')
        soup = BeautifulSoup(html_page, 'html.parser')
        publis= soup.find(id="publis")
        for pub in publicaciones:
          new_div = soup.new_tag("div")
          new_div.string = str(pub.publicacion)
          publis.append(new_div)
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.body = soup.prettify()
        
        #with open(get_dir_project()+"/controlador/paginaPrincipal.html", 'rb') as f:
        #    resp.body = f.read()


def on_put(self, req, resp):
    nombreTemporal = RedSocialController.temporalNombre
    apellidoTemporal = RedSocialController.temporalApellido
    nombreTemporal.close()
    apellidoTemporal.close()
