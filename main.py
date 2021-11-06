from dominio.Usuario import Usuario

import requests


def crear_video_juego(nombre, apellido, usuario, password):
    url = "https://5768-186-83-184-33.ngrok.io/red-social/"
    body = {
        "nombre": nombre,
        "apellido": apellido,
        "usuario": usuario,
        "password": password
    }
    response = requests.request("POST", url,data=body)
    print(response.status_code)


if __name__ == '__main__':
    nombre = input("Nombre del Juego: ")
    apellido = input("release_date del Juego: ")
    usuario = input("clasificacion del Juego: ")
    password = input("Consola del Juego: ")
    crear_video_juego(nombre, apellido, usuario, password)
