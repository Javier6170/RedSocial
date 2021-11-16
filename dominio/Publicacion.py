class Publicacion(Usuario):
    def __init__(self,textoArea):
        self.textoArea = textoArea
        self.id_p=None


    def __str__(self):
        return f'{self.textoArea}---{self.id_p}'



