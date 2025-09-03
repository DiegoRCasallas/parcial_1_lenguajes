import re

def crear_expresion_regular():

    inicio = r'[A-Za-z_]'              
    siguientes = r'[A-Za-z0-9_]'      
    longitud = r'{4,9}'                
    
    # expresion
    patron = f'^{inicio}{siguientes}{longitud}$'
    
    return patron

def validar_id(identificador):
    patron = crear_expresion_regular()
    return re.match(patron, identificador) is not None
def probar_casos():
    patron = crear_expresion_regular()
    casos = [
        "abc12",     
        "MyVar_1",   
        "_private",   
         "a1b2c3d4e5",
        "123abc",     
        "9variable",
    ]

    print("PRUEBA CASOS")
    
    for caso in casos:
        if validar_id(caso):
            print(f"'{caso}' -> ACEPTA ")
            
        else:
            print(f"'{caso}' -> RECHAZA ")
    
    
   
if __name__ == "__main__":
    print("VALIDADOR DE IDENTIFICADORES (ID)")
    print("Reglas: empezar con letra/_, seguir con letra/dígito/_, longitud 5-10")
    print("=" * 70)
    probar_casos()
