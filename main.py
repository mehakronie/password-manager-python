import pyperclip
import os

FILE_NAME = "passwords.txt"

def save_password():
    website = input("Enter the website: ")
    password = input("Enter the password: ")
    
    with open(FILE_NAME, 'a') as file:
        file.write(f"{website}:{password}\n")
    
    print("Password saved successfully!")

def get_password():
    website = input("Enter the website: ")
    with open(FILE_NAME, 'r') as file:
        for line in file:
            stored_website, stored_password = line.strip().split(':')
            if stored_website == website:
                pyperclip.copy(stored_password)
                print("Password copied to clipboard!")
                return
    print("Website not found.")
    

def main():
    while True:
        print("1. Save a password")
        print("2. Get a password")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            save_password()
        elif choice == '2':
            get_password()
        elif choice == '3':
            print("exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()