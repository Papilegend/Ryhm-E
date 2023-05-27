import mysql.connector # Impordin MySQLi Connector mooduli
import bcrypt # Impordin bcrypti mooduli soolamiseks ja hashimiseks

# Tekitan ühenduse https://www.freemysqlhosting.net andmebaasiga
conn = mysql.connector.connect(
    host='sql7.freemysqlhosting.net',
    port=3306,
    database='sql7620863',
    user='sql7620863',
    password='9T7P1uHFr6'
)
cursor = conn.cursor()  # Tekitan kursoriobjekti SQL-päringute täitmiseks


def hash_password(password):
    # Genereerin suvalise soolamise väärtuse
    sool = bcrypt.gensalt()

    # Hashin salasõna kasutades bcrypti
    hashed_password = bcrypt.hashpw(password.encode(), sool)
    return hashed_password

def registeerima():
    # Loon while tsükli, mis kestab nii kaua, kui on valitud kasutajanimi, mis pole andmebaasis
    kasutaja_on = True
    while kasutaja_on: 

        # Küsin kasutajalt kasutajanime ja salasõna
        kasutajanimi = input("Sisesta kasutajanimi: ")

        # Vaatan, kas kasutajanimi on võetud või mitte
        paring = "SELECT kasutajanimi FROM kasutajad WHERE kasutajanimi = %s"
        vaartused = (kasutajanimi,)
        cursor.execute(paring, vaartused)
        result = cursor.fetchone()

        if result:
            print("Kasutajanimi on juba võetud!")
        else:
            kasutaja_on = False

    password = input("Sisesta salasõna: ")

    # Hashin ja soolan alaprogrammi abil salasõna
    hashed_password = hash_password(password)

    # Salvestan kasutaja andmebaasi
    paring = "INSERT INTO kasutajad (kasutajanimi, password) VALUES (%s, %s)"
    vaartused = (kasutajanimi, hashed_password)
    cursor.execute(paring, vaartused)
    conn.commit()

    print("Kasutaja on edukalt registeeritud!")


def login():

    # Küsin kasutajalt kasutajanime ja salasõna
    kasutajanimi = input("Sisesta kasutajanimi: ")
    password = input("Sisesta salasõna: ")

    # Hangin andmebaasist sisestatud kasutajanime jaoks salvestatud hashitud ja soolatud salasõna
    paring = "SELECT password FROM kasutajad WHERE kasutajanimi = %s"
    vaartused = (kasutajanimi,)
    cursor.execute(paring, vaartused)
    result = cursor.fetchone()

    if result:
        stored_password = result[0]

        # Vaatan, kas sisestatud salasõna sobitud andmebaasis oleva hashitud salasõnaga 
        if bcrypt.checkpw(password.encode(), stored_password.encode()):
            print("Edukalt sisse loginud!")
        else:
            print("Vale salasõna!")
    else:
        print("Ei leia kasutajat")

# Küsin kasutajalt, millist funktsiooni ta kasutada tahab
valik = int(input("Sisselogimine - vajuta 0\nRegisteerimine - vajuta 1\nValik: "))

if valik == 0:
    login() # Kutsun välja sisselogimise 
elif valik == 1:
    registeerima() # Kutsun välja kasutaja registeerimise 
conn.close()
