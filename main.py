from models import Client
from views import display_client_input, display_delete_client

# first we will need to create a class for clients so we can add/edit
# and delete them.  then we should initialize the client class and define
# what each action can do within that class
class ClientController:
    client_list = []
# self.Client = Client() when you get data from user, and you want to report in database (input in database)
# we can add a client, name (later more personal things)
    def __init__(self):
        self.name_of_client = None

    def add_client(self):
        while True:
            name_of_client, phone_number = display_client_input()
            client = Client(name_of_client, phone_number)
    # append to add a client object, not just the name as it was before
            self.client_list.append(client)
            print(f"client: {client.name} added successfully {client.phone_number}")
            more_info = input("Do you want to add another client? [y/n]")
            if more_info != "y":
                break


    def list_clients(self):
        for client in self.client_list:
            print(client.name)

    # error handling if the name or something goes wrong?
    def update_client(self):
        name_of_client = input("Enter name of client to update")
        for client in self.client_list:
            if client.name == name_of_client:
                new_name = input("Enter new name")
                client.name = new_name
                print(f"Client {client.name} updated successfully")
                return
            else:
                print(f"Client {client.name} not found.")

    def delete_client(self):
        # if name of client is in list or database we allow deletion if not then it goes into except (didnt' find)
        name_of_client = display_delete_client()
        for client in self.client_list:
            if client.name == name_of_client:
                self.client_list.remove(client)
                print(f"Client {client.name} deleted successfully")
                return
            else:
                print(f"client: {name_of_client} is not in the list")



    def main(self):
        while True:
            print("************************")
            print("Welcome to CliManager v1.0")
            print("************************")
            print("Select the number of your choice to display screen")
            print("1 Print my clients")
            print("2 Add a client")
            print("3 Edit a client")
            print("4 Delete a client")
            print("5 Exit")


            selection = input("Enter your choice (1 through 5):")

            if selection == "1":
                self.list_clients()
            elif selection == "2":
                self.add_client()
            elif selection == "3":
                self.update_client()
            elif selection == "4":
                self.delete_client()
            elif selection == "5":
                print ("Exiting")
                exit()

            else:
                print("Invalid input")




if __name__ == "__main__":
    client_controller = ClientController()
    client_controller.main()
