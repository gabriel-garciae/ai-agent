# src/ai_agent/main.py

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

def main():
    model_name = "gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    model.eval()

    prompt = "How can artificial intelligence help a data engineer?"
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Adiciona attention_mask
    attention_mask = torch.ones_like(input_ids)

    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=100,
        num_return_sequences=1,
        temperature=0.7,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )

    print(tokenizer.decode(output[0], skip_special_tokens=True))

if __name__ == "__main__":
    main()