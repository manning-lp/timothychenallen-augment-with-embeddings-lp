!pip install openai
!pip install tiktoken

import pandas as pd
import openai
import tiktoken
import scipy
from bs4 import BeautifulSoup
import tiktoken
import os

# Function 1: Extract Text from HTML

def extract_text_from_html(file_path):
    """
    Extract text from an HTML file.
    
    Parameters:
    - file_path (str): Path to the HTML file.
    
    Returns:
    - Extracted text from the HTML.
    """
    # TODO: Open the file using the provided file_path
    # Hint: Use open() function with 'r' mode and "utf-8" encoding
    # TODO: Read the content of the file
    # Hint: Use the read() method of the file object
    try:
      with open(file_path, 'r') as file:
        content = file.read()
        #print(content)
    except FileNotFoundError:
      print(f"File not found at: {file_path}")
    except Exception as e:
      print(f"An error occurred: {e}")

    # TODO: Parse the HTML content using BeautifulSoup
    # Hint: Use BeautifulSoup with 'html.parser' as the parser
    soup = BeautifulSoup(content, 'html.parser')
    
    # TODO: Extract and return text from the parsed HTML content
    # Hint: Use the get_text() method of the BeautifulSoup object
    text = soup.get_text()
    
    return text  # Placeholder return


# Function 2: Split Text by Tokens
import tiktoken  # Ensure you have this module installed

def split_text_by_tokens(text, max_tokens=300):
    """
    Splits the text into chunks, ensuring that each chunk contains no more than `max_tokens` tokens.

    Parameters:
    - text (str): Text to be split.
    - max_tokens (int, optional): Maximum number of tokens per chunk. Default is 300.

    Returns:
    - List[str]: List of text chunks.
    """
    
    # TODO: Initialize the tokenizer
    # Hint: Use tiktoken to get an appropriate encoding model (e.g., 'cl100k_base')
    encoding = tiktoken.get_encoding("cl100k_base")
    
    # TODO: Tokenize the text using the tokenizer
    # Hint: Use the encode() method of the tokenizer
    tokens = encoding.encode(text)

    # TODO: Initialize a list to hold the text chunks and a string to hold the current chunk
    # Hint: Use list and string objects
    chunks = []
    current_chunk = ""
    
    # TODO: Iterate through each word in the input text
    # Hint: Use a for loop and the split() method of the string
    for word in text.split():
    
        # TODO: Check if adding a new word to the current chunk would exceed max_tokens
        # Hint: Use the encode() method of the tokenizer and len() function
        if len(encoding.encode(current_chunk + " " + word)) > max_tokens:
        
            # TODO: If it would, add the current chunk to the list of chunks and start a new chunk
            # Hint: Use append() method of the list
            chunks.append(current_chunk)
            current_chunk = ""
        
        # TODO: Add the current word to the current chunk
        # Hint: Use string concatenation
        current_chunk += " " + word
    
    # TODO: Add any remaining text as a chunk
    # Hint: Ensure the last chunk is not ignored if it does not exceed max_tokens
    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks  # Placeholder return

# TODO: Function 3: Process Directory (Students to complete based on guidance)

import os

def process_directory(directory, max_tokens=400):
    """
    Process all HTML files within a directory (and its subdirectories), extracting text and splitting based on token count.
    
    Parameters:
    - directory (str): The root directory to start the search for HTML files.
    - max_tokens (int): Maximum number of tokens per chunk.
    
    Returns:
    - Dictionary with file paths as keys and lists of text chunks as values.
    """
    # TODO: Initialize a dictionary to store results
    # Hint: Use a dictionary with file paths as keys and lists of text chunks as values
    results = {}

    # TODO: Loop through the directory and its subdirectories
    # Hint: Use the os.walk() function to traverse through directory and subdirectories
    for root, dirs, files in os.walk(directory):
    
        # TODO: Loop through each file in the current directory
        # Hint: Use a for loop to iterate through the filenames
        for file in files:
        
            # TODO: Check if the file is an HTML file
            # Hint: Use the endswith() method of the string
            if file.endswith(".html"):
            
                # TODO: Construct the full path to the HTML file
                # Hint: Use os.path.join() method
                file_path = os.path.join(root, file)
                
                # TODO: Extract text from the HTML file
                # Hint: Use the extract_text_from_html() function
                extracted_text = extract_text_from_html(file_path)
                
                # TODO: Split the extracted text based on token count
                # Hint: Use the split_text_by_tokens() function
                chunks = split_text_by_tokens(extracted_text, max_tokens)
                
                # TODO: Store the chunks in the results dictionary with the file path as the key
                # Hint: Assign the list of chunks to the dictionary key corresponding to the file path
                results[file_path] = chunks
                
    return results  # Placeholder return
