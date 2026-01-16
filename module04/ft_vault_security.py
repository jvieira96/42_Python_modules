def main():
    classified_data = "data/classified_data.txt"
    new_discovery = "data/security_protocols.txt"
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    try:
        print("Vault connection established with failsafe protocols\n")
        print("SECURE EXTRACTION")
        with open(classified_data, 'r') as r_file:
            content = r_file.read()
            print(content)
    except FileNotFoundError:
        print("[ERROR] No classified data found.")
    try:
        print("Vault connection established with failsafe protocols\n")
        print("SECURE PRESERVATION")
        with open(new_discovery, 'w') as w_file:
            text = "[CLASSIFIED] New security protocols archived"
            w_file.write(text)
            print(text)
            print("Vault automatically sealed upon completion\n")
    except IOError:
        print("ERROR: Failed to write to vault.")

    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
