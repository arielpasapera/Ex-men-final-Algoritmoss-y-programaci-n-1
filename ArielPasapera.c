#include <stdio.h>

void hallar_max_min(int array[], int n, int* max, int* min){
    
    for (int i = 0; i < n; i++){
        if (array[i] > array[i+1]){
           *max = array[i];

        }
        else if (array[i] < array[i+1]){
            *min = array[i];
        }
    }
 

    printf("\nEl numero maximo del array es: %d", *max);
    printf("\nEl numero minimo del array es: %d", *min);
}
    

int main(){
    int n = 5;
    int max;
    int min;
    int array[] = {12,24,10,98,32};
    hallar_max_min(array, n, &max, &min);

    return 0;
}