# Diccionarios en Python: pares clave-valor

# Creación de un diccionario
persona = {
    "nombre": "Ana",
    "edad": 25,
    "pais": "México",
}

print("Diccionario completo:", persona)

# Acceso a valores mediante su clave
print("Nombre:", persona["nombre"])

# get evita que el programa falle si la clave no existe
print("Profesión:", persona.get("profesion", "No especificada"))

# Agregar o modificar elementos
persona["profesion"] = "Ingeniera"
persona["edad"] = 26
print("Después de modificarlo:", persona)

# Eliminar elementos
eliminado = persona.pop("pais")
print("Elemento eliminado:", eliminado)
print("Después de eliminar:", persona)

# Recorrer claves, valores y pares clave-valor
print("Claves:")
for clave in persona:
    print("-", clave)

print("Valores:")
for valor in persona.values():
    print("-", valor)

print("Pares clave-valor:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Comprobar si una clave existe
if "nombre" in persona:
    print("El diccionario contiene una clave llamada 'nombre'")

# Ejemplo común: convertir una lista de pares en un diccionario
productos = dict([("pan", 20), ("leche", 30), ("huevo", 45)])
print("Precios:", productos)

# Ejemplo común: contar elementos
palabras = ["python", "diccionario", "python", "clase", "python"]
conteo = {}

for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print("Frecuencia de palabras:", conteo)


class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())