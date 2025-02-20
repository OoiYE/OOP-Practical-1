def number_to_words(s):
    """Convert digits to words."""
    mapping = {'1': 'One', '2': 'Two', '3': 'Three'}
    return ''.join(mapping.get(ch, ch) for ch in s)

with open('A1_input.txt', 'r') as f:
    content = f.read()

# Manually extract list-like parts
cleaned_lines = []
temp = ""
inside_brackets = False

for char in content:
    if char == '[':  # Start of a list
        inside_brackets = True
        temp = ""
    elif char == ']':  # End of a list
        inside_brackets = False
        cleaned_lines.append(temp)  # Store cleaned list content
    elif inside_brackets:
        temp += char  # Add character inside brackets

# Process and print the extracted lists
for line in cleaned_lines:
    line = line.replace(' ', '').replace("'", "")  # Remove spaces and single quotes
    elements = line.split(',')  # Split by commas
    elements = [number_to_words(e) for e in elements]  # Convert numbers to words
    print(','.join(elements))
