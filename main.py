import os

def display_menu():

    print("Welcome to the QR Code Generator")
    print("\n== MAIN MENU ==\n")
    my_menu_list = ["Create Your QR Code", "Search QR Codes", "Exit"]
    for option in my_menu_list:
        if option == "Exit":
            print("[0]", option)
        else:
            print([my_menu_list.index(option) + 1], option)

def main():
    while True:
        display_menu()
        choice = input("Select an option (0-2): ")

        if choice == "1":
            print("You selected: Create Your QR Code")
            # Add functionality for creating a QR code here
        elif choice == "2":
            print("You selected: Search QR Codes")
            os.startfile(r'C:\Users\ziark\Desktop\projects\qr-code-gen\qr-codes')
        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()