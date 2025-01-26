Definitions:
- Letter: A letter
- Cell: A section of the board that contains a collection of letters
- Board: a collection of cells
- Shift: Move the letters within the same board
- Shuffle: Move the boards within the collection
- Line Append: Appending style that puts the information about spaces for each line at the end of each line
- End Append: Appending style that puts the information about spaces for the entire document/message at the end of the entire file
- Seed and Key are used interchangably in this situatiom. Both will be the same value, but have multiple uses. Key is for decoding the message, while the seed is used for configuring the program to process the message properly, but Key and Seed will always have the same values.

Objects: 
- Letter: Contains nothing other than the letter itself, and MAYBE it's position
- Cell: Contains a collection 9 letters, and MAYBE it's position
- Board: Contains a collection of all cells (should be 10 cells in this version, other version can have more or less)

  Psuedo code
  ```
  # Encryption
  # board generation
  Enter/Detect seed
  if no seed, generate random seed
  manip is either bit or enum
  if seed prime manip = 11 (both)
  elif seed even: manip = 10 (shift)
  elif seed odd: manip = 01 (shuffle)
  elif seed 0/undefined: manip = 00 (none)
  else: Error catch, though it should never get here

  while cells in board to process:
      choose random cell
      while letters in cell to process:
          choose random letter and append it to currently active cell on new board

  # message generation THIS PART WILL HAVE TO CHANGE SLIGHTLY TO TAKE CARE OF THE DIFFERENT APPEND TYPES
  for each letter in message:
      if it is a space, add to space count and save space position for later
      find position in original board
      use position info from original board to find new letter on new board
  remove spaces from message using remove()/replace()
  output to file
  ```

  ```
  # Decryption
  # board generation
  Same as encryption board generation
  For each letter in the encryption, use the position on the NEW board to find the original letter on the original board
  Put the spaces back into the message
  ```
