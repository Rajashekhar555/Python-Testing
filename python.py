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
    for line in lines:
        if len(line) == 1 or len(line) == width:  # Single word or full line
            justified_lines.append(" ".join(line).ljust(width))
        else:
            spaces_needed = width - sum(len(word) for word in line)
            num_gaps = len(line) - 1
            spaces_between_words = spaces_needed // num_gaps
            extra_spaces = spaces_needed % num_gaps
            justified_line = ""
            for i in range(len(line) - 1):
                justified_line += line[i] + ' ' * (spaces_between_words + (1 if i < extra_spaces else 0))
            justified_line += line[-1]
            justified_lines.append(justified_line)

    return justified_lines

def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def validate_paragraph(paragraph):
    return len(paragraph) > 0

def validate_page_width(width):
    return width.isdigit() and int(width) > 0

# Get paragraph input from user with validation
paragraph = get_valid_input("Enter a paragraph: ", validate_paragraph)

# Get page width input from user with validation
page_width = get_valid_input("Enter the page width: ", validate_page_width)
page_width = int(page_width)

justified_paragraph = justify_paragraph(paragraph, page_width)
for i, line in enumerate(justified_paragraph, 1):
    print(f"Array [{i}] = {line}")
