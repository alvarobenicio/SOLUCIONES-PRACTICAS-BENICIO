familia = {
    "persona1": {
        "nombre": "Gonzalo",
        "apellido": "Farias",
        "dni": "46987456",
        "email": "gonzalofarias@hotmail.com",
        "fecha_nacimiento": "1990-07-12"
    },
    "persona2": {
        "nombre": "María",
        "apellido": "Farias",
        "dni": "23456789",
        "email": "mariafarias@hotmail.com",
        "fecha_nacimiento": "1985-08-20"
    },
    "persona3": {
        "nombre": "Pedro",
        "apellido": "Farias",
        "dni": "34567890",
        "email": "pedrofARIAS@HOTMAIL.com",
        "fecha_nacimiento": "1995-03-10"
    },
    "persona4": {
        "nombre": "Ana",
        "apellido": "Farias",
        "dni": "45678901",
        "email": "anafari@hotmail.com",
        "fecha_nacimiento": "1980-11-25"
    }
}

for clave, datos_persona in familia.items():
    print("\nPersona:", clave)
    print("Nombre:", datos_persona["nombre"])
    print("Apellido:", datos_persona["apellido"])
    print("DNI:", datos_persona["dni"])
    print("Email:", datos_persona["email"])
    print("Fecha de Nacimiento:", datos_persona["fecha_nacimiento"])
