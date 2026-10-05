"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title:str)-> str:

    """Convert the first letter of each word in the title to uppercase if needed.

    Parameters:
        title (str): Essay title that needs title casing.

    Returns:
        str: The title string in title case (first letters capitalized).
    """

    return title.title()

#print (capitalize_title('hey im not sure if you are aware but i love you')) 
    


def check_sentence_ending(sentence: str)-> str:
    """Check the ending of the sentence to verify that a period is present.

    Parameters:
        sentence (str): A sentence to check.

    Returns:
        bool: Is the sentence punctuated correctly?
    """

    return sentence.endswith('.')
#print (check_sentence_ending('hey im not sure if you are aware but i love you.')) 

def clean_up_spacing(sentence:str)-> str:
    """Trim any leading or trailing whitespace from the sentence.

    Parameters:
        sentence (str): A sentence to clean of leading and trailing space characters.

    Returns:
        str: A sentence that has been cleaned of leading and trailing space characters.
    """

    return sentence.strip()
#print (clean_up_spacing('    hey im not sure if you are aware but i love you.       '))


def replace_word_choice(sentence:str, old_word:str, new_word:str)-> str:
    """Replace a word in the provided sentence with a new one.

    Parameters:
        sentence (str): A sentence to replace words in.
        old_word (str): The word to replace.
        new_word (str): The replacement word.

    Returns:
        str: Input sentence with new words in place of old words.
    """

    return sentence.replace(old_word, new_word)

print(replace_word_choice('hey im not sure if you are aware but i love you.','but','and'))

