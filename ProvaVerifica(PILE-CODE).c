#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

#define MAX_VAL 10
#define MIN_VAL 1
#define N_ELEM 5

typedef struct node {
    int NUMERO_ARRIVO;
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
    printf(" - arrivo: %d, numero %d\n", node->NUMERO_ARRIVO, node->VALORE);
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

void setStrutture(Node** head, Node** tail, Node** pila) {
    for(int i = 0; i < N_ELEM; i ++) {
        Node* nP = (Node*) malloc(sizeof(Node));
        Node* nC = (Node*) malloc(sizeof(Node));

        nP->NUMERO_ARRIVO = i + 1;
        nC->NUMERO_ARRIVO = i + 1;
        nP->VALORE = rand()%(MAX_VAL - MIN_VAL + 1) + MIN_VAL;
        nC->VALORE = rand()%(MAX_VAL - MIN_VAL + 1) + MIN_VAL;
        nP->next = NULL;
        nC->next = NULL;

        enqueue(head, tail, nC);
        push(pila, nP);
    }
}

int main() {
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

    while(!isEmpty(head) && !isEmpty(pila)) {
        Node* nPila = pop(&pila);
        Node* nCoda = dequeue(&head, &tail);
        nPila->next = NULL;
        nCoda->next = NULL;

        printf("scontro tra pila (ARRIVO: %d VALORE: %d) e coda (ARRIVO: %d VALORE: %d): ", nPila->NUMERO_ARRIVO, nPila->VALORE, nCoda->NUMERO_ARRIVO, nCoda->VALORE);
        if(nPila->VALORE > nCoda->VALORE) {
            nPila->VALORE -= nCoda->VALORE;
            printf("pila vince!! nuovo valore: %d\n", nPila->VALORE);
            free(nCoda);
            push(&pila, nPila);
        } else if(nCoda->VALORE > nPila->VALORE) {
            nCoda->VALORE -= nPila->VALORE;
            printf("coda vince!! nuovo valore %d\n", nCoda->VALORE);
            free(nPila);
            enqueue(&head, &tail, nCoda);
        } else {
            printf("pareggio!! entrambi eliminati\n");
            free(nPila);
            free(nCoda);
        }
    }

    printf("\n");
    if(isEmpty(pila) && isEmpty(head))
        printf("PARTITA FINITA IN PARAGGIO");
    else if(isEmpty(head)) {
        printf("PARTITA VINTA DALLA PILA!\n valori rimasti:\n");
        printNodes(pila);
    } else {
        printf("PARTITA VINTA DALLA CODA!\n valori rimasti:\n");
        printNodes(head);
    }

    freeNodes(pila);
    freeNodes(head);

    return 0;
}