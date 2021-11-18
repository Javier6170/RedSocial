from falcon import App
import waitress

from controlador.controladorPublicaciones import ControlerPublicacion
from controlador.red_social_controller import RedSocialController, Registro


def iniciar() -> App:
    # run:app -b 0.0.0.0:2020 --workers 1 -t 240
    api = App()
    api.add_route("/redSocial/index.html", RedSocialController())
    api.add_route("/redSocial/Registro.html", Registro())
    api.add_route("/redSocial/paginaPrincipal.html", ControlerPublicacion())
    return api


app = iniciar()

if __name__ == "__main__":
    waitress.serve(app, port=8081, url_scheme="http")
