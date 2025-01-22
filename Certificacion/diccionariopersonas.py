


nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
direccion = input("Ingrese su dirección: ")
telefono = input("Ingrese su número de teléfono: ")


perfil = {
    "nombre": nombre,
    "edad": edad,
    "direccion": direccion,
    "telefono": telefono
  }

print(f"{perfil['nombre']} tiene {perfil['edad']} años, vive en {perfil['direccion']} y su número de teléfono es {perfil['telefono']}.")
 