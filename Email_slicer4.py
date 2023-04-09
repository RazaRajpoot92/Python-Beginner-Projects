def main():
    print("Welcome to Email Slicer!")
    print("")
    
    email = input("Please Enter your email.")
    
    (username, domain) = email.split("@")
    (domain, extension) = domain.split(".")
    
    print(f"Username: {username}\nDomain: {domain}\nExtension: {extension}")
    
    
main()