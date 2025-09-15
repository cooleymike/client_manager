from curses.ascii import isalpha
import re

def display_client_input():
    name = ""
    phone_number = ""
    while not name.isalpha() or not phone_number.isdigit():
        print("Please enter a valid name (alphanumeric), and phone number (digits)")
        name = input("Enter your name: ")
        phone_number = input("Enter your phone number: ")
        pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
        if pattern.match(phone_number):
            print("Your phone number is valid.")
    return name, phone_number



def display_delete_client():
    client_id = None
    while client_id is None:
        try:
            client_id = int(input("Enter number of clients to delete"))

        except ValueError:
            print("Enter a valid number")
    return client_id

def add_client():


