#include <stdio.h>
#include <stdlib.h>

// Here i've defined a constant wich represent the length 
// of an array.
#define N 4

// Global Variables
int solution[N];

// Prototypes
void see_solution(int solution[]);
int free_queen(int i, int j, int solution[]);
void queens_on_table(int j, int solution[]);

int main(){
  queens_on_table(0,solution);
  return 0;
}


void see_solution(int solution[]){
  //Var
  int i;

  //Begin
  for(i=0; i<N; i++){
    printf("Q%d ---> R%d - C%d\n", i+1, solution[i]+1, i+1);
  }
  puts("");
}


// This function verify if a queen can be in a 
// determine position (Verify if rows and diagonal are free_queen)
int free_queen(int i, int j, int solution[]){
  //Var
  int k, result;

  //Begin
  k = 0;
  result = 1;
  while(k < j && result) {
    if(solution[k] == i){
      result = 0;
    }
    if(abs(i - solution[k]) == abs(j - k)){
      result = 0;
    }
    k++;
  }
  return result;
}

// This function will find all solutions
// Here i've used the all solutions approach
void queens_on_table(int j, int solution[]){
  //Var 
  int i;
  //Begin
  i = 0;
  while(i < N){
    
    if(free_queen(i, j, solution)){
      solution[j] = i;
      if(j == N-1){
        see_solution(solution);
      }else{
        queens_on_table(j+1, solution);
      }
    }
    i++;
  }
  
}