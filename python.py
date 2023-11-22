def justify_paragraph(paragraph, width):
    words = paragraph.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) <= width:
            current_line.append(word)
            current_length += len(word)
        else:
            lines.append(current_line)
            current_line = [word]
            current_length = len(word)

    if current_line:
        lines.append(current_line)

    justified_lines = []
    for idx, line in enumerate(lines, 1):
        if len(line) == 1 or len(line) == width:  # Single word or full line
            justified_lines.append(f"Array [{idx}] = {' '.join(line).ljust(width)}")
        else:
            spaces_needed = width - sum(len(word) for word in line)
            num_gaps = len(line) - 1
            spaces_between_words = spaces_needed // num_gaps
            extra_spaces = spaces_needed % num_gaps
            justified_line = ""
            for i in range(len(line) - 1):
                justified_line += line[i] + ' ' * (spaces_between_words + (1 if i < extra_spaces else 0))
            justified_line += line[-1]
            justified_lines.append(f"Array [{idx}] = {justified_line}")

    return justified_lines

# Accepting user input for paragraph and page width
user_paragraph = input("Enter the paragraph: ")
user_width = int(input("Enter the page width: "))

justified_paragraph = justify_paragraph(user_paragraph, user_width)
for line in justified_paragraph:
    print(line)
