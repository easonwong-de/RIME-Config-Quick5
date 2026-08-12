import csv
import datetime
import urllib.request
import unicodedata

FILES = [
    "word.csv",
    "fixed_expressions.csv",
    "phrase_fragment.csv",
    "trending.csv",
]
BASE_URL = "https://raw.githubusercontent.com/CanCLID/rime-cantonese-upstream/main/"

def clean_word(word: str) -> str:
    cleaned = []
    for char in word:
        if char.isspace():
            continue
        cat = unicodedata.category(char)
        if cat.startswith(('P', 'S', 'Z')):
            continue
        cleaned.append(char)
    return "".join(cleaned)

def main():
    seen_words = set()
    words_list = []

    for filename in FILES:
        url = BASE_URL + filename
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            with urllib.request.urlopen(req) as resp:
                content = resp.read().decode("utf-8")
        except Exception as e:
            print(f"Error downloading {filename}: {e}")
            continue

        lines = content.splitlines()
        reader = csv.reader(lines)
        for row in reader:
            if not row:
                continue
            raw_word = row[0].strip()
            if not raw_word or raw_word.lower() in ("char", "word", "text", "head"):
                continue
            cleaned = clean_word(raw_word)
            if cleaned and cleaned not in seen_words:
                seen_words.add(cleaned)
                words_list.append(cleaned)

    today = datetime.date.today().strftime("%Y.%m.%d")
    header = f"""---
name: cantonese
version: "{today}"
sort: by_weight
use_preset_vocabulary: true
...
"""
    output_path = "cantonese.dict.yaml"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(header)
        for w in words_list:
            f.write(w + "\n")

    print(f"Successfully generated {output_path} with {len(words_list)} entries.")

if __name__ == "__main__":
    main()
