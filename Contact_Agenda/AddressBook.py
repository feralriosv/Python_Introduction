import os

class AddressBook:
    def __init__(self, title: str) -> None:
        self.__title = title
        self.__contacts = []
        self.__total_contacts = 0

    @property
    def title(self) -> str:
        return self.__title

    # Arrays have implementations
    def add_contact(self, contact):
        self.__contacts.append(contact)
        self.__total_contacts += 1

    def remove_contact(self, contact):
        self.__contacts.remove(contact)
        self.__total_contacts -= 1

    def get_total_contacts(self):
        return self.__total_contacts

    def __str__(self):
        contact_list = []
        number_of_contacts = len(self.__contacts)
        contact_list.append("~" + self.__title + "~")
        for i in range(number_of_contacts):
            contact_list.append(self.__contacts[i].__str__())
        return os.linesep.join(contact_list)