"""
Morse code string regulations:
-  This program evaluates the validity of the inputted Morse code sequence and decodes it.
-  There should be a space between each letter/digit's Morse code representation (e.g., '.- .--. -' => APT).
-  The maximum length of each letter's Morse code representation is 4 characters, with a few invalid combinations
-  There is a fixed length for each digit's Morse code representation which is of 5 characters (only 10 acceptable combinations)
"""

def get_number(string):
    morse_code_dict = {
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.'
    }
    
    for key, value in morse_code_dict.items():
        if string == value:
            return key
    return None

def get_letter(string):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
        'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..'
    }
    
    for key, value in morse_code_dict.items():
        if string == value:
            return key
    return None


# def transition_letter(morse_str):
#     pattern = ""
#     word = ""
#     state = 0
#     space_count = 0;

#     # Transition table
#     table = [
#         [1, 4, 7],
#         [10, 2, 0],
#         [6, 3, 0],
#         [12, 12, 0],
#         [8, 5, 0],
#         [9, 12, 0],
#         [12, 7, 0],
#         [7, 7, 7],
#         [9, 9, 0],
#         [12, 12, 0],
#         [11, 6, 0],
#         [12, 12, 0],
#         [7, 7, 0],
#     ]

#     for char in morse_str:
#         if char == '.':
#             pattern += '.'    # stores the encoded morse code string
#             input_val = 0
#             print(f"State: {state}")
#             space_count = 0
#         elif char == '-':
#             pattern += '-'
#             input_val = 1
#             print(f"State: {state}")
#             space_count = 0
#         elif char == ' ':
#             space_count += 1
            
#             if space_count == 1:
#                 # One space to decode a letter
#                 if pattern:
#                     print(f"\nCurrent pattern: {pattern}")
#                     print(f"Overall State: {state}")
#                     letter = get_letter(pattern)
#                     print(f"Decoded letter: {letter}")
#                     if letter:
#                         word += letter  # stores decoded morse code sequence
#                     pattern = "" 

#             elif space_count == 3:
#                 # Three spaces signify the end of a word
#                 word += ' ' 
#                 space_count = 0 
#                 state = 0
#                 input_val = 2
#                 continue
#             input_val = 2
#         else:
#             return 0 
        
#         state = table[state][input_val]

#     if pattern:
#         letter = get_letter(pattern)
#         # print(f"Decoded letter: {letter}")
#         if letter:
#             word += letter
    
#     if state != 7:
#         print(f"Decoded word: {word}")
#         return 1

#     return 0 
    

# def transition_number(morse_str):
#     pattern = ""
#     word = ""
#     state = 0
#     space_count = 0;

#     # Transition table
#     table = [
#         [1, 2, 10],
#         [3, 14, 10],
#         [11, 4, 10],
#         [5, 15, 10],
#         [12, 6, 10],
#         [7, 16, 10],
#         [13, 8, 10],
#         [9, 9, 10],
#         [9, 9, 10],
#         [10, 10, 0],
#         [10, 10, 10],
#         [12, 10, 10],
#         [13, 10, 10],
#         [9, 10, 10],
#         [10, 15, 10],
#         [10, 16, 10],
#         [10, 9, 10],
#     ]

#     for char in morse_str:
#         if char == '.':
#             pattern += '.'    # stores the encoded morse code string
#             input_val = 0
#             space_count = 0
#         elif char == '-':
#             pattern += '-'
#             input_val = 1
#             space_count = 0
#         elif char == ' ':
#             space_count += 1
            
#             if space_count == 1:
#                 # One space: decode a single digit
#                 if pattern:
#                     print(f"Current pattern: {pattern}")
#                     digit = get_number(pattern)
#                     print(f"Decoded letter: {digit}")
#                     if digit:
#                         word += digit  
#                     pattern = ""  
                
#                 input_val = 2
#             elif space_count == 3:
#                 # Three spaces signify the end of a word
#                 word += ' ' 
#                 space_count = 0 
#                 state = 0
#                 input_val = 2
#                 continue
#         else:
#             return 0 
        
#         state = table[state][input_val]

#     if pattern:
#         digit = get_number(pattern)
#         if digit:
#             word += digit
    
#     if state != 0 and state != 7:
#         print(f"Decoded word: {word}")
#         return 1

#     return 0 
    
# Helper function to check if pattern could be a number: Numbers have a length of 5 while lettes have <= 4
def is_number_pattern(pattern):
    return len(pattern) == 5  
    
def combined_transition(morse_str):
    pattern = ""
    word = ""
    state_letter = 0
    state_number = 0
    space_count = 0
    
    # Transition table for letters
    """
    INITIAL STATE = Q0
    FINAL STATES = {Q1, Q2, Q3, Q4, Q5, Q6, Q8, Q9, Q10, Q11, Q12}
    DEAD STATE = Q7
    """
    table_letter = [
        [1, 4, 7], [10, 2, 0], [6, 3, 0], [12, 12, 0],
        [8, 5, 0], [9, 12, 0], [12, 7, 0], [7, 7, 7],
        [9, 9, 0], [12, 12, 0], [11, 6, 0], [12, 12, 0], 
        [7, 7, 0]
    ]

    # Transition table for numbers
    """
    INITIAL STATE = Q0
    FINAL STATES = {Q9}
    DEAD STATE = Q10
    """
    table_number = [
        [1, 2, 10], [3, 14, 10], [11, 4, 10], [5, 15, 10], 
        [12, 6, 10], [7, 16, 10], [13, 8, 10], [9, 9, 10],
        [9, 9, 10], [10, 10, 0], [10, 10, 10], [12, 10, 10], 
        [13, 10, 10], [9, 10, 10], [10, 15, 10], [10, 16, 10],
        [10, 9, 10]
    ]

    for char in morse_str:
        if char == '.':
            pattern += '.'
            input_val = 0
            space_count = 0
        elif char == '-':
            pattern += '-'
            input_val = 1
            space_count = 0
        elif char == ' ':
            space_count += 1
            
            if space_count == 1:
                if pattern:
                    # If length == 5 then decode a digit
                    if is_number_pattern(pattern):
                        # print(f"Number pattern: {pattern}")
                        digit = get_number(pattern)
                        if digit:
                            word += digit
                        state_number = 0 
                    else:
                        # print(f"Letter pattern: {pattern}")
                        letter = get_letter(pattern)
                        if letter:
                            word += letter
                        state_letter = 0  
                    pattern = ""
                input_val = 2
            elif space_count == 3:
                word += ' ' 
                space_count = 0
                continue
        else:
            return 0
        
        state_letter = table_letter[state_letter][input_val]
        state_number = table_number[state_number][input_val]
    
    
    # This is to process the last character in the pattern that is not included in the elif char == ' ':
    if pattern:
        if is_number_pattern(pattern):
            digit = get_number(pattern)
            if digit:
                word += digit
        else:
            letter = get_letter(pattern)
            if letter:
                word += letter
    
    print(f"Decoded string: {word}")
    return word


input_string = input("Enter the Morse Code sequence ('.' or '-' or ' ' - 1 space between each letter/digit, 3 spaces between each word): ")
input_string = input_string.rstrip()

if combined_transition(input_string):
    print("Valid Morse code sequence.")
else:
    print("Invalid Morse code sequence!")
