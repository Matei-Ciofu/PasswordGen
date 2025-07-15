import string
import secrets
def ask(question):
      while True:
            answer = input(question+"(si/no): ").strip().lower()
            if answer in ['si','no']:
                  return answer == 'si'
            print("Rispondi con 'si' o 'no'")
      
def generate_password(length,use_lower,use_upper,use_digits,use_punctuation):
        alphabet = ""
        if use_lower:
                alphabet+= string.ascii_lowercase
        if use_upper:
                alphabet+= string.ascii_uppercase
        if use_digits:
                alphabet+= string.digits
        if use_punctuation:
                alphabet+= string.punctuation
             
        if not alphabet:
                raise ValueError("La password deve esistere, seleziona almeno un tipo di catattere")
        min_digits=2
        while True:
                password = ''.join(secrets.choice(alphabet) for i in range(length))
                if ((not use_lower or any(c.islower() for c in password)) and
                    (not use_upper or any(c.isupper() for c in password)) and
                    (not use_digits or sum(c.isdigit() for c in password) >= min_digits) and
                    (not use_punctuation or any(c in string.punctuation for c in password)) 
                ):
                        return password
                
def main():
    try:
       length=int(input("inserisci lunghezza password: "))
       max_length = 64
       min_length=4
       if min_length>=length or max_length<=length:
           print(f"La lunghezza minina é {min_length} caratteri e massima {max_length}")
           return
    except ValueError:
        print("Inserito numero non valido")
        return
    print("Che caratteri vuoi utilizzare?")
    use_lower = ask("Lettere minuscole")
    use_upper = ask("Lettere maiuscole")
    use_digits = ask("Numeri")
    use_punctuation = ask("Simboli")
    password = generate_password(length,use_lower,use_upper,use_digits,use_punctuation)
    print(f"Password: {password}")

if __name__=="__main__":
      main()