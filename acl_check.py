# Solicitar al usuario que introduzca el número de ACL
acl = int(input("Por favor, introduce el número de ACL IPv4: "))

# Comprobar si el número de ACL es una ACL estándar o extendida
if 1 <= acl <= 99 or 1300 <= acl <= 1999:
    print("La ACL es estándar.")
elif 100 <= acl <= 199 or 2000 <= acl <= 2699:
    print("La ACL es extendida.")
else:
    print("El número no corresponde a una lista de acceso.")
