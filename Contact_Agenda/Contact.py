from typing import override
from abc import ABC, abstractmethod

class Contact(ABC):
    # Private attributes format: self.__attribute
    def __init__(self, first_name: str, last_name: str, phone_number: int) -> None: # None: no return value
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone_number = phone_number

    @abstractmethod
    def __str__(self) -> str:
        pass

    # Getter methods go with @property label
    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def phone_number(self):
        return self.__phone_number