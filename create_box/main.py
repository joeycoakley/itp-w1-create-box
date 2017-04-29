"""This is the entry point of the program."""

def create_box(height, width, character):
  my_string = ""
  for i in range(height):
    my_string = my_string + (character * width) + "\n"
  return my_string

		    

if __name__ == '__main__':
    create_box(3, 4, '*')
        
        
