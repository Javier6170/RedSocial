from falcon import App
import falcon
from falcon import API
import waitress

from controlador.red_social_controller import RedSocialController


def iniciar() -> App:
    # run:app -b 0.0.0.0:2020 --workers 1 -t 240
    api = App()
    api.add_route("/red-social/", RedSocialController())
    return api


app = iniciar()

if __name__ == "__main__":
    waitress.serve(app, port=8081, url_scheme="http")
