import re

def is_valid_email(email):
    # Basic email validation using regex
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

email = input("Enter Your Email: ")

if is_valid_email(email):
    try:
        res = email.split("@")
        username = res[0]
        domain_parts = res[1].split(".")
        
        # Handling multiple subdomains
        domain_name = ".".join(domain_parts[:-1])
        top_level_domain = domain_parts[-1]

        print("UserName: ", username)
        print("Domain Name: ", domain_name)
        print("Top Level Domain: ", top_level_domain)
    
    except Exception as e:
        print("An error occurred while processing the email:", e)
else:
    print("Invalid email format. Please enter a valid email.")
