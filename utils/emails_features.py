import re

SPAM_KEYWORDS = ["free","win","winner","cash","prize","urgent","loan","credit","offer","click","buy now","lottery","courses"]

def extract_email_features(text: str) -> list[int]:
    words = re.findall(r"\w+", text)
    num_words   = len(words)
    num_upper   = sum(w.isupper() for w in words)
    num_excl    = text.count("!")
    num_links   = len(re.findall(r"https?://\S+", text))
    kw_count    = sum(text.lower().count(kw) for kw in SPAM_KEYWORDS)
    return [num_words, num_upper, num_excl, num_links, kw_count]
