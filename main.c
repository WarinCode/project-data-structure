#include <stdio.h>
#include <math.h>
#include <stdbool.h>

// declare all directives
#define SIZEOF_HASH_TABLE 10
#define EMPTY_VALUE -1

// declare the hash table
int hashTable[SIZEOF_HASH_TABLE];

// declare all prototype functions
void init();
int hash(int key);
void insert(int key);
void delete(int key);
void deleteAll();
void display();
void search(int key);
void linearProbing(int key, int index);
void quadraticProbing(int key, int index);
bool isEmptyCell(int index);
bool isEmpty();
bool isFull();
bool contains(int key);

int main(void) {
    //set Array value to -1 or Empty value
    init();

    // declare all variables
    int choice;
    int key;

    //Run Program
    while(true){
        printf("\nMenu\n");
        printf(" 1. Insert\n 2. Delete\n 3. Display\n 4. Search\n 5. Delete all\n 6. Exit\n");
        printf("Enter a number:");
        //get choice numbre
        scanf("%d", &choice);

        //case choice 
        switch(choice){
            //Insert data
            case 1:
                printf("Enter the key:");
                scanf("%d", &key);
                insert(key);
                break;
            //Delete data  set value back to -1
            case 2:
                printf("Enter the key:");
                scanf("%d", &key);
                delete(key);
                break;
            //Display whole Array
            case 3:
                display();
                break;
            //Search data in Array
            case 4:
                printf("Enter the key:");
                scanf("%d", &key);
                search(key);
                break;
            //Delete whole data from Array set value back to -1
            case 5:
                deleteAll();
                break;
            //Exit
            case 6:
                return 0;
            //Handle wrong choice number
            default:
                printf("Wrong choice please input the number between or 1 - 6 only!");
        }
    }

    return 0;
}


//Set All Index in Array to have value of -1
void init(){
    for(int i = 0; i < SIZEOF_HASH_TABLE; i++){
        hashTable[i] = EMPTY_VALUE;
    }
}

//Hash numerical Data
int hash(int key){
    return key % SIZEOF_HASH_TABLE;
}

//Insert numerical Data
void insert(int key){
    // call Hash function
    int index = hash(key);
    //Check if Full
    if(isFull()){
        printf("Hash table is full!\n");
        return;
    }
    //Check is Empty if True
    if(isEmptyCell(index)){
        hashTable[index] = key;
        printf("Inserted %d successfully.\n", key);
    //Check is Empty if False
    } else {
        //call linearProbing
        //linearProbing(key, index);
        quadraticProbing(key, index);
    }
}

//Delete numerical Data
void delete(int key){
    //Check if Data not in Array
    if(!contains(key)){
        printf("The key %d does not exist in the hash table.", key);
        return;
    }
    //Linear Search
    // //Check Data in Array by Default
    // for(int i = 0; i < SIZEOF_HASH_TABLE; i++){
    //     //Find Data in Array
    //     if(hashTable[i] == key){
    //         //get Data from Array
    //         int element = hashTable[i];
    //         //set Array's Data to -1
    //         hashTable[i] = EMPTY_VALUE;
    //         printf("Deleted %d successfully.", element);
    //         break;
    //     }
    // }

    //Hash table lookup
    int index = hash(key);
    //HashTable lookup 
    // For linear and Quadratic SEARCH
    int count = 0;
    int max_Size = SIZEOF_HASH_TABLE+1;

    //Avg case O(n/2)
    //Best Case O(1)
    //Worst case O(n+1)
    while(count < max_Size)
    {
        if(hashTable[index] == key)
        {
            
            hashTable[index] = EMPTY_VALUE;
            printf("Deleted %d successfully.", key);
            return;
        }
        else
        {
            

            //Quardatic indexing (Double size of index)
            index = count*2;
            //make index in Array Size
            int mod_index = index % SIZEOF_HASH_TABLE;

            //if count is exceed Array Size
            if (index >= SIZEOF_HASH_TABLE)
            {
                //make Linear indexing (index size is in Array)
                mod_index = (index-1)%(SIZEOF_HASH_TABLE);
            }
            //change index value to mod_index
            index = mod_index;
            count++;
        }
        // printf(" %d ",index);
    }

}

//Delete all numerical Data from Array
void deleteAll(){
    //Check if Array is Empty
    if(isEmpty()){
        printf("Hash table is empty!\n");
        return;
    }
    //Check if Array is not Empty by default
    for(int i = 0; i < SIZEOF_HASH_TABLE; i++){
        //Set Index to -1 
        hashTable[i] = EMPTY_VALUE;
    }
    printf("Deleted successfully.\n");
}

//Display whole Array
void display(){
    printf("\n-------------------\n");
    printf("    Index   Key\n\n");
    for(int i = 0; i < SIZEOF_HASH_TABLE; i++){
        //check if Data is -1 if Not Then  Display
        if(isEmptyCell(i)){
            printf("    [%d]     \n", i);
        } 
        else {
            printf("    [%d]    %d\n", i, hashTable[i]);
        }
    }
    printf("-------------------\n");
}

//LinearProb Function
void linearProbing(int key, int index){
    //Check if Index is not Empty
    while(!isEmptyCell(index)){
        //Set Index into next index
        index++;
        //not really need this
        if(index == SIZEOF_HASH_TABLE){
            //Keep Index in SIZE OF ARRAY
            index %= SIZEOF_HASH_TABLE;
        }
        //Check if Index is Empty by Default
        // if(isEmptyCell(index)){
        //     //Set Data to Index
        //     hashTable[index] = key;
        //     break;
        // }
    }
    //Index is Empty by Default Then Set Data to Index
    hashTable[index] = key;
    printf("Inserted %d successfully.\n", key);
}

//QuadraticProb Function
void quadraticProbing(int key, int index){
    //Set repettition value to 1
    int i = 1;
    int newIndex = index;

    //if index is not Empty(repettition)
    while(!isEmptyCell(newIndex)){
        // formular: (H(x) + i ** 2) / SIZE
        //Find new Index using formular
        
        //int newIndex = hash(index + ((int)pow(i, 2)));
        // if(isEmptyCell(newIndex)){
        //     hashTable[newIndex] = key;
        //     break;
        // }

        //Set NewIndex to New Index and modulo Size of 
        newIndex = (index + ((int)pow(i, 2))) % SIZEOF_HASH_TABLE;
        i++;
    }
    //index is Empty
    //Set Data to index
    hashTable[newIndex] = key;
    printf("Inserted %d successfully.\n", key);


    //the problem of Quardatic Probing is hash index can jump to its repettitive index therefore infinit loop
    //My solution ----
}

//Search Function
void search(int key){
    //if data in Array Then Found Else Not found.
    contains(key) ? printf("Found %d in the hash table", key) : printf("Not found %d in the hash table", key);
}

//Check if Index is Empty 
bool isEmptyCell(int index){
    return hashTable[index] == EMPTY_VALUE;
}

//Check if Array is Empty
bool isEmpty(){
    for(int i = 0; i < SIZEOF_HASH_TABLE; i++){
        if(hashTable[i] != EMPTY_VALUE) {
            return false;
        }
    }
    return true;
}

//Check if Array is Full
bool isFull(){
    int counter = 0;
    for(int i = 0; i < SIZEOF_HASH_TABLE; i++){
        if(hashTable[i] != EMPTY_VALUE){
            counter++;
        }
    }
    return counter == SIZEOF_HASH_TABLE;
}

//check Data is in Array ###should improve this to O(1)
bool contains(int key){
    int index = hash(key);
    // For Linear Serch
    // for(int i = 0; i < SIZEOF_HASH_TABLE; i++){
    //     if(hashTable[i] == key){
    //         return true;
    //     }
    // }

    //HashTable lookup 
    // For linear and Quadratic SEARCH
    int count = 0;
    int maxSize = SIZEOF_HASH_TABLE + 1;

    //Avg case O(n/2)
    //Best Case O(1)
    //Worst case O(n+1)
    while(count < maxSize){
        if(hashTable[index] == key){
            return true;
        } else {
            //Quardatic indexing (Double size of index)
            index = count * 2;
            //make index in Array Size
            int modIndex = index % SIZEOF_HASH_TABLE;

            //if count is exceed Array Size
            if (index >= SIZEOF_HASH_TABLE){
                //make Linear indexing (index size is in Array)
                modIndex = (index - 1) % SIZEOF_HASH_TABLE;
            }
            //change index value to mod_index
            index = modIndex;
            count++;
        }
        //printf("%d ",index);
    }

    return false;
}