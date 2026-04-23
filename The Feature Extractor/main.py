# Write a function `extract_features(text)`.
# Convert the entire input string to lowercase to ensure case-insensitivity.
# Remove all punctuation (periods, commas, exclamation marks) before splitting the text into words.
# Initialize an empty dictionary. Iterate through your list of words, adding new words as keys with a value of `1`, and incrementing the value for words that already exist in the dictionary.
# Wrap your execution in a `try/except` block. If the user passes an integer instead of a string, catch the `AttributeError` or `TypeError` and print: *"Error: Input must be a string.*

def extract_features(text):  
    try:
        text = text.lower().replace(".", "").replace(",", "").replace('!', "")

        word_list = text.split()
        word_dictionary = {}

        for word in word_list:
            if word not in word_dictionary:
                word_dictionary[word] = 1
            else:
                word_dictionary[word] += 1
        
        return word_dictionary
    except (AttributeError, TypeError):
        print("Error: Input must be a string.")
        return {}
