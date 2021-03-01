from typing import List
import nltk


def get_word_tokens(text: str) -> List[str]:
    try:
        return nltk.word_tokenize(text)
    except LookupError:
        # tokens cannot be generated unless the tokenisor is download
        nltk.download('punkt')
        return nltk.word_tokenize(text)