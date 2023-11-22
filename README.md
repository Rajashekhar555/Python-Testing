 # Python-Testing

Function justify_text: This function takes two parameters, paragraph (a string containing the input text) and page_width (an integer specifying the desired width for each line of the output text).

Splitting the input paragraph into words: The paragraph.split() function is used to split the input paragraph into individual words, creating a list of words.

Initializing variables:

lines is an empty list that will store the justified lines of text.
current_line is an empty list used to build the current line of text being processed.
current_length keeps track of the total length of words in the current line.
Iterating through words: The program iterates through each word in the list of words obtained from the input paragraph.

It checks if adding the next word to the current line will exceed the page width. If it does, it appends the current line to the lines list and resets current_line and current_length to start building a new line.
Handling remaining words: After processing all words, if there are remaining words in current_line, they are appended to the lines list.

Justification of lines:

The justified_lines list will contain the final justified strings.
For each line in the lines list:
It calculates the total spaces needed to reach the desired page_width.
Divides these spaces among the words in the line.
Builds the justified line by adding words with appropriate spaces in between to meet the page_width without breaking words.
Returning the justified lines: The function returns the list of justified lines.

Example usage:

It defines an example paragraph and a page width.
Calls the justify_text function with these parameters.
Prints the result by iterating through the justified lines and displaying them as "Array [i] = ...".
