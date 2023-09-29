def extract_domain(email):
    parts = email.split("@")
    
    if len(parts)==2:
        return parts[1]
    else:
        return None
    
email1 = "user@domain.com"
domain = extract_domain(email1)

print(domain)