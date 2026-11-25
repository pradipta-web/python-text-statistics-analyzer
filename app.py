import re
from collections import Counter


def analyze_text(text):
    words = re.findall(r"\b[a-zA-Z0-9]+\b", text)

    total_characters = len(text)
    total_words = len(words)
    total_sentences = len(re.findall(r"[.!?]+", text))
    total_paragraphs = len([
        paragraph for paragraph in text.split("\n\n")
        if paragraph.strip()
    ])

    word_frequency = Counter(word.lower() for word in words)

    most_common = word_frequency.most_common(1)

    average_word_length = (
        sum(len(word) for word in words) / total_words
        if total_words > 0 else 0
    )

    return {
        "characters": total_characters,
        "words": total_words,
        "sentences": total_sentences,
        "paragraphs": total_paragraphs,
        "most_common": most_common,
        "average_length": average_word_length
    }


def main():
    print("=" * 45)
    print("       TEXT STATISTICS ANALYZER")
    print("=" * 45)

    print("\nEnter your text (type END to finish):\n")

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    text = "\n".join(lines)

    if not text.strip():
        print("\n[ ERROR ] No text entered!")
        return

    result = analyze_text(text)

    print("\n" + "-" * 45)
    print("             ANALYSIS RESULT")
    print("-" * 45)

    print(f"Total Characters : {result['characters']}")
    print(f"Total Words      : {result['words']}")
    print(f"Total Sentences  : {result['sentences']}")
    print(f"Total Paragraphs : {result['paragraphs']}")

    if result["most_common"]:
        word, count = result["most_common"][0]
        print(f"Most Used Word   : {word}")
        print(f"Word Frequency   : {count}")

    print(f"Average Word Length : {result['average_length']:.2f}")

    print("=" * 45)


if __name__ == "__main__":
    main()