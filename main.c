//
//  main.c
//  es01TPSIT
//  Creare un programma in linguaggio C che legga il file vgsales.csv e lo importi in un array di strutture.
//  Ogni riga contiene i campi separati da virgole, per cui può essere comodo creare una funzione split
//  che dalla riga letta ritorni la struttura valorizzata.
//  Created by Alexandru Zup on 13/09/22.
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define DIM 1024

typedef struct gioco{
    
    int rank;
    char* name;
    char* platform;
    int year;
    char* genre;
    char* publisher;
    float NA_sales;
    float EU_sales;
    float JP_sales;
    float Other_sales;
    float Global_sales;

}gioco;


int main() {
    
    gioco giochi[16600];
    gioco *a = giochi;
    
    char riga[DIM];
    FILE*fp;
    fp = fopen("/Users/zupy/Documents/Scuola/TPSIT/file.csv","r");
    if(fp == NULL){
        printf("WARNING!: Il file non esiste");
        return 0;
    }else{
        printf("WARNING!: sono dentro");
        fgets(riga, DIM, fp);
        while(fgets(riga, DIM, fp) != EOF){
            
            (*a).rank = atoi(strtok(riga, ","));
            (*a).name = strtok(NULL, ",");
            (*a).platform = strtok(NULL, ",");
            (*a).year = atoi(strtok(NULL, ","));
            (*a).genre = strtok(NULL, ",");
            (*a).publisher = strtok(NULL, ",");
            (*a).NA_sales = atof(strtok(NULL, ","));
            (*a).EU_sales = atof(strtok(NULL, ","));
            (*a).JP_sales = atof(strtok(NULL, ","));
            (*a).Other_sales = atof(strtok(NULL, ","));
            (*a).Global_sales = atof(strtok(NULL, ","));

            printf("\n %d, %s, %s, %d, %s, %s, %.3f, %.3f, %.3f, %.3f, %.3f", (*a).rank, (*a).name, (*a).platform, (*a).year, (*a).genre, (*a).publisher, (*a).NA_sales, (*a).EU_sales, (*a).JP_sales, (*a).Other_sales, (*a).Global_sales);
            
            a++;
        }
        fclose(fp);
    }
    return 0;
}












