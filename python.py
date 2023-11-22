def justify_text(paragraph, page_width):
    words = paragraph.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        # If adding the next word exceeds the page width, append the current line to lines
        if current_length + len(word) + len(current_line) > page_width:
            lines.append(current_line)
            current_line = []
            current_length = 0

        current_line.append(word)
        current_length += len(word)

    # Append the last line if there are remaining words
    if current_line:
        lines.append(current_line)

    # Join the lines into left and right justified strings
    justified_lines = []
    for line in lines:
        total_spaces = page_width - sum(len(word) for word in line)
        spaces_between_words = len(line) - 1 if len(line) > 1 else 1
        space_per_word = total_spaces // spaces_between_words
        extra_spaces = total_spaces % spaces_between_words

        justified_line = ""
        for i, word in enumerate(line):
            justified_line += word
            if i < len(line) - 1:
                justified_line += " " * space_per_word
                if extra_spaces > 0:
                    justified_line += " "
                    extra_spaces -= 1

        justified_lines.append(justified_line)

    return justified_lines

# Example usage
paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
page_width = 20

justified_text = justify_text(paragraph, page_width)
for i, line in enumerate(justified_text, start=1):
    print(f"Array [{i}] = \"{line}\"")
