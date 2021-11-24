
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "Alexa",
                "last_name": last_name,
                "age": 22,
                "lucky_numbers": [0,6,2,4,3]
            },
            {
                "id": self._generateId(),
                "first_name": "Siri",
                "last_name": last_name,
                "age":25,
                "Lucky Numbers": [10, 11, 12]
            },
            {
                "id": self._generateId(),
                "first_name": "Google",
                "last_name": last_name,
                "age":28,
                "Lucky Numbers": [0, 5, 6]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)
        return self

    def delete_member(self, id):
        for position, member in enumerate(self._members): 
            if member["id"] == int(id): 
                kicked_member = self._members.pop(position) 
                return kicked_member

    def get_member(self, id):
        for member in self._members:
            if member["id"] == int(id): 
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
