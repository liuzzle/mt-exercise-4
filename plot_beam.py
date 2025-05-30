import matplotlib.pyplot as plt

# Data extracted translations/translation.log
beam_sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]
bleu_scores = [6.3, 8.6, 8.7, 8.5, 8.6, 8.6, 8.4, 8.3, 8.2, 8.1, 7.9]
generation_times = [96, 98, 128, 180, 180, 234, 268, 312, 322, 370, 696]

plt.figure(figsize=(12, 5))

# BLEU vs Beam Size
plt.subplot(1, 2, 1)
plt.plot(beam_sizes, bleu_scores, marker='o')
plt.xlabel('Beam Size')
plt.ylabel('BLEU Score')
plt.title('Impact of Beam Size on BLEU Score')
plt.grid(True)

# Time vs Beam Size
plt.subplot(1, 2, 2)
plt.plot(beam_sizes, generation_times, marker='o', color='orange')
plt.xlabel('Beam Size')
plt.ylabel('Generation Time (sec)')
plt.title('Impact of Beam Size on Generation Time')
plt.grid(True)

plt.tight_layout()
plt.show()

plt.savefig('beam_size_analysis.png', dpi=300)