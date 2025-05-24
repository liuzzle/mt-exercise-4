import re
import random

# Configuration
input_file = "joint_vocab.txt"
output_file = "joint_vocab_2k.txt"
sample_size = 2000
random_seed = 42  # Set to None for non-reproducible random samples

# Read the input file
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# Extract words using regex
words = re.findall(r"\b\w+\b", text)

# Sample randomly
if random_seed is not None:
    random.seed(random_seed)

if sample_size > len(words):
    raise ValueError("Sample size exceeds total number of words in the file.")

sampled_words = random.sample(words, sample_size)

# Write to output file
with open(output_file, "w", encoding="utf-8") as f:
    for word in sampled_words:
        f.write(f"{word}\n")

print(f"Sampled {sample_size} words written to '{output_file}'")