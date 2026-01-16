import sys

def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")
    standard_msg = f"\n[STANDARD] Archive status from {archivist_id}: {status_report}\n"
    sys.stdout.write(standard_msg)

    alert_msg = "[ALERT] System diagnostic: Communication channels verified\n"
    sys.stderr.write(alert_msg)

    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("\nThree-channel communication test successful.")

if __name__ == "__main__":
    main()
