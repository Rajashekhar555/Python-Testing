 # Python-Testing
justify_paragraph() Function:

This function takes a paragraph string and a width as parameters.
It splits the paragraph into words.
It constructs lines based on the page width such that no word is broken across lines.
For each line, it calculates the number of spaces needed to justify the text evenly.
It then creates justified lines by adding appropriate spaces between words.
The function returns an array of justified strings.
get_valid_input() Function:

This function takes a prompt message and a validation function as parameters.
It repeatedly asks the user for input until the input satisfies the validation function.
It returns the valid input.
validate_paragraph() Function:

This function validates the paragraph input from the user.
It checks if the length of the input paragraph is greater than zero (i.e., not empty).
validate_page_width() Function:

This function validates the page width input from the user.
It checks if the input consists only of digits and is greater than zero.
The program starts by asking the user to input a paragraph using get_valid_input().

Then, it prompts the user for the page width using get_valid_input().

The paragraph and page width are passed to the justify_paragraph() function to obtain the justified lines.

Finally, the program displays the justified strings in an array-like format using a loop (for i, line in enumerate(justified_paragraph, 1)).
