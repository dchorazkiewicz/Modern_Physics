def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity**2
 
def inverse_Ek(mass, Ek):
    velocity = (2 * Ek / mass) ** 0.5
    return velocity
 
def czas_lotu(velocity):
    return 2 * velocity / 10
 



mass = 1
velocity = 10

calkowity_czas = 0


# czas lotu po n krokach
def czas_lotu_n_krokach(mass, velocity, n):
    calkowity_czas = 0
    for i in range(n):
        czas = czas_lotu(velocity)
        calkowity_czas += czas
        Ek = calculate_kinetic_energy(mass, velocity)
        velocity = inverse_Ek(mass, Ek / 2)  
    return calkowity_czas


# czas lotu po 10, 100, 1000 krorkach
print(czas_lotu_n_krokach(mass, velocity, 4))
print(czas_lotu_n_krokach(mass, velocity, 100))
print(czas_lotu_n_krokach(mass, velocity, 1000))