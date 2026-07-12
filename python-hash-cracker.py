import hashlib

target_hash = "2ff0ba90379b492d9618c3cffce52cac"

print("=== ROZPOCZYNAMY ŁAMANIE HASHA ===")
with open("slownik.txt", "r") as file:
    for line in file:
        password= line.strip()

        hashed_password = hashlib.md5(password.encode()).hexdigest()

        print(f"Sprawdzam hasło: {password} -> generuje hash: {hashed_password}")

        if hashed_password == target_hash:
        
           print(f"\n[+] SUKCES! Hasło zostało złamane! Ukryte słowo to: {password}")


           break

