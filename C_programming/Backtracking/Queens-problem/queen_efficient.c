#include <stdio.h>
#include <stdlib.h>
#define N 8

int solution[8] = {0,0,0,0,0,0,0,0};
int x = 0;
int *find_solution = &x;

int free_diagonal(int i , int j, int fila, int col){
    // Here j = solution[i] that means the column 
    // and i means the row
    if(abs(fila - i) == abs(col-j)){
        return 0;
    }else{
        return 1;
    }
}


int free_column(int col, int j){
    // Here j = solution[i] that means the column 
    if(col == j){
        return 0;
    }else{
        return 1;
    }
}

int verify(int fila, int col){
    int i;
    for(i=0; i <= fila - 1; i++){
        if(!free_column(col, solution[i]) || !free_diagonal(i, solution[i], fila, col)){
            return 0;
        }
    }
    return 1;
}

// When you call this procediment fila must be start in (zero 0)
// This is an agreement
void queen_in_table(int solution[], int fila, int *find_solution){
    // Var
    int col, i, flag;


    // Inicializando la alternativa
    col = 0;
    while(!*find_solution && col < 8){
        // alternativa valida
        flag = verify(fila, col);
        if(flag){
            // regitrar paso
            solution[fila] = col;

            // Verificar si ya se llego a la solución
            *find_solution = (fila == N - 1)? 1:0;

            if(!*find_solution){
                queen_in_table(solution, fila + 1, find_solution);
                if(!find_solution){
                    // borrar paso
                    solution[fila] = 0;
                }
            }else{
                // Imprimir solución
                    for(i=0; i < N; i++){
                        printf("Queen %d, row=%d column=%d\n",i+1, i+1, solution[i]+1);
                    }
            }
        }
        col++;
    }
}

int main(){
    // int solution[], int fila, int *find_solution
    queen_in_table(solution, 0, find_solution);
    return 0;
}