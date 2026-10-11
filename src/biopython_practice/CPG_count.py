# These scripts compute the percentage of a DNA sequence's GC content. I am planning on applying these to find CPG islands in potential biomarkers for neurodivergent phenotypes.
# 1. Using standard Python functions and operations

# Step 1: Define your DNA strand
# Example
dna_sequence = "CCGTCGATAAAAGGGTTT"

# Step 2: Count the Gs and Cs
g_count = dna_sequence.count("G")
c_count = dna_sequence.count("C")

# Step 3: Add them together
total_gc = g_count + c_count

# Step 4: Find the total length of the DNA strand
total_letters = len(dna_sequence)

# Step 5: Calculate the percentage
percentage = (total_gc / total_letters)

# Step 6: Print the result to the screen (output: percentage of your sequence's GC count!)
print("The GC content is:")
print(percentage)

# 2. Alternatively, you can use Biopython's gc_fraction function for a shortcut!

# Biopython example
# Make sure to import the gc_fraction function with the Bio.SeqUtils package!
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

# Define DNA sequence and use gc_fraction (output: percentage of your sequence's GC count!)
dna_sequence = "CCGTCGATAAAAGGGTTT"
dna_count = gc_fraction(dna_sequence)
print (dna_count)
