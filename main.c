#include <stdio.h>
#include <math.h>
#include <stdbool.h>

// declare all directives
#define SIZEOF_HASH_TABLE 11
#define EMPTY_VALUE -1

// declare the hash table
int hashTable[SIZEOF_HASH_TABLE] = {};

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
    init();

    // declare all variables
    int choice;
    int key;

    while(true){
        printf("\nMenu\n");
        printf(" 1. Insert\n 2. Delete\n 3. Display\n 4. Search\n 5. Delete all\n 6. Exit\n");
        printf("Enter a number:");
        scanf("%d", &choice);

        switch(choice){
            case 1:
                printf("Enter the key:");
                scanf("%d", &key);
                insert(key);
                break;
            case 2:
                printf("Enter the key:");
                scanf("%d", &key);
                delete(key);
                break;
            case 3:
                display();
                break;
            case 4:
                printf("Enter the key:");
                scanf("%d", &key);
                search(key);
                break;
            case 5:
                deleteAll();
                break;
            case 6:
                return 0;
            default:
                printf("Wrong choice please input the number between or 1 - 6 only!");
        }
    }

    return 0;
}

void init(){
    for(int i = 0; i < SIZEOF_HASH_TABLE; i++){
        hashTable[i] = EMPTY_VALUE;
    }
}

int hash(int key){
    return key % SIZEOF_HASH_TABLE;
}

void insert(int key){
    int index = hash(key);
    if(isFull()){
        printf("Hash table is full!\n");
        return;
    }
    if(isEmptyCell(index)){
        hashTable[index] = key;
        printf("Inserted %d successfully.\n", key);
    } else {
        linearProbing(key, index);
//        quadraticProbing(key, index);
    }
}

void delete(int key){
    if(!contains(key)){
        printf("The key %d does not exist in the hash table.", key);
        return;
    }
    for(int i = 0; i < SIZEOF_HASH_TABLE; i++){
        if(hashTable[i] == key){
            int element = hashTable[i];
            hashTable[i] = EMPTY_VALUE;
            printf("Deleted %d successfully.", element);
            break;
        }
    }
}

void deleteAll(){
    if(isEmpty()){
        printf("Hash table is empty!\n");
        return;
    }
    for(int i = 0; i < SIZEOF_HASH_TABLE; i++){
        hashTable[i] = EMPTY_VALUE;
    }
    printf("Deleted successfully.\n");
}

void display(){
    printf("\n-------------------\n");
    printf("    Index   Key\n\n");
    for(int i = 0; i < SIZEOF_HASH_TABLE; i++){
        if(isEmptyCell(i)){
            printf("[%d]     \n", i);
        } else {
            printf("[%d]    %d\n", i, hashTable[i]);
        }
    }
    printf("-------------------\n");
}

void linearProbing(int key, int index){
    while(!isEmptyCell(index)){
        index++;
        if(index == SIZEOF_HASH_TABLE){
            index %= SIZEOF_HASH_TABLE;
        }
        if(isEmptyCell(index)){
            hashTable[index] = key;
            break;
        }
    }
    printf("Inserted %d successfully.\n", key);
}

void quadraticProbing(int key, int index){
    int i = 1;
    while(!isEmptyCell(index)){
        // formular: (H(x) + i ** 2) / SIZE
        int newIndex = hash(index + ((int)pow(i, 2)));
        if(isEmptyCell(newIndex)){
            hashTable[newIndex] = key;
            break;
        }
        i++;
    }
    printf("Inserted %d successfully.\n", key);
}

void search(int key){
    contains(key) ? printf("Found %d in the hash table", key) : printf("Not found %d in the hash table", key);
}

bool isEmptyCell(int index){
    return hashTable[index] == EMPTY_VALUE;
}

bool isEmpty(){
    for(int i = 0; i < SIZEOF_HASH_TABLE; i++){
        if(hashTable[i] != EMPTY_VALUE) {
            return false;
        }
    }
    return true;
}

bool isFull(){
    int counter = 0;
    for(int i = 0; i < SIZEOF_HASH_TABLE; i++){
        if(hashTable[i] != EMPTY_VALUE){
            counter++;
        }
    }
    return counter == SIZEOF_HASH_TABLE;
}

bool contains(int key){
    for(int i = 0; i < SIZEOF_HASH_TABLE; i++){
        if(hashTable[i] == key){
            return true;
        }
    }
    return false;
}