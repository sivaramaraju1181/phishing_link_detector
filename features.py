from urllib.parse import urlparse

def get_features(url):
    parsed = urlparse(url)

    features = [
        len(url),                         # URL Length
        url.count('.'),                  # Dot count
        url.count('-'),                  # Hyphen count
        1 if '@' in url else 0,          # @ symbol
        1 if parsed.scheme == 'https' else 0,  # HTTPS
        1 if parsed.hostname and parsed.hostname.replace('.', '').isdigit() else 0
    ]

    return features