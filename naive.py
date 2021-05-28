def naive(pattern: str, text: str, line_positions: [int]):
    line_number = 0
    next_line = line_positions[line_number]

    for pos, char in enumerate(text):
        if pos >= next_line:
            line_number += 1
            if line_number < len(line_positions):
                next_line = line_positions[line_number]

        if pattern == text[pos: pos+len(pattern)]:
            print("Found pattern at line", line_number)
