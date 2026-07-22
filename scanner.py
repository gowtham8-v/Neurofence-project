from model_loader import load_model


def scan(prompt):

    tokenizer, model = load_model()

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_length=100,
        do_sample=True,
        temperature=0.7
    )

    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return response