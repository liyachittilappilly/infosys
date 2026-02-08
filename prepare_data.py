import os

TRANS_FILE = "61-70968.trans.txt"

pairs = []

with open(TRANS_FILE, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(" ", 1)

        if len(parts) < 2:
            continue

        audio_id = parts[0]
        text = parts[1]

        audio_file = audio_id + ".flac"

        if os.path.exists(audio_file):
            pairs.append({
                "audio": audio_file,
                "text": text
            })
        else:
            print("Missing audio:", audio_file)

print("✅ Total pairs:", len(pairs))
print("🔹 Sample:", pairs[:3])
