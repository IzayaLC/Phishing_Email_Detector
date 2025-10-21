import re
from detection_rules import phishing_keywords

    
def detect_suspicious_language(path, words):
    with open(path, 'r') as f:
        text = f.read().lower()
    
    matches = []
    for kw in words:
        if kw.lower() in text:
            matches.append(kw.lower())
            
    return matches

def detect_sender_reply_mismatch(path):
    sender, reply_to = None, None
    
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            
            if line.lower().startswith('from:'):
                sender = line.split('<')[-1].rstrip('>').lower()
            elif line.lower().startswith('reply-to'):
                reply_to = line.split('<')[-1].rstrip('>').lower()
                
    if not sender or not reply_to:
        return 'Sender domain or reply_to domain is missing'
    
    if sender != reply_to:
        return f'Mismatch detected - sender domain "{sender}" vs reply-to domain "{reply_to}"'
    else:
        return f'No mismatch - both from {sender}'
    



if __name__ == "__main__":
    path = 'sample.txt'
    print('-' * 50, 'Email Report', '-' * 50)
    print(detect_suspicious_language(path, phishing_keywords))
    print(detect_sender_reply_mismatch(path))