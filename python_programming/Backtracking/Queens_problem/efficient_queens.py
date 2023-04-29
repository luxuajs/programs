
N = 4

solution = [None] * N

def see_queens(solution):
  for i in range(N):
    print(f"Q{i+1} ---> C{i+1} - R{solution[i]+1}")
  print("\n")
def free_queen(i, j, solution):
  #Var
  #Begin
  k = 0
  result = True
  while(k < j and result):
    if(solution[k] == i):
      result = False
    if(abs(i - solution[k]) == abs(j - k)):
      result = False
    k += 1
  return result

def queens_on_table(j, solution):
  #Var
  #Begin
  i = 0
  while(i < N):
    if(free_queen(i,j,solution)):
      solution[j] = i
      if(j == N-1):
        see_queens(solution)
      else:
        queens_on_table(j+1, solution)
    i += 1
queens_on_table(0,solution)