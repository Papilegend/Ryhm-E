import rsa # Impordib RSA mooduli 

# Avab faili, et saada kätte privaatset võtit
with open("privaatne_võti.txt", "rb") as f:

    # Laeb privaatse võtme failist muutujasse
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# Avab krüpteeritud teksti faili, et saada kätte krüpteeritud teksti 
encrypted_tekst = open("encrypted.txt", "rb").read()

# Dekrüpteerib privaatse võtme abil krüpteeritud teksti 
tekst = rsa.decrypt(encrypted_tekst, private_key)

print(tekst.decode())