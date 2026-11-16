
## 🐍 Biopython Functions: 🧬

### Text Manipulation (Bio.Seq)
* `Seq()` - Turns a string of text into biological sequence object for genetic analysis
* `.transcribe()` - Turns DNA to RNA (swapping T with U)
* `.translate()` - Takes RNA sequence and translates it into protein sequence (chain of amino acids)
* `.reverse_complement` - Flips DNA backwards and pairs letters (A with T, C with G) to see how the opposite strand looks

### File Handling (Bio.SeqIO)
* `SeqIO.read()` - Opens a file containing a genetic sequence (like .fasta or .gb file) and reads it (parses into a Biopython sequence record)
* `SeqIO.parse()` - Used when a file has hundreds or millions of different sequences at once, convenient because you can loop through them one by one
* `SeqIO.write()` - Saves edited DNA back to standard biological file

### Database Searching (Bio.Blast)
* `NCBIWWW.qblast()` - Sends DNA sequence over the internet to NCBI to find out what organism it belongs to

### PairwiseAligner(): Sequence alignment tool
* `Aligner.mode = ‘global’` Sets alignment to global, aligning length of both sequences end-to-end
* `aligner.align()`: compares species-species sequences letter by letter
* `next(alignments)`: Retrieves top-scoring alignment from results generator

* `Identical_matches`: counts matching amino acids between two aligned sequences, ensuring gaps (-) are excluded
* `Percent_identity`: Divides matches by total length of alignment to get a percentage
* `print()`: Displays the final percentage

---

## 🧬 PyMOL

### Loading and Viewing
* `Fetch [ID]`: Downloads a 3D protein structure directly from global Protein Data Bank using its 4-letter ID code (e.g., `fetch 6Q2N`)
* `Load [filename]`: Opens a 3D molecule file (like .pdb)
* `Zoom` - Centers camera, allowing you to focus on the molecule clearly

### Styling and Coloring
* `show [style]`: Changes how the molecule looks.
  * Common Styles: cartoon (ribbon shaped), spheres (every individual atom) or surface (solid outer shell)
* `hide [style]`: removes visual style so screen doesn’t look cluttered
* `Color [color_name], [selection]` - colors specific parts of the protein (e.g. `color purple, chain A`)

### Measurement
* `Distance [name], [atom1], [atom2]` - Draws dotted line between two atoms and calculates how close they are in nanometers
* `Align [protein1], [protein2]` - Takes two different proteins, stacks them directly on top of each other, shows where structures match or differ
