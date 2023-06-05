import rsa # Impordib rsa mooduli 

# Genereerib avaliku ja privaatse võtme 
public_key, private_key = rsa.newkeys(1024)

# Salvestab avaliku võtme faili 
with open("avalik_võti.txt", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

# Salvestab privaatse võtme faili 
with open("privaatne_võti.txt", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))