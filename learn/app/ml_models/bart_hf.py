import logging

from transformers import pipeline, AutoTokenizer

from core.preprocess import get_word_tokens

log = logging.getLogger(__name__)

model_name = tokenizer_name = "facebook/bart-large-cnn"

tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
summarizer = pipeline(
    "summarization",
    model=model_name,
    tokenizer=tokenizer_name,
    framework="pt",
)


def summarize(text: str) -> str:
    tokens = get_word_tokens(text)
    log.info(f"Sumarizing text containing {len(tokens)} words with model {model_name}")

    log.debug("Summarizing %s", text)

    # if the model has no max-size input, use the full txt as input
    max_length = tokenizer.max_model_input_sizes.get(model_name, len(tokens))
    log.debug(f"Model {model_name} has max summarisation input capacity: {tokenizer.max_model_input_sizes}")

    # FIXME use the
    chunks = []
    chunk_size = max_length // 2
    for i in range(0, len(tokens), chunk_size):
        chunk = tokens[i:i+chunk_size]
        chunks.append(' '.join(chunk))

    log.info(f"Seperated text into {len(chunks)} chunks")

    # see arguments in https://huggingface.co/transformers/main_classes/model.html#generative-models
    summarized = summarizer(
        chunks,
        min_length=5,
        max_length=50,
        return_text=True,
        clean_up_tokenization_spaces=True,
    )

    summary = ''.join([s["summary_text"] + "\n" for s in summarized])

    log.info(f"Summary: {summary}")

    return summary
