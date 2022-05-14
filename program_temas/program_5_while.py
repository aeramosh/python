#ciclo while, programa para validar password
contrasena = "x"
intento = 1
while intento < 4 and contrasena != "mundo" :
    contrasena = input("Dame la contraseña de ingreso ")
    print("intento ", intento)
    intento = intento + 1        
if contrasena == "mundo" :
    print("Bienvenido al Curso de Pyton")
else :
    print("exceso de intentos, hasta la vista baby")

        