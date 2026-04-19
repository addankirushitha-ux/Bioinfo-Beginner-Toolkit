# Script to calculate GC Content percentage
sequence = "ATGCGATATGCCTAG"
gc_count = sequence.count("G") + sequence.count("C")
gc_percent = (gc_count / len(sequence)) * 100

print(f"Sequence: {sequence}")
print(f"GC Content: {gc_percent:.2f}%")
