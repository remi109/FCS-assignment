#ex 2
def generate_combinations(characters, n, current_string=""):
      # Base case: if the current string is of length n, print it
      if len(current_string) == n:
          print(current_string)
          return

      # Recursive case: for each character, append it to the current string and recurse:
      for char in characters:
          generate_combinations(characters, n, current_string + char)
#Example usage:
characters = ['a', 'b', 'c']
n = 2
generate_combinations(characters, n)