import hashlib #biblioteca que se utiliza para calcular el hash del mesaje original y del mensaje cifrado

# Función para cifrar el mensaje usando una red de sustitución simple rot 3
def cifrar_mensaje(mensaje, desplazamiento):
    # inicia una cadena vacia
    mensaje_cifrado = ""
    #bucle for que recorre cada carácter en el mensaje original
    for caracter in mensaje:
    #  Se verifica si el carácter actual es una letra mayúscula o minúscula. Si es una letra, se realizará el cifrado.
        if 'A' <= caracter <= 'Z' or 'a' <= caracter <= 'z':
            nueva_posicion = (ord(caracter) - ord('a' if 'a' <= caracter <= 'z' else 'A') + desplazamiento) % 26 #las funciones ord para obtener el valor numérico del carácter
            mensaje_cifrado += chr(ord('a' if 'a' <= caracter <= 'z' else 'A') + nueva_posicion)#chr para convertir el valor numérico 
            # Para lograr Calcular la nueva posición del carácter cifrado.
        else:
            mensaje_cifrado += caracter
    return mensaje_cifrado

###########################################################################

# Lee el mensaje de entrada desde el archivo mensajedeentrada.txt
with open('mensajedeentrada.txt', 'r') as file:
    mensaje_original = file.read()

# Cifra el mensaje usando la variable desplazamiento
desplazamiento = 3
mensaje_cifrado = cifrar_mensaje(mensaje_original, desplazamiento)

# Se calcula el hash SHA-256 del mensaje original y se almacena en la variable 
hash_original = hashlib.sha256(mensaje_original.encode()).hexdigest()

# Escribe el mensaje cifrado y el hash en el archivo mensajeseguro.txt
with open('mensajeseguro.txt', 'w') as file:
    file.write(hash_original)
    file.write('\n')  # Separador
    file.write(mensaje_cifrado)

################################################

# Función para descifrar el mensaje cifrado rot se desplaza al sentido contrario
def descifrar_mensaje(mensaje_cifrado, desplazamiento):
    mensaje_descifrado = ""
    for caracter in mensaje_cifrado:
        if 'A' <= caracter <= 'Z' or 'a' <= caracter <= 'z':
            nueva_posicion = (ord(caracter) - ord('a' if 'a' <= caracter <= 'z' else 'A') - desplazamiento) % 26
            mensaje_descifrado += chr(ord('a' if 'a' <= caracter <= 'z' else 'A') + nueva_posicion)
        else:
            mensaje_descifrado += caracter
    return mensaje_descifrado

# Lee el mensaje cifrado y el hash desde el archivo mensajeseguro.txt
with open('mensajeseguro.txt', 'rb') as file:       #strip() se utiliza para eliminar cualquier espacio en blanco
    hash_original = file.readline().decode().strip()# .decode sirve para convertir una secuencia de bytes en una cadena de caracteres
    mensaje_cifrado = file.readline().decode()

# Descifra el mensaje usando la misma clave
desplazamiento = 3  # Utiliza la misma clave que en el programa de cifrado
mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, desplazamiento)

# Calcula un nuevo hash SHA-256 del mensaje descifrado
hash_descifrado = hashlib.sha256(mensaje_descifrado.encode()).hexdigest()

# Compara el hash original con el hash calculado del mensaje descifrado
if hash_original == hash_descifrado:
    print("El mensaje es auténtico.")
else:
    print("El mensaje ha sido modificado.")

# Guarda el mensaje descifrado en un archivo o lo crea.
with open('mensaje_descifrado.txt', 'w') as file:
    file.write(mensaje_descifrado)
