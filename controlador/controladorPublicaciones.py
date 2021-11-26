import falcon

from dominio.Publicacion import Publicacion
from controlador.red_social_controller import RedSocialController


class ControlerPublicacion():
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open("C:/Users/Javier/PycharmProjects/RedSocial/controlador/paginaPrincipal.html", 'rb') as f:
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
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open("C:/Users/Javier/PycharmProjects/RedSocial/controlador/paginaPrincipal.html", 'rb') as f:
            resp.body = f.read()


def on_put(self, req, resp):
    nombreTemporal = RedSocialController.temporalNombre
    apellidoTemporal = RedSocialController.temporalApellido
    nombreTemporal.close()
    apellidoTemporal.close()
