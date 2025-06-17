from AddressBook import AddressBook
from contactagenda.FamilyContact import FamilyContact
from contactagenda.FamilyRelation import Relation


def main():
    my_address_book = AddressBook("My Address Book")
    first_contact = FamilyContact("Fernando", "Rios", 4939400192, Relation.SON)
    my_address_book.add_contact(first_contact)
    print(my_address_book, end="")

if __name__ == "__main__": # Java's main method
    main()
