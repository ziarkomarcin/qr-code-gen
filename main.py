import os
import qrcode

def display_menu():

    print("Welcome to the QR Code Generator")
    print("\n== MAIN MENU ==\n")
    my_menu_list = ["Create Your QR Code", "Search QR Codes", "Exit"]
    for option in my_menu_list:
        if option == "Exit":
            print("[0]", option)
        else:
            print([my_menu_list.index(option) + 1], option)

def instructions():
    print("Instructions:")
    print("You can create a QR code by entering the data you want to encode.")
    print("The QR code will be saved as a PNG file in qr-codes folder.")
    print("Before creating a QR code make sure that the names of the files are unique.")
    print("You can also search for existing QR codes in the specified directory.")
    print("To exit the program, select 'Exit' from the menu.")

def create_qr():
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(input("Enter the data to be encoded: "))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(os.path.join("qr-codes", input("Enter the file name: ") + ".png"))
    print("QR code generated successfully!")

def main():
    while True:
        display_menu()
        choice = input("Select an option (0-2): ")

        if choice == "1":
            print("You selected: Create Your QR Code")
            instructions()
            create_qr()
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