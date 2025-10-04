from curses.ascii import isalpha
import re




def display_client_input():
    name_of_client = ""
    phone_number = ""
    address = ""
    work_title = ""
    while not name_of_client.isalpha() or not phone_number.isdigit():
        print("Please enter a valid name (alphanumeric), and phone number (digits)")
        name_of_client = input("Enter your name: ")
        phone_number = input("Enter your phone number: ")
        address = input("Enter your address: ")
        work_title = input("Enter your work title: ")
        pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
        if pattern.match(phone_number):
            print("Your phone number is valid.")
    return name_of_client, phone_number, address, work_title

def add_client():
    while True:
        name_of_client = input("Enter your client's name: ")
        phone_number = input("Enter your client's phone number: ")
        address = input("Enter your client's address: ")
        work_title = input("Enter your client's work title: ")
        print(f"Client name: {name_of_client} phone number: {phone_number} address: {address} and work title: {work_title} added successfully")
        more_info = input("Do you want to add another client? [y/n]")
        if more_info != "y":
            break
        return name_of_client, phone_number, address, work_title


def display_delete_client():
    name_of_client = ""
    # import pdb; pdb.set_trace()
    while not name_of_client.isalpha():
         name_of_client = input("Enter name of clients to delete")
    return name_of_client


def delete_client_message(name_of_client, message=True):
    if message:
        print(f"You have successfully deleted your client{name_of_client}.")
    else:
        print(f"You have not successfully deleted your client{name_of_client}.")




def display_clients(client_list):
    if not client_list:
        print("No clients found")
        return
    for client in client_list:
        print(f"{client.name_of_client}: {client.phone_number}: {client.address}: {client.work_title} ")



def updated_client_name():
    name_of_client = input("Enter name of client to update")
    new_name = input("Enter new name to update: ")
    return name_of_client, new_name


    # if message=True:
    #     print(f"Client {name_of_client} updated successfully")
    # else:
    #      print(f"Client {name_of_client} not found.")

