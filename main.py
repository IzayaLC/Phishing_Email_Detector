import re
from rules import phishing_keywords

    
with open('sample.txt', 'r') as f:
    text = f.read().lower()
                
matches = []
for kw in phishing_keywords:
    if kw.lower() in text:
        matches.append(kw.lower())
    
    
print('-' * 50, 'Suspicious Language Detected', '-' * 50)
print(matches)
        

   

