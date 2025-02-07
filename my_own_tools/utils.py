import hashlib
import tiktoken

def get_tokenizer(model: str = "gpt-3.5-turbo"):
    return tiktoken.encoding_for_model(model)

def get_md5(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()
