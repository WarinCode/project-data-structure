from math import pow
from abc import ABC, abstractmethod

# The `class Validator(ABC)` is defining an abstract base class (ABC) named `Validator`. This class
# contains abstract methods that must be implemented by any subclass that inherits from it
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

        
# The `class OpenAddressing(ABC)` is defining an abstract base class (ABC) named `OpenAddressing`.
# This class contains abstract methods that must be implemented by any subclass that inherits from it.
class OpenAddressing(ABC):
    @abstractmethod
    def linear_probing(self, key: int, index: int) -> None:
        ...

    @abstractmethod
    def quadratic_probing(self, key: int, index: int) -> None:
        ...

# The `class HashTable(ABC)` is defining an abstract base class (ABC) named `HashTable`. This class
# serves as a blueprint for creating hash table implementations. It contains abstract methods that
# must be implemented by any subclass that inherits from it.
class HashTable(ABC):
    # Declare all attributes
    _table = []
    _size = 0
    EMPTY_VALUE = -1

    # constructor method
    def __init__(self) -> None:
        # Loop to get the size of the table
        while self._size <= 0:
            try:
                self._size = int(input("Enter the size of hash table: "))
                raise
            # When an error occurs
            except ValueError:
                print("Error: Enter integer only!")
            except Exception:
                print("Error: The size cannot be a negative number or zero!")
        
        # Set All Index in Array to have value of -1
        for i in range(self._size):
            self._table.append(self.EMPTY_VALUE)

    # Hash numerical Data
    def hash(self, key: int) -> int:
        return key % self._size
    
    @abstractmethod
    def insert(self, key: int) -> None:
        ...

    @abstractmethod
    def delete(self, key: int) -> None:
        ...

    @abstractmethod
    def search(self, key: int) -> None:
        ...

    # Returns the size of the hash table
    def get_size(self) -> int:
        return self._size


# This class inherits from HashTable, Validator, and OpenAddressing classes in Python.
class Program(HashTable, Validator, OpenAddressing):
    # Declare all attributes
    _choice = None
    _key = None
    _runnable = True

    # Constructor method
    def __init__(self) -> None:
        # Call the constructor method of superclass
        super().__init__()

    # Run Program
    def run(self) -> None:
        while self._runnable:
            # Show menu
            print("\n Menu")
            print(" 1. Insert\n 2. Delete\n 3. Display\n 4. Search\n 5. Exit");
            try:
                # Get choice number
                self._choice = int(input("Enter a number: "))
                
                # Case choice
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
            # When an error occurs
            except ValueError:
                print("Error: Please enter only integers!")
            except AssertionError:
                print("Error: The size can't be a negative number or zero!")
            except Exception as e:
                print(e.__str__())
    
    def _enter_key(self) -> None:
        self._key = int(input("Enter the key: "))
        assert not self.is_negative_number(self._key) 

    # Method override: Insert numerical Data
    def insert(self, key) -> None:
        # Call Hash method
        index = self.hash(key)

        # Check if Full
        if self.is_full():
            print("Hash table is full!")
        # Check if it is a negative number
        elif self.is_negative_number(key):
            print("The key can't be entered as a negative number!")
        # Check is Empty if True
        elif self.is_empty_cell(index):
            self._table[index] = key
            print(f"Inserted {key} successfully.")
        # Check is Empty if False
        else:
            # Call linearProbing method
            self.linear_probing(key, index)
            # Call quadraticProbing method
            # self.quadratic_probing(key, index)

    # Method override: Delete numerical Data
    def delete(self, key) -> None:
        # Check if Array is Empty
        if self.is_empty():
            print("Hash table is empty!")
            return
        # Check if it is a negative number
        if self.is_negative_number(key):
            print("The key can't be entered as a negative number!")
            return
        # Check if Data not in Array
        if not self.contains(key):
            print(f"The key {key} does not exist in the hash table!")
            return
        
        # Linear Search
        # Check Data in Array by Default
        for i in range(self.get_size()):
            if self._table[i] == key:
                self._table[i] = self.EMPTY_VALUE
                print(f"Deleted {key} successfully.")
                break

    # Display whole Array
    def display(self) -> None:
        print("\n-------------------\n")
        print("    Index   Key\n")

        for i in range(self.get_size()):
            if self.is_empty_cell(i):
                print(f"    [{i}]     ")
            else:
                print(f"    [{i}]    {self._table[i]}")

        print("\n-------------------\n")

    # Method override: LinearProb method
    def linear_probing(self, key, index) -> None:
        # Check if Index is not Empty
        while not self.is_empty_cell(index):
            # Set Index into next index
            index += 1    
            # Not really need this
            if index == self.get_size():
                # Keep Index in SIZE OF ARRAY
                index %= self.get_size()
        # Index is Empty by Default Then Set Data to Index
        self._table[index] = key
        print(f"Inserted {key} successfully.")

    # Method override: QuadraticProb method
    def quadratic_probing(self, key, index) -> None:
        # Set repettition value to 1
        i = 1
        new_index = index
        
        # If index is not Empty(repettition)
        while not self.is_empty_cell(index):
            # Formular: (H(x) + i ** 2) / SIZE
            # Find new Index using formular

            # Set NewIndex to New Index and modulo Size of
            new_index = (index + pow(i, 2)) % self.get_size()
            i += 1
        # Index is Empty
        # Set Data to index
        self._table[new_index] = key
        print(f"Inserted {key} successfully.")

    # Method override: Search method
    def search(self, key) -> None:
        # If data in Array Then Found Else Not found
        if self.contains(key):
            print(f"Found {key} in the hash table.")
        else:
            print(f"Not found {key} in the hash table.")

    # Method override: Check if Index is Empty
    def is_empty_cell(self, index) -> bool:
        return self._table[index] == self.EMPTY_VALUE
    
    # Method override: Check if Array is Empty
    def is_empty(self) -> bool:
        for i in range(self.get_size()):
            if not self.is_empty_cell(i):
                return False
        return True
    
    # Method override: Check if Array is Full
    def is_full(self) -> bool:
        counter = 0
        for i in range(self.get_size()):
            if not self.is_empty_cell(i):
                counter += 1
        return counter == self._size

    # Method override: Check if a number is negative
    def is_negative_number(self, n) -> bool:
        return n < 0
    
    # Method override: Check Data is in Array #should improve this to O(1)
    def contains(self, key) -> bool:
        # For Linear Serch
        for i in range(self.get_size()):
            if self._table[i] == key:
                return True
        return False
    
# Created an instance of the program
program = Program()
# Run program
program.run()