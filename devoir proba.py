# ==========================================
# CALCULATEUR DE DOSAGE DU BÉTON
# ==========================================

print("==========================================")
print("       CALCULATEUR DE DOSAGE DU BÉTON")
print("==========================================")

# Entrée du volume de béton
volume = float(input("Entrez le volume de béton (m³) : "))

# Dosage du ciment
dosage_ciment = float(input(
    "Entrez le dosage du ciment (kg/m³) [ex: 350] : "
))

# Calcul du ciment
ciment = volume * dosage_ciment

# Nombre de sacs de 50 kg
sacs = ciment / 50

# Quantités de sable, gravier et eau
# Valeurs de référence pour 1 m³
sable_par_m3 = 0.50
gravier_par_m3 = 0.80
eau_par_m3 = 175

sable = volume * sable_par_m3
gravier = volume * gravier_par_m3
eau = volume * eau_par_m3

# Affichage des résultats
print("\n==========================================")
print("              RÉSULTATS")
print("==========================================")

print(f"Volume de béton : {volume:.2f} m³")
print(f"Ciment          : {ciment:.2f} kg")
print(f"Sacs de 50 kg   : {sacs:.2f} sacs")
print(f"Sable           : {sable:.2f} m³")
print(f"Gravier         : {gravier:.2f} m³")
print(f"Eau             : {eau:.2f} litres")

print("==========================================")