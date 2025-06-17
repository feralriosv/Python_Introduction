from enum import Enum

class Relation(Enum):
    SON = "Son"
    MOTHER = "Mother"
    FATHER = "Father"
    UNCLE = "Uncle"
    AUNT = "Aunt"
    DAUGHTER = "Daughter"

    def toString(self):
        return self.value