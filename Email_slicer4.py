"""
                        EMAIL SLICER
    
    if you enter your mail eg example@gmail.com 
    then out will be
    
    username: example
    domain: gmail
    extension: com
"""
def main():
    print("Welcome to Email Slicer!")
    print("")
    
    email = input("Please Enter your email.")
    
    (username, domain) = email.split("@")
    (domain, extension) = domain.split(".")
    
    print(f"Username: {username}\nDomain: {domain}\nExtension: {extension}")
    
    
main()