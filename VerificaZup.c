#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include <string.h>

#define MAX_VAL 10
#define MIN_VAL 1
#define N_ELEM 4

typedef struct node {
    char* NOME;
    int VALORE;
    struct node* next;
} Node;

bool isEmpty(Node* node) {
    return node == NULL;
}

void freeNodes(Node* node) {
    if(node == NULL)
        return;
    if(node->next != NULL)
        freeNodes(node->next);
    free(node);
}

void printNodes(Node* node) {
    if(isEmpty(node))
        return;
    printf(" - nome: %s, numero %d\n", node->NOME, node->VALORE);
    if(node->next != NULL)
        printNodes(node->next);
}

void enqueue(Node** head, Node** tail, Node* el) {
    if(isEmpty(*head))
        *head = el;
    else
        (*tail)->next = el;
    *tail = el;
    el->next = NULL;

}

Node* dequeue(Node** head, Node** tail) {
    Node* ret = *head;
    if(isEmpty(*head))
        return NULL;
    *head = ret->next;
    if(isEmpty(*head))
        *tail = NULL;
    return ret;
}

void push(Node** head, Node* el) {
    if(!isEmpty(*head))
        el->next = *head;
    else
        el->next = NULL;
    *head = el;
}

Node* pop(Node** head) {
    if(isEmpty(*head))
        return  NULL;
    Node* ret = *head;
    *head = ret->next;
    ret->next = NULL;
    return ret;
}

//inizializzo le strutture con il nome che si imposta tramite il for e il valore assegnato random
void setStrutture(Node** head, Node** tail, Node** pila) {
    for(int i = 0; i < N_ELEM; i ++) {
        Node* nP = (Node*) malloc(sizeof(Node));
        Node* nC = (Node*) malloc(sizeof(Node));

        nP->NOME = "P";
        nC->NOME = "C";
        nP->VALORE = rand()%(MAX_VAL - MIN_VAL + 1) + MIN_VAL;
        nC->VALORE = rand()%(MAX_VAL - MIN_VAL + 1) + MIN_VAL;
        nP->next = NULL;
        nC->next = NULL;

        enqueue(head, tail, nC);
        push(pila, nP);
    }
}

int main (){
    srand(time(NULL));

    Node* head = NULL;
    Node* tail = NULL;
    Node* pila = NULL;

    setStrutture(&head, &tail, &pila);
    printf("coda:\n");
    printNodes(head);
    printf("\npila:\n");
    printNodes(pila);
    printf("\n");

    Node* headSmaller = NULL;
    Node* tailSmaller = NULL;
    Node* pilaMaggior = NULL;

    while(!isEmpty(head) && !isEmpty(pila)) {
        Node* nPila = pop(&pila);
        Node* nCoda = dequeue(&head, &tail);
        nPila->next = NULL;
        nCoda->next = NULL;

        printf("scontro tra pila (NOME: %s VALORE: %d) e coda (NOME: %s VALORE: %d): ", nPila->NOME, nPila->VALORE, nCoda->NOME, nCoda->VALORE);
        printf("\n");
        if(nPila->VALORE > nCoda->VALORE) {
            printf("pila vince!!, coda finisce nella coda dei minori, pila finisce nella pila dei maggiori");
            printf("\n");
            push(&pilaMaggior, nPila);
            enqueue(&headSmaller, &tailSmaller, nCoda);
            //free(nCoda);
        } else if(nCoda->VALORE > nPila->VALORE) {
            printf("coda vince!!, coda finisce nella pila dei maggiori, pila finisce nella coda dei minori");
            printf("\n");
            push(&pilaMaggior, nCoda);
            enqueue(&headSmaller, &tailSmaller, nPila);
            //free(nPila);
        } else {
            printf("pareggio!! entrambi eliminati\n");
            free(nPila);
            free(nCoda);
        }
    }

    printf("\n");
    printf("CODA_MINORI:\n");
    printNodes(headSmaller);
    printf("\nPILA_MAGGIORI:\n");
    printNodes(pilaMaggior);

    freeNodes(pila);
    freeNodes(head);
    freeNodes(headSmaller);
    freeNodes(pilaMaggior);
}