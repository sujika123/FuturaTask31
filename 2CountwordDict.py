# 2.Write a function that reads a text file and counts the number of times each word appears in the file.
# The function should return a dictionary where the keys are words and the values are the counts.

def count_words_in_file(filename):
    import string

    # Initialize an empty dictionary to hold word counts
    word_counts = {}

    # Open the file for reading
    with open(filename, 'r') as file:
        # Read the file line by line
        for line in file:
            # Remove punctuation and convert to lowercase
            line = line.translate(str.maketrans('', '', string.punctuation)).lower()
            # Split the line into words
            words = line.split()

            # Count each word
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

    return word_counts


# Example usage:
filename = 'sample.txt'  # Replace with the path to your text file
word_counts = count_words_in_file(filename)
print(word_counts)
