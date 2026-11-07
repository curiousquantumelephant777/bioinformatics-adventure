
## Purpose: This script calculates the similarity of a protein (GTF2I) between humans and dogs using the NCBI database. This output shows that the protein sequence is highly similar among dogs and humans. I plan to investigate more potential biomarkers of domestication across humans and socially domesticated/empathetic species like bonobos, horses, cats, elephants, and dogs.

! pip install biopython
from Bio import Entrez
from Bio import SeqIO
from Bio.Align import PairwiseAligner
from Bio.Align import substitution_matrices

# Set your email for NCBI Entrez (Required by NCBI), replace example with your email
Entrez.email = "your.email@example.com"

# Search and fetch Human GTF2I protein sequence
human_prot_search = Entrez.esearch(db="protein", term="GTF2I[gene] AND Homo sapiens[orgn] AND refseq[filter]")
human_record = Entrez.read(human_prot_search)
human_prot_search.close()

if not human_record["IdList"]:
    raise ValueError("No human GTF2I RefSeq protein sequence found.")
human_prot_id = human_record["IdList"][0]

fetch_handle = Entrez.efetch(db="protein", id=human_prot_id, rettype="fasta", retmode="text")
human_protein = SeqIO.read(fetch_handle, "fasta")
fetch_handle.close()

# Search and fetch Dog (Canis lupus familiaris) GTF2I protein sequence
dog_prot_search = Entrez.esearch(db="protein", term="GTF2I[gene] AND Canis lupus familiaris[orgn] AND refseq[filter]")
dog_record = Entrez.read(dog_prot_search)
dog_prot_search.close()

if not dog_record["IdList"]:
    raise ValueError("No dog GTF2I RefSeq protein sequence found.")
dog_prot_id = dog_record["IdList"][0]

fetch_handle_dog = Entrez.efetch(db="protein", id=dog_prot_id, rettype="fasta", retmode="text")
dog_protein = SeqIO.read(fetch_handle_dog, "fasta")
fetch_handle_dog.close()

# Align protein sequences globally using PairwiseAligner with BLOSUM62
aligner = PairwiseAligner()
aligner.mode = 'global'
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
# Optional: Adjust gap scores for protein alignments (defaults can sometimes be strict)
aligner.open_gap_score = -10.0
aligner.extend_gap_score = -0.5

alignments = aligner.align(str(human_protein.seq), str(dog_protein.seq))
best_alignment = next(alignments)

# Calculate percent identity (ensuring gaps '-' are not counted as identical matches)
identical_matches = sum(1 for a, b in zip(best_alignment[0], best_alignment[1]) if a == b and a != '-')
percent_identity = (identical_matches / len(best_alignment[0])) * 100

print(f"Protein Sequence Identity: {percent_identity:.2f}%")

## Output: Protein Sequence Identity: 98.18%
