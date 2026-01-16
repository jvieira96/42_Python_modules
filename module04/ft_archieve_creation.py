def main():
    filename = "data/new_discovery.txt"
    archive_entries = [
        "[ENTRY 001] New quantum algorithm discovered\n",
        "[ENTRY 002] Efficiency increased by 347%\n",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {filename}")
    try:
        file = open(filename, 'w')
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        for entry in archive_entries:
            file.write(entry)
            print(entry.strip())
        file.close()
        
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")
    except IOError:
        print("ERROR: Unauthorized access or storage failure.")

if __name__ == "__main__":
    main()
