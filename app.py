from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        total_sin_descuento = tarros * 9000

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento * (1 - descuento)
        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, total_con_descuento=total_con_descuento)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    usuarios = {'juan': 'admin', 'pepe': 'user'}
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in usuarios and usuarios[username] == password:
            if username == 'juan':
                mensaje = f"Bienvenido administrador {username}"
            else:
                mensaje = f"Bienvenido usuario {username}"
        else:
            mensaje = "Usuario o contraseña incorrectos"
        return render_template('ejercicio2.html', mensaje=mensaje)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
