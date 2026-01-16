def main():
    file_name = "data/ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {file_name}")
    try:
        file = open(file_name, 'r')
        print("Connection established...\n")
        data = file.read()
        print("RECOVERED DATA:")
        print(data)
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
    print("\nData recovery complete. Storage unit disconnected")


if __name__ == "__main__":
    main()
