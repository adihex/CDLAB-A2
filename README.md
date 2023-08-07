# CDLAB-A2

### Implementing a lexical analyser:

`Given grammar:`

![Alt text](image.png)

`Patterns for the grammar:`

![Alt text](image-1.png)

- The program takes two arguments: he input file path and the output file path. The input file contains a list of input statements. The output file will contain the categorized test cases, one per line.

- The program first reads the input file into a string. Then, it calls the buildArray() function to split the string into a list of words. The buildArray() function uses regular expressions to identify keywords, relational operators, numbers, and identifiers. It then adds each word to the list, along with its type.

- The program then calls the categorizeTestCases() function to categorize the test cases. The categorizeTestCases() function loops through the list of words and categorizes each one as a keyword, relop, number, identifier, or unrecognized if it does not match any of the given patterns.

- Finally, the program prints the type of tokens and writes them to the output file. 

