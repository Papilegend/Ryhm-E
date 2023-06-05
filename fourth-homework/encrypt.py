import rsa # Impordib RSA mooduli 

# Avab faili, et kasutada privaatset võtit
with open("privaatne_võti.txt", "r") as f:

    # Laeb privaatse võtme failist muutujasse
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

    # Küsib kasutajalt, mis teksti ta tahab krüpteerida
    tekst = input("Sisesta tekst, mida sa tahad krüpteerida: ")

    # Krüpteerib teksti, kasutades privaatset võtit 
    encrypted_tekst = rsa.encrypt(tekst.encode(), private_key)
    
    # Salvestab krüpteeritud teksti faili 
    with open("encrypted.txt", "wb") as f:
        f.write(encrypted_tekst)

