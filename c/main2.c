#include <stdio.h>
#include <math.h>

// Declare all constant values
#define EMPTY_VALUE -1
int size = 0;

// Declare all prototype functions
void init(int hashTable[]);
int hash(int key);
void insert(int key, int hashTable[]);
void delete(int key, int hashTable[]);
void deleteAll(int hashTable[]);
void display(int hashTable[]);
void search(int key, int hashTable[]);
void linearProbing(int key, int index, int hashTable[]);
void quadraticProbing(int key, int index, int hashTable[]);
bool isEmptyCell(int index, int hashTable[]);
bool isEmpty(int hashTable[]);
bool isFull(int hashTable[]);
bool isNegativeNumber(int number);
bool isInteger(int number);
bool contains(int key, int hashTable[]);
int getNumberofKeys();

int main(void) {
    while(isNegativeNumber(size)){
        printf("Enter number:");
        scanf("%d", &size);
        if(isNegativeNumber(size)){
            printf("Error size of hash table is can't negative or zero!\n");
        }
    }
    int hashTable[size];

    // Set Array value to -1 or Empty value
    init(hashTable);

    // Declare all variables
    int choice;
    int key;
    bool runnable = true;

    // Run Program
    while(runnable){
        printf("\n  Menu\n");
        printf(" 1. Insert\n 2. Delete\n 3. Display\n 4. Search\n 5. Delete all\n 6. Exit\n");
        printf("Enter a number:");
        // Get choice number
        scanf("%d", &choice);

        // Case choice
        switch(choice){
            // Insert data
            case 1:
                printf("Enter the key:");
                scanf("%d", &key);
                insert(key, hashTable);
                break;
                // Delete data set value back to -1
            case 2:
                printf("Enter the key:");
                scanf("%d", &key);
                delete(key, hashTable);
                break;
                // Display whole Array
            case 3:
                display(hashTable);
                break;
                // Search data in Array
            case 4:
                printf("Enter the key:");
                scanf("%d", &key);
                search(key, hashTable);
                break;
                // Delete whole data from Array set value back to -1
            case 5:
                deleteAll(hashTable);
                break;
                // Exit
            case 6:
                runnable = false;
                break;
                // Handle wrong choice number
            default:
                printf("Wrong choice please input the number between or 1 - 6 only!");
        }
    }

    return 0;
}


// Set All Index in Array to have value of -1
void init(int hashTable[]){
    for(int i = 0; i < size; i++){
        hashTable[i] = EMPTY_VALUE;
    }
}

// Hash numerical Data
int hash(int key){
    return key % size;
}

// Insert numerical Data
void insert(int key, int hashTable[]){
    // Call Hash function
    int index = hash(key);
    // Check if Full
    if(isFull(hashTable)){
        printf("Hash table is full!\n");
    }
        // Check if it is a negative number
    else if(isNegativeNumber(key)){
        printf("The key can't be entered as a negative number!\n");
    }
        // Check is Empty if True
    else if(isEmptyCell(index, hashTable)){
        hashTable[index] = key;
        printf("Inserted %d successfully.\n", key);
        // Check is Empty if False
    } else {
        // Call linearProbing function
        linearProbing(key, index, hashTable);
        // Call quadraticProbing function
        // quadraticProbing(key, index);
    }
}

// Delete numerical Data
void delete(int key, int hashTable[]){
    // Check if Array is Empty
    if(isEmpty(hashTable)){
        printf("Hash table is empty!\n");
        return;
    }
    // Check if it is a negative number
    if(isNegativeNumber(key)){
        printf("The key can't be entered as a negative number!\n");
        return;
    }
    // Check if Data not in Array
    if(!contains(key, hashTable)){
        printf("The key %d does not exist in the hash table!\n", key);
        return;
    }

    // Linear Search
    // Check Data in Array by Default
    // for(int i = 0; i < size; i++){
    //     // Find Data in Array
    //     if(hashTable[i] == key){
    //         // Get Data from Array
    //         int temp = hashTable[i];
    //         // Set Array's Data to -1
    //         hashTable[i] = EMPTY_VALUE;
    //         printf("Deleted %d successfully.", temp);
    //         break;
    //     }
    // }

    // Hash table lookup
   int index = hash(key);
    // HashTable lookup
    // For linear and Quadratic SEARCH
   int count = 0;
   int maxSize = size + 1;

    // Avg case O(n/2)
    // Best Case O(1)
    // Worst case O(n+1)
    while(count < maxSize){
        if(hashTable[index] == key){
           hashTable[index] = EMPTY_VALUE;
           printf("Deleted %d successfully.", key);
           return;
        } else {
            // Quardatic indexing (Double size of index)
            index = count * 2;
            // Make index in Array Size
            int modIndex = index % size;
            // If count is exceed Array Size
            if (index >= size){
               // Make Linear indexing (index size is in Array)
               modIndex = (index - 1) % size;
            }
            // Change index value to modIndex
            index = modIndex;
            count++;
        }
       // printf(" %d ",index);
    }
}

// Delete all numerical Data from Array
void deleteAll(int hashTable[]){
    // Check if Array is Empty
    if(isEmpty(hashTable)){
        printf("Hash table is empty!\n");
        return;
    }
    // Check if Array is not Empty by default
    for(int i = 0; i < size; i++){
        // Set Index to -1
        hashTable[i] = EMPTY_VALUE;
    }
    printf("Deleted successfully.\n");
}

// Display whole Array
void display(int hashTable[]){
    printf("\n-------------------\n");
    printf("    Index   Key\n\n");
    for(int i = 0; i < size; i++){
        // Check if Data is -1 if Not Then Display
        isEmptyCell(i, hashTable) ? printf("    [%d]     \n", i) : printf("    [%d]    %d\n", i, hashTable[i]);
    }
    printf("-------------------\n");
}

// LinearProb Function
void linearProbing(int key, int index, int hashTable[]){
    // Check if Index is not Empty
    while(!isEmptyCell(index, hashTable)){
        // Set Index into next index
        index++;
        // Not really need this
        if(index == size){
            // Keep Index in SIZE OF ARRAY
            index %= size;
        }
    }
    // Index is Empty by Default Then Set Data to Index
    hashTable[index] = key;
    printf("Inserted %d successfully.\n", key);
}

// QuadraticProb Function
void quadraticProbing(int key, int index, int hashTable[]){
    // Set repettition value to 1
    int i = 1;
    int newIndex = index;

    // if index is not Empty(repettition)
    while(!isEmptyCell(newIndex, hashTable)){
        // Formular: (H(x) + i ** 2) / SIZE
        // Find new Index using formular

        // Set NewIndex to New Index and modulo Size of
        newIndex = (index + ((int)pow(i, 2))) % size;
        i++;
    }
    // Index is Empty
    // Set Data to index
    hashTable[newIndex] = key;
    printf("Inserted %d successfully.\n", key);
}

// Search Function
void search(int key, int hashTable[]){
    // If data in Array Then Found Else Not found.
    contains(key, hashTable) ? printf("Found %d in the hash table.\n", key) : printf("Not found %d in the hash table.\n", key);
}

// Check if Index is Empty
bool isEmptyCell(int index, int hashTable[]){
    return hashTable[index] == EMPTY_VALUE;
}

// Check if Array is Empty
bool isEmpty(int hashTable[]){
    for(int i = 0; i < size; i++){
        if(hashTable[i] != EMPTY_VALUE) {
            return false;
        }
    }
    return true;
}

// Check if Array is Full
bool isFull(int hashTable[]){
    int counter = 0;
    for(int i = 0; i < size; i++){
        if(hashTable[i] != EMPTY_VALUE){
            counter++;
        }
    }
    return counter == size;
}

// Check if a number is negative
bool isNegativeNumber(int number){
    return number <= 0;
}

// Check Data is in Array #should improve this to O(1)
bool contains(int key, int hashTable[]){
    // For Linear Serch
    // for(int i = 0; i < size; i++){
    //     if(hashTable[i] == key){
    //         return true;
    //     }
    // }
    // return false;

    // HashTable lookup
    // For linear and Quadratic SEARCH
   int count = 0;
   int maxSize = size + 1;

    // Avg case O(n/2)
    // Best Case O(1)
    // Worst case O(n+1)

   int index = hash(key);
   while(count < maxSize){
       if(hashTable[index] == key){
           return true;
       } else {
           // Quardatic indexing (Double size of index)
           index = count * 2;
           // Make index in Array Size
           int modIndex = index % size;

           // If count is exceed Array Size
           if (index >= size){
               // Make Linear indexing (index size is in Array)
               modIndex = (index - 1) % size;
           }
           // Change index value to mod_index
           index = modIndex;
           count++;
       }
       //printf("%d ",index);
   }

   return false;
}