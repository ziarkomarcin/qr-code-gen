def display_menu():
    print("=== Main Menu ===")
    print("1. Create Your QR Code")
    print("2. Search QR Codes")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("Select an option (0-2): ")

        if choice == "1":
            print("You selected: Create Your QR Code")
            # Add functionality for creating a QR code here
        elif choice == "2":
            print("You selected: Search QR Codes")
            # Add functionality for searching QR codes here
        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()