from math import pow
from abc import ABC, abstractmethod

class Validator(ABC):
    @abstractmethod
    def is_empty_cell(self, index) -> bool:
        ...
    
    @abstractmethod
    def is_empty(self) -> bool:
        ...

    @abstractmethod
    def is_full(self) -> bool:
        ...

    @abstractmethod
    def is_negative_number(self, n) -> bool:
        ...
    
    @abstractmethod
    def contains(self, key) -> bool:
        ...

        
class OpenAddressing(ABC):
    @abstractmethod
    def linear_probing(self, key, index) -> None:
        ...

    @abstractmethod
    def quadratic_probing(self, key, index) -> None:
        ...

class HashTable(ABC):
    _table = []
    _size = 0
    EMPTY_VALUE = -1

    def __init__(self) -> None:
        while self._size <= 0:
            try:
                self._size = int(input("Enter the size of hash table: "))
                raise
            except ValueError:
                print("Error: Enter integer only!")
            except Exception:
                print("Error: The size cannot be a negative number or zero!")
        
        # Set All Index in Array to have value of -1
        for i in range(self._size):
            self._table.append(self.EMPTY_VALUE)

    def hash(self, key) -> int:
        return key % self._size
    
    @abstractmethod
    def insert(self, key) -> None:
        ...

    @abstractmethod
    def delete(self, key) -> None:
        ...

    @abstractmethod
    def search(self, key) -> None:
        ...

    def get_size(self) -> int:
        return self._size


class Program(HashTable, Validator, OpenAddressing):
    _choice = 0
    _key = 0
    _runnable = True

    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        while self._runnable:
            print("\n Menu")
            print(" 1. Insert\n 2. Delete\n 3. Display\n 4. Search\n 5. Exit");
            try:
                self._choice = int(input("Enter a number: "))
                
                # Insert data
                if self._choice == 1:
                    self._enter_key()
                    self.insert(self._key)
                # Delete data set value back to -1
                elif self._choice == 2:
                    self._enter_key()
                    self.delete(self._key)
                # Display whole Array
                elif self._choice == 3:
                    self.display()
                # Search data in Array
                elif self._choice == 4:
                    self._enter_key()
                    self.search(self._key)
                # Exit
                elif self._choice == 5:
                    self._runnable = False
                # Handle wrong choice number
                else:
                    raise Exception("Wrong choice please input the number between or 1 - 5 only!")
            except ValueError:
                print("Error: Enter integer only!")
            except AssertionError:
                print("Error: The size cannot be a negative number or zero!")
            except Exception as e:
                print(e.__str__())
    
    def _enter_key(self) -> None:
        self._key = int(input("Enter the key: "))
        assert not self.is_negative_number(self._key) 

    def insert(self, key) -> None:
        index = self.hash(key)

        if self.is_full():
            print("Hash table is full!")
        elif self.is_negative_number(key):
            print("The key can't be entered as a negative number!")
        elif self.is_empty_cell(index):
            self._table[index] = key
        else:
            self.linear_probing(key, index)
            # self.quadratic_probing(key, index)

    def delete(self, key) -> None:
        if self.is_empty():
            print("Hash table is empty!")
            return
        if self.is_negative_number(key):
            print("The key can't be entered as a negative number!")
            return
        if not self.contains(key):
            print(f"The key {key} does not exist in the hash table!")
            return
        
        for i in range(self.get_size()):
            if self._table[i] == key:
                self._table[i] = self.EMPTY_VALUE
                print(f"Deleted {key} successfully.")
                break

    def display(self) -> None:
        print("\n-------------------\n")
        print("    Index   Key\n")
        
        for i in range(self.get_size()):
            if self.is_empty_cell(i):
                print(f"    [{i}]     ")
            else:
                print(f"    [{i}]    {self._table[i]}")

        print("\n-------------------\n")

    def linear_probing(self, key, index) -> None:
        while not self.is_empty_cell(index):
            index += 1    
            if index == self.get_size():
                index %= self.get_size()
        self._table[index] = key
        print(f"Inserted {key} successfully.")

    def quadratic_probing(self, key, index) -> None:
        i = 1
        new_index = index
        while not self.is_empty_cell(index):
            new_index = (index + pow(i, 2)) % self.get_size()
            i += 1
        self._table[new_index] = key
        print(f"Inserted {key} successfully.")

    def search(self, key) -> None:
        if self.contains(key):
            print(f"Found {key} in the hash table.")
        else:
            print(f"Not found {key} in the hash table.")

    def is_empty_cell(self, index) -> bool:
        return self._table[index] == self.EMPTY_VALUE
    
    def is_empty(self) -> bool:
        for i in range(self.get_size()):
            if not self.is_empty_cell(i):
                return False
        return True
    
    def is_full(self) -> bool:
        counter = 0
        for i in range(self.get_size()):
            if not self.is_empty_cell(i):
                counter += 1
        return counter == self._size

    def is_negative_number(self, n) -> bool:
        return n < 0
    
    def contains(self, key) -> bool:
        for i in range(self.get_size()):
            if self._table[i] == key:
                return True
        return False
    
# Created the instance of program
program = Program()
program.run()