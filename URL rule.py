import re
from urllib.parse import urlparse

SUSPICIOUS_TLDS = {'ru', 'cn', 'tk', 'top', 'zip', 'xyz', 'click', 'gq', 'ml', 'cf'}
TRUSTED_DOMAINS = {
    'google.com', 'microsoft.com', 'paypal.com', 'apple.com',
    'amazon.com', 'github.com', 'facebook.com'
}

def extract_urls(text):
    """Extract all URLs from text using regex."""
    url_pattern = re.compile(r'(https?://[^\s]+)', re.IGNORECASE)
    return re.findall(url_pattern, text)

def is_suspicious(url):
    """Check if the given URL looks suspicious."""
    parsed = urlparse(url)
    hostname = parsed.hostname or ""
    hostname = hostname.lower()

    
    if re.match(r'^\d{1,3}(\.\d{1,3}){3}$', hostname):
        return True, "Uses IP address instead of domain"

    if "%" in url or "@" in url:
        return True, "Contains obfuscated or misleading characters (% or @)"

    tld = hostname.split('.')[-1]
    if tld in SUSPICIOUS_TLDS:
        return True, f"Suspicious top-level domain: .{tld}"

    for trusted in TRUSTED_DOMAINS:
        trusted_name = trusted.split('.')[0]
        if trusted_name in hostname and not hostname.endswith(trusted):
            return True, f"Possible impersonation of {trusted}"

    return False, None

def analyze_file(file_path="D:\Program Files\sample.txt"):
    """Read sample.txt, extract URLs, and check for suspicious ones."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f" File not found: {file_path}")
        return

    urls = extract_urls(text)

    if not urls:
        print("No URLs found in the file.")
        return

    print(f"Found {len(urls)} URL(s) in {file_path}\n")

    for url in urls:
        suspicious, reason = is_suspicious(url)
        if suspicious:
            print(f"[ Suspicious] {url}")
            print(f"   ↳ Reason: {reason}")
        else:
            print(f"[ Safe] {url}")

    print("\nAnalysis complete.")

if __name__ == "__main__":
    analyze_file()
