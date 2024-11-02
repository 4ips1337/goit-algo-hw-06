from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)

    @staticmethod
    def validate_phone(phone):
        return phone.isdigit() and len(phone) == 10


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
        else:
            raise ValueError("Phone number not found.")

    def edit_phone(self, old_phone, new_phone):
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            self.phones[self.phones.index(phone_obj)] = Phone(new_phone)
        else:
            raise ValueError("Old phone number not found.")

    def find_phone(self, phone):
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj
        return None

    def __str__(self):
        phones_str = ", ".join(phone.value for phone in self.phones)
        return f"{self.name.value}: {phones_str if phones_str else 'No phones'}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Name not found in address book.")

    def __str__(self):
        records = "\n".join(str(record) for record in self.data.values())
        return f"AddressBook:\n{records if records else 'No records'}"


try:
    
    address_book = AddressBook()

    
    record = Record("Alice")
    record.add_phone("1234567890")
    address_book.add_record(record)

    
    print(address_book)

    
    found_record = address_book.find("Alice")
    print(f"Found record: {found_record}")

    
    record.edit_phone("1234567890", "0987654321")
    print(f"After editing: {found_record}")

    
    record.remove_phone("0987654321")
    print(f"After removing phone: {found_record}")

    
    address_book.delete("Alice")
    print("After deleting Alice:\n", address_book)

except ValueError as e:
    print(e)