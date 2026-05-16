from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a text file"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"This file {path} has about {num_words} words.")
        word = 'the '
        contents_num = contents.count(word)
        print(f"This file mentions the word {word} {contents_num} times.")       



filenames = ['text_files/beyond_good_and_evil.txt', 
             'text_files/thus_spake_zarathustra.txt', 
             'text_files/the_genealogy_of_morals.txt']

for filename in filenames:
    path = Path(filename)
    count_words(path)

