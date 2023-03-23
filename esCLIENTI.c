#include <stdio.h>
#include<time.h>
#include<stdlib.h>
#include<string.h>

#define MIN 1
#define MAX 4
#define MINUTI_GIORNALIERI 720


typedef struct cliente{
    struct cliente *next;
    int tempo_necessario;
}Cliente;


void stampaCoda(Cliente *p){
    while(p != NULL){
        p = p->next;
    }
}

int is_empty(Cliente* head){
    if(head == NULL) return 1;
    else return 0;
}

void enqueue(Cliente** head, Cliente** tail, Cliente* element){
    if(is_empty(*head))
        *head = element;
    else
        (*tail)->next = element;

    *tail = element;
    element->next = NULL;
}

Cliente* dequeue(Cliente** head, Cliente** tail){
    Cliente* ret = *head;

    if(is_empty(*head))
        return NULL;
    else
        *head = ret->next;

    if(*head == NULL)
        *tail = NULL;

    return ret;
}

int main(){

    srand(time(NULL));



    int orario_lavorativo = MINUTI_GIORNALIERI;

    int k = 0;
    int temp = 0;

    Cliente *cliente;
    Cliente *testa = NULL;
    Cliente *coda = NULL;


    cliente= (Cliente*)malloc(sizeof(Cliente));
    cliente->tempo_necessario = rand()%(MAX-MIN+1)+MIN;
    printf("%d",cliente->tempo_necessario);
    int orario_per_cliente = rand()%(MAX-MIN+1)+MIN;
    printf("%d\n",orario_per_cliente);

    while(orario_lavorativo > 0 && orario_lavorativo >= orario_per_cliente){

        if (temp != 0){

            cliente->tempo_necessario = rand()%(MAX-MIN+1)+MIN;
            printf("%d",cliente->tempo_necessario);
            int orario_per_cliente = rand()%(MAX-MIN+1)+MIN;
            printf("%d\n",orario_per_cliente);
        }

        orario_lavorativo -= orario_per_cliente;

        if(orario_per_cliente < cliente->tempo_necessario){

            cliente->tempo_necessario-=orario_per_cliente;
            enqueue(&testa, &coda, cliente);


        }else if(orario_per_cliente >= cliente->tempo_necessario){

            orario_lavorativo+=(orario_per_cliente - cliente->tempo_necessario);
            dequeue(&testa,&coda);
            k++;


        }else{
            k++;

        }

        temp ++;

        int tempo_di_attesa = rand()%(MAX-MIN+1)+MIN;

        orario_lavorativo -= tempo_di_attesa;

    }

    printf("numero clienti serviti: %d😍", k);

    //funzione che fa' la free di tutto quello che c'è da fare!😍
    return 0;
}