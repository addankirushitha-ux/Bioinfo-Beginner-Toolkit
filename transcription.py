# Script to convert DNA sequence to RNA (Transcription)
dna_sequence = "ATGCGATATGCCTAG"

# Transcription replaces Thymine (T) with Uracil (U)
rna_sequence = dna_sequence.replace("T", "U")

print(f"Original DNA: {dna_sequence}")
print(f"Transcribed RNA: {rna_sequence}")
