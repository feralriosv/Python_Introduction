from typing import override
from contactagenda.Contact import Contact
from contactagenda.FamilyRelation import Relation


class FamilyContact(Contact):
    def __init__(self, first_name, last_name, phone_number, relation : Relation) -> None:
        super().__init__(first_name, last_name, phone_number)
        self.__relation = relation

    @override
    def __str__(self) -> str:
        return f"{self.__relation.toString()}: {self.first_name} {self.last_name} - Tel:{self.phone_number}"