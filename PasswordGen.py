import string
import secrets

alphabet = string.ascii_letters + string.digits + string.punctuation
length=int(input("inserisci lunghezza password: "))
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3
            and any(c in string.punctiation for c in password)
    ):
        break
print(password)