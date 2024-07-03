import re

def process_text(text):
    # Remove numbers and square brackets
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'\[.*?\]', '', text)  # Remove content inside square brackets

    # Split the text into lines
    lines = text.split('\n')
    
    # Initialize a list to hold the cleaned lines
    cleaned_lines = []
    
    skip_next_line = False
    for line in lines:
        if skip_next_line:
            # Skip this line and reset the flag
            skip_next_line = False
            continue
        
        # Check if the line starts with "Rozdział" and has some content after it
        if re.match(r'Rozdział .*', line):
            # Set the flag to skip the next line
            skip_next_line = True
            # Add 5 empty lines
            cleaned_lines.extend([''] * 5)
            continue
        
        # Strip whitespace and add non-empty lines to the cleaned list
        stripped_line = line.strip()
        if stripped_line:
            cleaned_lines.append(stripped_line)
    
    # Join the cleaned lines back into a single string with proper formatting
    formatted_text = '\n'.join(cleaned_lines)
    
    return formatted_text

def save_chapters_to_files(text):
    # Process the text
    formatted_text = process_text(text)
    
    # Split the formatted text into chapters using 5 empty lines as a delimiter
    chapters = re.split(r'\n{5}', formatted_text)
    
    # Save each chapter into a separate file
    for i, chapter in enumerate(chapters):
        file_name = f"{i+1:02}.txt"  # Name files as 01, 02, 03, etc.
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(chapter.strip())

# Example usage
text = """

"""

save_chapters_to_files(text)
