from dataclasses import dataclass

from charset_normalizer import models
from faker.providers import phone_number

@dataclass
class Personal_Information:
    # def __init__(self, phone_number, address, work_title):
    #     self.phone_number = phone_number
    #     self.address = address
    #     self.work_title = work_title

    phone_number: str
    address: str
    work_title: str


class Client (Personal_Information):
    def __init__(self, name_of_client, phone_number, address, work_title): # automatically inherits all parent class attributes
        self.name_of_client = name_of_client
        super().__init__(phone_number, address, work_title)


class Vendor (Personal_Information):  # no overloading/over writing just reusing the init method from line 6
    pass





