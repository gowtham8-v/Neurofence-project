from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "distilgpt2"

_tokenizer = None
_model = None


def load_model():
    """
    Load the tokenizer and model only once.
    """

    global _tokenizer, _model

    if _tokenizer is None or _model is None:
        print("Loading DistilGPT2 model...")

        _tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        _model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

        print("Model loaded successfully!")

    return _tokenizer, _model