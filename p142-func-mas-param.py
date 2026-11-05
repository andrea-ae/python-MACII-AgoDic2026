# p142-func-mas-param.py
# Función que recibe n parámetros y los imprime en pantalla

def saluda(*nombres: str) -> None:
    print(nombres)
    for nombre in nombres:
        print(f"Hola {nombre}, ¡bienvdnid@ a python! \nTu nombre tiene {len(nombre)} caracteres.")

def edades(*edades: int) -> None:
    print(edades)
    for edad in edades:
        print(f"Tu edad es: {edad} años.")

saluda("Harry", "Niall", "Liam", "Zayn", "Louis")
edades(30, 31, 31, 31, 32)