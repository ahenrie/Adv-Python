import pdfplumber
from collections import Counter
import string
import matplotlib.pyplot as plt
import os
import fnmatch

directory_to_search = '.'

def find_pdfs(directory):
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for file in fnmatch.filter(files, '*.pdf'):
            pdf_files.append(os.path.join(root, file))
    return pdf_files

"""Function to count occurences of letters given a pdf path"""
def count_letters_pdf(pdf_path):
    # Using Counter from collections module
    letter_counts = Counter()

    # Properly open and close with with
    with pdfplumber.open(pdf_path) as file:
        # Iterate over each page, extract text, if != None, lower
        for page in file.pages:
            text = page.extract_text()
            if text:
                text = text.lower()
                # Iterate over each letter in the lowercase text
                for letter in text:
                    if letter in string.ascii_lowercase:
                        letter_counts[letter] += 1
    return letter_counts

def plot_letters(letter_counts):
    sorted_letter_counts = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)
    letters, counts = zip(*sorted_letter_counts)
    plt.figure(figsize=(10, 6))
    plt.bar(letters, counts, color='blue')
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.show()

def count_letters_txt(txt_path):
    letter_counts = Counter()

    with open(txt_path, 'r') as file:
        for line in file:
            for letter in line:
                if letter in string.ascii_lowercase:
                    letter_counts[letter] += 1
    return letter_counts

def create_key(cipher, english_list):
    key = {}
    sorted_cipher = [key for key, _ in cipher.most_common()]

    for key1, key2 in zip(sorted_cipher, english_list):
        key[key1] = key2
    return key

def print_key(key):
    print("Key Mapping:", key)


def decrypt(key, txt_path):
    with open(txt_path, 'r') as file:
        content = file.read()
    decrypted_content = ''.join(key.get(letter, letter) for letter in content)
    with open(txt_path, 'w') as file:
        file.write(decrypted_content)

def main():
    letter_list = [
        'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u',
        'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z'
    ]
    found_pdf_files = find_pdfs(directory_to_search)
    pdf_path = found_pdf_files[0]
    letter_counts_pdf = count_letters_pdf(pdf_path)
    letter_counts_txt = count_letters_txt('./text.txt')
    #plot_letters(letter_counts_txt)
    key = create_key(letter_counts_txt, letter_list)
    print_key(key)

    decrypt(key, './text.txt')

if __name__ == "__main__":
    main()
