from abc import ABC, abstractmethod

# The `class Validator(ABC)` is defining an abstract base class (ABC) named `Validator`. This class
# contains abstract methods that must be implemented by any subclass that inherits from it
class Validator(ABC):
    # Declare all abstract methods
    @abstractmethod
    def is_empty_cell(self, index: int) -> bool: 
        ...

    @abstractmethod
    def is_empty(self) -> bool: 
        ...
    
    @abstractmethod
    def is_full(self) -> bool: 
        ...

    @abstractmethod
    def find_key(self, key: int) -> bool: 
        ...

    # Check if a number is negative
    def is_negative(self, n: int) -> bool: 
        return n < 0
        
    # Check if a number is zero
    def is_zero(self, n: int) -> bool:
        return n == 0

# The `class OpenAddressing(ABC)` is defining an abstract base class (ABC) named `OpenAddressing`.
# This class contains abstract methods that must be implemented by any subclass that inherits from it.
class OpenAddressing(ABC):
    # Dict variable for addressing 
    types_of_addressing = {
        "linear": "Linear Probing", 
        "quadratic": "Quadratic Probing"
    }
    # Selecte Linear probing by default
    select_type = types_of_addressing["linear"]
    
    # Sets the type of addressing
    def _set_addressing(self) -> None:
        # Show information
        print(f"You are selecting {self.select_type}.")
        print("Please select 'linear' or 'quadratic' only.")

        key = None
        # When the address type is invalid
        while key not in self.types_of_addressing:
            key = input("Select a type of addressing: ")
            # Check if the key does not match the specified type.
            if key not in self.types_of_addressing:
                print("Invalid type please enter again!")
        # Assign a new value
        self.select_type = self.types_of_addressing[key]

    # Declare all abstract methods
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
        while self.get_size() <= 0:
            try:
                self.__set_size(int(input("Enter the size of hash table: ")))
                if self.get_size() <= 0: 
                    raise
            # When an error occurs
            except ValueError:
                print("Error: Enter an integer number only!")
            except Exception:
                print("Error: The size can't be a negative number or zero!")
       
        # Set All Index in Array to have value of -1
        for i in range(self.get_size()):
            self._table.append(self.EMPTY_VALUE)

    # Hash numerical Data
    def hash(self, key: int) -> int:
        return key % self.get_size()
    
    # Returns the size of the hash table
    def get_size(self) -> int:
        return self._size

    # Sets the size attribute of an object to the specified integer value
    def __set_size(self, size: int) -> None:
        self._size = size

    # Declare all abstract methods
    @abstractmethod
    def insert(self, key: int) -> None: 
        ...

    @abstractmethod
    def delete(self, key: int) -> None: 
        ...

    @abstractmethod
    def search(self, key: int) -> None: 
        ...


class Choices:
    # Declare all constant attributes
    INSERT = 1
    DELETE = 2
    DISPLAY = 3
    SEARCH = 4
    EXIT = 5

    # Display a menu of options to the user.
    @staticmethod
    def show_menu() -> None:
        print("\n Menu")
        # Keep list of menu
        menus = ("Insert", "Delete", "Display", "Search", "Exit")
        # Show each menu
        for i in range(len(menus)):
            print(f"{i + 1}.) {menus[i]}")


# This class inherits from HashTable, Validator, and OpenAddressing classes in Python.
class Program(HashTable, Validator, OpenAddressing):
    # Declare all attributes
    _choice = None
    _key = None
    _runnable = True

    # Constructor method
    def __init__(self) -> None:
        # Call the constructor method of superclass (HashTable)
        super().__init__()
        self._set_addressing()

    # Run Program
    def run(self) -> None:
        while self._runnable:
            # Show menu
            Choices.show_menu()
            try:
                # Get choice number
                self.__set_choice(int(input("Enter a number: ")))

                # Case choice
                # Insert data
                if self.get_choice() == Choices.INSERT:
                    self._input_key()
                    self.insert(self.get_key())
                    
                # Delete data set value back to -1
                elif self.get_choice() == Choices.DELETE:
                    self._input_key()
                    self.delete(self.get_key())
                    
                # Display whole Array
                elif self.get_choice() == Choices.DISPLAY:
                    self.display()
                    
                # Search data in Array
                elif self.get_choice() == Choices.SEARCH:
                    self._input_key()
                    self.search(self.get_key())
                    
                # Select address type
                elif self.get_choice() == Choices.EXIT:
                    self._runnable = False
                    print("Exited the program.")
                    self._set_addressing()
                    print("Successfully changed the address type.")
                # Handle wrong choice number
                else:
                    raise Exception("Error: Wrong choice please input the number between 1 - 5 only!")
                
            # When an error occurs
            except ValueError:
                print("Error: Please enter integer only!")
            except AssertionError:
                print("Error: The size can't be a negative number or zero!")
            except Exception as e:
                print(e.__str__())

    # Prompts the user to enter a key and ensures that the key isn't a negative number
    def _input_key(self) -> None:
        # Set the key
        self.__set_key(int(input("Enter the key: ")))
        # Check that the number must be an integer, otherwise an AssertionException will occur.
        assert not self.is_negative(self.get_key()) or not self.is_zero(self.get_key())

    # Returns the choice number
    def get_choice(self) -> int:
        return self._choice

    # Sets the value of choice
    def __set_choice(self, choice: int) -> None:
        self._choice = choice

    # Returns the key value
    def get_key(self) -> int:
        return self._key

    # Sets the value of key
    def __set_key(self, key: int) -> None:
        self._key = key

    # Override: Insert numerical Data
    def insert(self, key: int) -> None:
        # Call Hash method
        index = self.hash(key)

        # Check if Full
        if self.is_full():
            print("Hash table is full!")
        # Check if it is a negative number
        elif self.is_negative(key):
            print("Error: The key can't be entered as a negative number!")
        # Check is Empty if True
        elif self.is_empty_cell(index):
            self._table[index] = key
            print(f"Inserted {key} successfully.")
            self.display()
        # Check is Empty if False and the Key collided in the hash table
        else:
            if self.select_type == self.types_of_addressing["linear"]:
                # Call linearProbing method
                self.linear_probing(key, index)
            elif self.select_type == self.types_of_addressing["quadratic"]:
                # Call quadraticProbing method
                self.quadratic_probing(key, index)
            self.display()
            print(f"Inserted {key} successfully.")

    # Override: Delete numerical Data
    def delete(self, key: int) -> None:
        # Check if Array is Empty
        if self.is_empty():
            print("Hash table is empty!")
            return
        # Check if it is a negative number
        if self.is_negative(key):
            print("Error: The key can't be entered as a negative number!")
            return
        # Check if Data not in Array
        if not self.find_key(key):
            print(f"Error: The key {key} does not exist in the hash table!")
            return
                
        # Linear Search
        # Check Data in Array by Default
        for i in range(self.get_size()):
            if self._table[i] == key:
                self._table[i] = self.EMPTY_VALUE
                print(f"Deleted {key} successfully.")
                break
            
        # Hash table lookup
        # index = self.hash(key)
        # HashTable lookup
        # For linear and Quadratic SEARCH
        # count = 0
        # max_size = self.get_size() + 1

        # Avg case O(n/2)
        # Best Case O(1)
        # Worst case O(n+1)
        
        # while count < max_size:
        #     if self._table[index] == key:
        #         self._table[index] = self.EMPTY_VALUE;
        #         print(f"Deleted {key} successfully.");
        #         return
        #     else:
        #         # Quardatic indexing (Double size of index)
        #         index = count * 2;
        #         # Make index in Array Size
        #         mod_index = index % self.get_size();
        #         # If count is exceed Array Size
        #         if index >= self.get_size():
        #             # Make Linear indexing (index size is in Array)
        #             mod_index = (index - 1) % self.get_size();
                
        #         # Change index value to modIndex
        #         index = mod_index;
        #         count += 1
            
        #     print(index);
    
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

    # Override: LinearProb method
    def linear_probing(self, key: int, index: int) -> None:
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

    # Override: QuadraticProb method
    def quadratic_probing(self, key: int, index: int) -> None:
        # Set repettition value to 1
        i = 1
        new_index = index

        # If index is not Empty(repettition)
        while not self.is_empty_cell(new_index):
            # Formular: (H(x) + i ^ 2) % SIZE
            # Find new Index using formular
            # Set NewIndex to New Index and modulo Size of
            new_index = self.hash(index + (i ** 2))
            i += 1
        # Index is Empty
        # Set Data to index
        self._table[new_index] = key

    # Override: Search method
    def search(self, key: int) -> None:
        # If data in Array Then Found Else Not found
        if self.find_key(key):
            print(f"Found {key} in the hash table.")
        else:
            print(f"Not found {key} in the hash table.")

    # Override: Check if Index is Empty
    def is_empty_cell(self, index: int) -> bool:
        return self._table[index] == self.EMPTY_VALUE

    # Override: Check if Array is Empty
    def is_empty(self) -> bool:
        # Check if size of hash table is zero number
        if self.is_zero(len(self._table)):
            return True
        # Loop to find empty value
        for i in range(self.get_size()):
            if not self.is_empty_cell(i):
                return False
        return True

    # Override: Check if Array is Full
    def is_full(self) -> bool:
        return self.is_zero(self._table.count(self.EMPTY_VALUE))
        
        # For Linear Serch
        # counter = 0
        # for i in range(self.get_size()):
        #     if not self.is_empty_cell(i):
        #         counter += 1
        # return counter == self._size

    # Override: Check Data is in Array #should improve this to O(1)
    def find_key(self, key: int) -> bool:
        return key in self._table
    
        # For Linear Serch
        # for i in range(self.get_size()):
        #     if self._table[i] == key:
        #         return True
        # return False
        
        # HashTable lookup
        # For linear and Quadratic SEARCH
        # count = 0
        # max_size = self.get_size() + 1;

        # Avg case O(n/2)
        # Best Case O(1)
        # Worst case O(n+1)

        # index = self.hash(key)
        # while count < max_size:
        #     if self._table[index] == key:
        #         return True;
        #     else: 
        #         # Quardatic indexing (Double size of index)
        #         index = count * 2;
        #         # Make index in Array Size
        #         mod_index = index % self.get_size();

        #         # If count is exceed Array Size
        #     if index >= self.get_size():
        #         # Make Linear indexing (index size is in Array)
        #         mod_index = (index - 1) % self.get_size();
        #         # Change index value to mod_index
        #         index = mod_index;
        #         count += 1;
        #     print(index);
        
        # return False;


# Creating an instance of a Program class and assigning it to the variable
program = Program()
# Running a program with run method
program.run()