import string
import secrets
import re

print("                   .^~!!~^.  ")
print("                 !P#@@@@@@#P!")
print("               ^B@@@GJ??JG@@@B^")
print("              :&@@B^      ^B@@&:")
print("              ?@@@~        ~@@@?")
print("              ?@@@^        ^@@@?")
print("           ~Y5B@@@P55555555P@@@B5Y~")
print("          :&@@@@@@@@@@@@@@@@@@@@@@&:")
print("          :@@@@@@@@@@@@@@@@@@@@@@@@:")
print("          :&@@@@@@@@@@@@@@@@@@@@@@&:")
print("          :&@@@@@@@@@@@@@@@@@@@@@@&:")
print("          :&@@@@@@@@@@@@@@@@@@@@@@&:")
print("          :@@@@@@@@@@@@@@@@@@@@@@@@:")
print("+-----------------------------------------------+")
print("|               SECURE SENTINEL                 |")
print("+-----------------------------------------------+")
print("|       Generate a secure random password.      |")
print("+-----------------------------------------------+")


              
def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        print("Error: No character set selected.")
        return None
    
    password = ''
    for _ in range(length):
        password += secrets.choice(characters)
    
    return password

def get_user_preferences():
    print("Welcome to the Password Generator!")
    
    length = int(input("Enter the desired password length: "))
    
    print("Choose character types:")
    print("1. Include letters")
    print("2. Include digits")
    print("3. Include symbols")
    
    choices = input("Password Characteristic (e.g., '123'): ")

    
    use_letters = '1' in choices
    use_digits = '2' in choices
    use_symbols = '3' in choices
    
    return length, use_letters, use_digits, use_symbols

def check_password_strength(password):
    score = 0
    
    if len(password) >= 8:              # Check for length of password  
        score += 1

    # Check for uppercase, lowercase, and digits
    if re.search(r'[A-Z]', password) and \
       re.search(r'[a-z]', password) and \
       re.search(r'\d', password):
        score += 1

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):   # Check for special characters
        score += 1

    if score == 3:
        return "Strong - Password is very secure!"
    elif score == 2:
        return "Moderate - Password is moderately secure."
    else:
        return "Weak - Password needs improvement."
    

length, use_letters, use_digits, use_symbols = get_user_preferences()
    
password = generate_password(length, use_letters, use_digits, use_symbols)

strength = check_password_strength(password)
print("+-----------------------------------------------+")
print(f"\n\033[96mSecure Random password: {password}\033[0m\n")
print(f"Password Strength: {strength}")
print("+-----------------------------------------------+")