import sys


def lz77_compress(text, search_buffer_size=31, lookahead_buffer_size=15):
  compressed = []
  i = 0

  while i < len(text):
    match_length = 0
    match_offset = 0

    # search for the longest match in the search buffer
    for j in range(max(0, i - search_buffer_size), i):
      length = 0
      while (length < lookahead_buffer_size and
            i + length < len(text) and 
            text[j + length] == text[i + length]):
        length += 1

      if length > match_length or (length == match_length and i - j < match_offset):
        match_length = length
        match_offset = i - j

    # get next symbol after the match
    if i + match_length < len(text):
      next_symbol = text[i + match_length]
    else:
      next_symbol = "NULL"

    # add the tuple to compressed data
    compressed.append((match_offset, match_length, next_symbol))

    i += match_length + 1

  return compressed


def show_menu():
  # Display the main program menu
  print("====================================")
  print("          LZ77 Compression          ")
  print("====================================")
  print("1. Compress Text")
  print("2. Decompress Text")
  print("3. Exit")
  print("====================================")


def main():
  while True:
    show_menu()

    # Get user choice and handle invalid input
    try:
      choice = int(input("Please enter your choice: "))
    except ValueError:
      print("Invalid input! Please enter a number.\n")
      continue

    if choice == 1:
      # Compress input text using LZ77
      text = str(input("Please enter the text: "))
      compressed_data = lz77_compress(text)
      print(f"Compressed data: {compressed_data}\n")

    elif choice == 2:
      # Collect tags for decompression
      number_of_tags = int(input("Please enter number of tags: "))
      print("Enter offset, length, and next symbol (separated by space): ")
      tags = []

      for i in range(number_of_tags):
        offset, length, next_symbol = input().split()
        tags.append((int(offset), int(length), next_symbol))
      
      print(tags)

    elif choice == 3:
      print("\nExiting program. Goodbye!")
      sys.exit(0)

    else:
      print("Invalid choice! Please try again.")


# Entry point of the program
if __name__ == "__main__":
  main()
