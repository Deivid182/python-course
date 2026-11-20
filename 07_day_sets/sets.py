"""Ejemplos de usos habituales de los conjuntos (sets) en Python."""

# 1. Crear conjuntos. No guardan elementos repetidos y no tienen un orden fijo.
frutas = {"manzana", "pera", "manzana"}
print("Conjunto sin duplicados:", frutas)

# Un conjunto vacío se crea con set(); {} crea un diccionario vacío.
vacio = set()

# Sus elementos deben ser inmutables (por ejemplo, números o cadenas).
numeros = set([1, 2, 2, 3])  # También se puede construir desde una lista.
print("Desde una lista:", numeros)

# 2. Añadir y quitar elementos.
frutas.add("naranja")
frutas.update(["uva", "kiwi"])  # Añade varios elementos.
frutas.discard("ciruela")  # No da error si el elemento no existe.
frutas.remove("pera")  # Da KeyError si el elemento no existe.
print("Después de modificarlo:", frutas)

# 3. Comprobar pertenencia y recorrer elementos.
print("¿Hay manzana?", "manzana" in frutas)
for fruta in frutas:
	print("Fruta:", fruta)

# 4. Operaciones entre conjuntos.
grupo_a = {"Ana", "Luis", "Marta"}
grupo_b = {"Marta", "Pablo", "Luis"}

print("Unión:", grupo_a | grupo_b)  # Elementos de cualquiera de los dos.
print("Intersección:", grupo_a & grupo_b)  # Elementos comunes.
print("Diferencia A - B:", grupo_a - grupo_b)  # Solo los que están en A.
print("Diferencia simétrica:", grupo_a ^ grupo_b)  # Están en uno, no en ambos.

# También existen los métodos union(), intersection(), difference() y
# symmetric_difference(), equivalentes a los operadores anteriores.

# 5. Comparar conjuntos: subconjuntos, superconjuntos y disjunción.
permisos = {"leer", "escribir"}
permisos_admin = {"leer", "escribir", "borrar"}
print("¿Permisos incluidos?", permisos <= permisos_admin)
print("¿Es superconjunto?", permisos_admin.issuperset(permisos))
print("¿No comparten elementos?", {1, 2}.isdisjoint({3, 4}))

# 6. Quitar duplicados de una colección.
colores = ["rojo", "azul", "rojo", "verde", "azul"]
colores_unicos = set(colores)
print("Colores únicos (orden no garantizado):", colores_unicos)

# Si se necesita conservar el orden original, dict.fromkeys es una alternativa.
colores_sin_repetir_y_en_orden = list(dict.fromkeys(colores))
print("Sin duplicados y en orden:", colores_sin_repetir_y_en_orden)

# 7. Comprensión de conjuntos: crear un conjunto a partir de una expresión.
cuadrados_pares = {numero**2 for numero in range(10) if numero % 2 == 0}
print("Cuadrados de números pares:", cuadrados_pares)

# 8. frozenset es un conjunto inmutable; puede usarse como clave o elemento.
coordenadas = frozenset({("x", 1), ("y", 2)})
conjuntos = {frozenset({1, 2}), frozenset({3, 4})}
print("Conjunto inmutable:", coordenadas)
print("Conjuntos dentro de otro conjunto:", conjuntos)
