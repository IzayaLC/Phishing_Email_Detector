import re


    
with open('sample.txt', 'r') as rf:
    for line_number, line in enumerate(rf, start=1):
        if re.search(r"\burgent\b", line, re.IGNORECASE):
            print(f"Searched word found on line {line_number}")
                

   

