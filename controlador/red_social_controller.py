import falcon

class RedSocialController():
    def on_get(self, req, resp):

        print("hola")
        template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
         <meta charset="UTF-8">
         <title>Hello!</title>
        <link rel="stylesheet" href="css/estilos.css">
        </head>
        <body>
            <div class="cod-container">
        <div class="form-header">
            <img src="../img/Logo.png" alt="Logo de CodigoMasters">
            <h1>Codigo<span>Masters</span></h1>
        </div>

        <div class="form-content">
            <form action="#" class="cod-form">
                <div class="form-title">
                    <h3>Iniciar Sesión</h3>
                </div>

                <div class="input-group">
                    <input type="email" class="form-input" name="form-input" id="correo">
                    <label class="label" for="correo">Correo</label>
                </div>

                <div class="input-group">
                    <input type="password" class="form-input" name="form-input" id="pass">
                    <label class="label" for="pass">Contraseña</label>
                </div>

                <div class="input-group">
                    <input type="submit" class="form-input" value="Iniciar Sesión">
                    <p>No tienes cuenta? <a href="#" class="alt-form">Ingresa aquí</a></p>
                </div>

            </form>
        </div>


        <div class="form-content">
            <form action="#" class="cod-form">
                <div class="form-title">
                    <h3>Regístrate Gratis</h3>
                </div>

                <div class="input-group">
                    <input type="email" class="form-input" name="form-input" id="reg-correo">
                    <label class="label" for="reg-correo">Correo</label>
                </div>

                <div class="input-group">
                    <input type="password" class="form-input" name="form-input" id="reg-pass">
                    <label class="label" for="reg-pass">Contraseña</label>
                </div>

                <div class="input-group">
                    <input type="password" class="form-input" name="form-input" id="reg-rep-pass">
                    <label class="label" for="reg-rep-pass">Repetir Contraseña</label>
                </div>

                <div class="input-group">
                    <input type="submit" class="form-input" value="Registrate">
                    <p>Ya tienes cuenta? <a href="#" class="alt-form">Ingresa aquí</a></p>
                </div>

            </form>
        </div>
    </div>

    <script src="js/jquery-3.3.1.min.js"></script>
    <script src="js/form.js"></script>
</body>
</html>
        """
        resp.body = template
        resp.content_type = 'text/html'
        resp.status = falcon.HTTP_OK
