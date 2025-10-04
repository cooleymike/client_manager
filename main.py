import os
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from models import Client, Base
from views import display_client_input, display_delete_client, delete_client_message, updated_client_name, \
    display_clients

engine = create_engine("sqlite:///mydb.sqlite", echo=True)
Session = sessionmaker(engine)
# look at classes inheriting from BASE and create tables for those classes
Base.metadata.create_all(engine)

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
        print("Welcome to add a client")
        name_of_client, phone_number, address, work_title = display_client_input()
        client = Client(name_of_client=name_of_client, phone_number=phone_number, address=address, work_title=work_title)
    # append to add a client object, not just the name as it was before
    #     self.client_list.append(client)
        with Session( ) as session:
            session.add(client)
            session.commit()


# positional for few inputs - for lots of values/parameters we use Named Parameters
    # when create an instance use Named Parameters always - order doesn't matter

    def list_clients(self):
        with Session() as session:
            clients = session.query(Client).all()
            display_clients(clients)



    def update_client(self):
        name_of_client, new_client = updated_client_name()

        with Session() as session:
            found_client = session.execute(select(Client).filter_by(name_of_client=name_of_client)).scalar_one()
            found_client.name_of_client = new_client
            print(f"{found_client.name_of_client} updated")
            session.commit()
            return name_of_client, new_client


    def delete_client(self):
        name_of_client = display_delete_client()

        delete_client_message(name_of_client, False)
        with Session() as session:
            client = session.execute(select(Client).filter_by(name_of_client=name_of_client)).scalar_one()
            session.delete(client)
            session.commit()






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
