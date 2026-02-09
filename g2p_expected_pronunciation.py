from g2p_en import G2p
import os

# create output folder
os.makedirs("expected_pronunciation", exist_ok=True)

# initialize G2P
g2p = G2p()

# example sentences (you can change/add)
sentences = [
    "cat",
    "bat",
    "rat",
    "she sells sea shells"
]

for i, sentence in enumerate(sentences):
    phonemes = g2p(sentence)

    # remove known unwanted tokens (spaces)
    phonemes = [p for p in phonemes if p != " "]

    out_path = f"expected_pronunciation/sentence_{i}.txt"

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"sentence: {sentence}\n")
        f.write("expected_pronunciation:\n")
        f.write(" ".join(phonemes))

    print(f"Saved: {out_path}")
