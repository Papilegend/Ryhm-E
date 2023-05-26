import mysql.connector
import bcrypt

conn = mysql.connector.connect(
    host='sql7.freemysqlhosting.net',
    port=3306,
    database='sql7620863',
    user='sql7620863',
    password='9T7P1uHFr6'
)
cursor = conn.cursor()


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

def registeerima():
    kasutajanimi = input("Sisesta kasutajanimi: ")
    password = input("Sisesta salasõna: ")

    # Hashi ja soola salasõna
    hashed_password = hash_password(password)

    # Salvesta kasutaja andmebaasi
    query = "INSERT INTO kasutajad (kasutajanimi, password) VALUES (%s, %s)"
    values = (kasutajanimi, hashed_password)
    cursor.execute(query, values)
    conn.commit()

    print("Kasutaja on edukalt registeeritud!")


def login():
    username = input("Sisesta kasutajanimi: ")
    password = input("Sisesta salasõna: ")

    # Retrieve the stored hashed password for the entered username
    query = "SELECT password FROM kasutajad WHERE kasutajanimi = %s"
    values = (username,)
    cursor.execute(query, values)
    result = cursor.fetchone()

    if result:
        stored_password = result[0]

        # Check if the entered password matches the stored hashed password
        if bcrypt.checkpw(password.encode(), stored_password.encode()):
            print("Edukalt sisse loginud!")
        else:
            print("Vale salasõna!")
    else:
        print("Ei leia kasutajat")

registeerima()
login()

conn.close()