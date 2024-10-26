def analyze_text_file(file_path):
    try:
        # Initialize counters
        sentence_count = 0
        word_count = 0
        char_count = 0

        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the file contents
            text = file.read()

            # Count characters
            char_count = len(text)

            # Count sentences (considering '.', '!', and '?' as sentence delimiters)
            sentence_count = text.count('.') + text.count('!') + text.count('?')

            # Count words
            # Split the text into words and filter out empty strings
            words = text.split()
            word_count = len(words)

        # Print the analysis results
        print(f"Number of sentences: {sentence_count}")
        print(f"Number of words: {word_count}")
        print(f"Number of characters: {char_count}")

    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")

# Specify the path to your text file
file_path = input("Enter the path to the text file: ")
analyze_text_file(file_path)
