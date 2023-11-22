 # Python-Testing
Splitting Paragraph into Lines:

justify_paragraph function takes in two parameters: paragraph (input text) and width (page width).
It splits the paragraph into words and then constructs lines such that no word is broken across lines, considering the given width.
The function stores each line as a list of words within the lines list.
Justifying Lines:

For each line in the lines list, the function justifies the text to the specified width.
It handles single-word lines or lines that occupy the entire width separately from lines that contain multiple words.
For lines with multiple words, it calculates the number of spaces needed between words to reach the desired width without breaking words.
Formatting Output:

The function constructs formatted strings for each justified line according to the specified output format (Array [index] = justified_line).
These formatted strings are stored in the justified_lines list, which is then returned by the function.
User Input and Output:
User Input:

The script prompts the user to enter a paragraph and a page width.
It accepts user input using input() function and stores them in user_paragraph and user_width variables, respectively.
Processing and Displaying Justified Lines:

The script calls the justify_paragraph function with the user-provided paragraph and page width.
It receives the justified lines as a list (justified_paragraph).
For each line in justified_paragraph, it prints the line, displaying each line in the requested format (Array [index] = justified_line).
