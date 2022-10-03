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
    gioco *a;
    a = giochi;
    int k = 0;

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

            (a +k)->rank = atoi(strtok(riga, ","));
            (a +k)->name = strtok(NULL, ",");
            (a +k)->platform = strtok(NULL, ",");
            (a +k)->year = atoi(strtok(NULL, ","));
            (a +k)->genre = strtok(NULL, ",");
            (a +k)->publisher = strtok(NULL, ",");
            (a +k)->NA_sales = atof(strtok(NULL, ","));
            (a +k)->EU_sales = atof(strtok(NULL, ","));
            (a +k)->JP_sales = atof(strtok(NULL, ","));
            (a +k)->Other_sales = atof(strtok(NULL, ","));
            (a +k)->Global_sales = atof(strtok(NULL, ","));

            printf("\n %d, %s, %s, %d, %s, %s, %.3f, %.3f, %.3f, %.3f, %.3f", (a +k)->rank, (a +k)->name, (a +k)->platform, (a +k)->year, (a +k)->genre, (a +k)->publisher, (a +k)->NA_sales, (a +k)->EU_sales, (a +k)->JP_sales, (a +k)->Other_sales, (a +k)->Global_sales);

            k++;
        }
        fclose(fp);
    }
    return 0;
}
