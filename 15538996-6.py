# Archivo: 15538996-6.py

# Definir las VLANs para cada switch según el diagrama
switch1 = {"native_vlan": 99, "vlans": [10, 20, 30]}
switch2 = {"native_vlan": 200, "vlans": [40, 50, 60]}

# Definir las VLANs para comparar
compare_vlans1 = [10, 100, 30]
compare_vlans2 = [40, 50, 60]

# Comparar las VLANs nativas y las VLANs creadas para cada switch
for i, switch in enumerate([switch1, switch2], start=1):
    # Comparar la VLAN nativa
    if switch["native_vlan"] == 99:
        print(f"Para el switch{i}, las vlans nativas son iguales y cumplen con el requerimiento")
    else:
        print(f"Para el switch{i}, las vlans nativas son diferentes y no cumplen con el requerimiento")

    # Comparar las VLANs creadas
    compare_vlans = compare_vlans1 if i == 1 else compare_vlans2
    if set(switch["vlans"]) == set(compare_vlans):
        print(f"Para el switch{i}, las vlans creadas son iguales y cumplen con el requerimiento")
    else:
        print(f"Para el switch{i}, las vlans creadas son diferentes y no cumplen con el requerimiento")
