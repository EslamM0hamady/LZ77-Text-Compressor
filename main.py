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
