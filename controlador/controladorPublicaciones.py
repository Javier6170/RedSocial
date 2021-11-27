import falcon

from dominio.Publicacion import Publicacion
from controlador.red_social_controller import RedSocialController
from json import dumps
from servicios.Util import get_dir_project
from bs4 import BeautifulSoup

class ControlerPublicacion():
    def __get_publications(self):
        cuenta = Publicacion()
        publicaciones = cuenta.traer_publicaciones()
        html_page = open(get_dir_project()+"/controlador/paginaPrincipal.html", 'rb')
        soup = BeautifulSoup(html_page, 'html.parser')
        publis= soup.find(id="publis")
        for pub in publicaciones:
            new_div = soup.new_tag("div",attrs={"class":"card"})
            new_head = soup.new_tag("div",attrs={"class":"card-header"})
            new_head.string = str(pub.nombre_usuario + " " + pub.apellido_usuario)
            new_div_body = soup.new_tag("div",attrs={"class":"card-body"})
            new_div_body.string = str(pub.publicacion)
            new_div.append(new_head)
            new_div.append(new_div_body)
            publis.append(new_div)
        return soup.prettify()
    
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.body = self.__get_publications()

    def on_post(self, req, resp):
        nombreTemporal = RedSocialController.temporalNombre
        apellidoTemporal = RedSocialController.temporalApellido
        nombreTemporal.seek(0)
        apellidoTemporal.seek(0)
        lecturaNombre = nombreTemporal.read()
        lecturaApellido = apellidoTemporal.read()
        n = lecturaNombre.decode('UTF-8')
        a = lecturaApellido.decode('UTF-8')
        dict = {'id_p':-1,'publicacion': req.media.get('publicacion'), 'nombre_usuario': n, 'apellido_usuario': a}
        cuenta = Publicacion(**dict)
        cuenta.guardarPublicacion()
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.body = self.__get_publications()
        
        #with open(get_dir_project()+"/controlador/paginaPrincipal.html", 'rb') as f:
        #    resp.body = f.read()


def on_put(self, req, resp):
    nombreTemporal = RedSocialController.temporalNombre
    apellidoTemporal = RedSocialController.temporalApellido
    nombreTemporal.close()
    apellidoTemporal.close()
