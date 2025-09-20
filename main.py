import os

from models import Client
from views import display_client_input, display_delete_client, delete_client_message, updated_client_name


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
        os.system('clear')
        print("Welcome to the future to add a client")
        name_of_client, phone_number, address, work_title = display_client_input()
        client = Client(name_of_client, phone_number, address, work_title)
    # append to add a client object, not just the name as it was before
        self.client_list.append(client)





    def list_clients(self):
            if not self.client_list:
                return
            for client in self.client_list:
                print(f"{client.name_of_client}: {client.phone_number}: {client.address}: {client.work_title}")


    def update_client(self):
        name_of_client, new_client = updated_client_name()
        for client in self.client_list:
            if client.name_of_client == name_of_client: #iterate through clients and get new name
                client.name_of_client = new_client # the updated client name to BE the client name =
                return



    def delete_client(self):
        name_of_client = display_delete_client()
        # import pdb;
        # pdb.set_trace()
        for client in self.client_list:
            if client.name_of_client == name_of_client:
                self.client_list.remove(client)
                delete_client_message(name_of_client, True)
                return
        delete_client_message(name_of_client, False)






    def main(self):
        while True:
            os.system('clear')
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
