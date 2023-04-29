# N represent the length of the solution array.
N = 4

# "solution" is the array where i'll put each solution.
solution = [None] * N

# This procedure print each solution.
def see_queens(solution):
  for i in range(N):
    print(f"Q{i+1} ---> C{i+1} - R{solution[i]+1}")
  print("\n")

# This function verify if a queen can be in a determine position
#(It verify the row and diagonal)
def free_queen(i, j, solution):
  #Var
  #Begin
  k = 0
  result = True
  while(k < j and result):
    if(solution[k] == i): # Verifying the row.
      result = False
    if(abs(i - solution[k]) == abs(j - k)): # Verifying the diagonal.
      result = False
    k += 1
  return result

# Main funtion which use backtracking to solve the problem queens.
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

# Calling to main function.
queens_on_table(0,solution)