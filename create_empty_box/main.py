"""This is the entry point of the program."""

def create_empty_box(width, height, character):
  box = ""
  #Construct Top Line
  box = box + (character * width) + "\n"
  #Next, we build the body. Subtract 2 in order to account
  #for top and bottom lines.
  for i in range(height -2):
    box = box + (character + " " * (width - 2) + character + "\n")
  #Construct Bottom Line
  box = box + (character * width) + "\n"
  return box

		    

if __name__ == '__main__':
    create_empty_box(8, 8, '*')
    
        
