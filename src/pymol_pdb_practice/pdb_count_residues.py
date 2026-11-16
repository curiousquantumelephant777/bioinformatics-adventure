# This script pulls PDB info from the RCSB Protein Data Bank (RCSB PDB) (https://www.rcsb.org/) and computes the number of total residues for each protein. You can input your select PDB 4-letter IDs in the pdb_ids field. Here,7WC4 (https://www.rcsb.org/structure/7WC4) represents the active 5-HT2A receptor bound to serotonin, whereas 8ZMG is the crystal structure of an inverse agonist antipsychotic drug pimavanserin-bound 5-HT2A (inactive, source: https://www.rcsb.org/structure/8ZMG). The third entry, 7WC6, represents the crystal structure of 5-HT2A bound to LSD (https://www.rcsb.org/structure/7WC6).
# Note: Comparing these entries highlights how different structural biology research groups use varying construct designs, truncations, and stabilization strategies (such as fusion partners) to crystallize the same receptor.
!pip install biopython
from Bio.PDB import MMCIFParser, PDBList
import os

os.makedirs("structures", exist_ok=True)
pdb_ids = ["7WC4", "8ZMG", "7WC6"]
downloader = PDBList()

for pdb_id in pdb_ids:
    downloader.retrieve_pdb_file(pdb_id, pdir="structures", file_format="mmCif")

parser = MMCIFParser(QUIET=True)

for pdb_id in pdb_ids:
    filepath = f"structures/{pdb_id.lower()}.cif"
    structure = parser.get_structure(pdb_id, filepath)
    print(f"\nStructure: {pdb_id}")
    
    for chain in structure[0]:
        all_entities = list(chain.get_residues())
        # Filter for standard amino acid residues only (hetflag == " ")
        aa_residues = [res for res in all_entities if res.id[0] == " "]
        
        print(
            f"Chain: {chain.id} | "
            f"Amino Acids: {len(aa_residues)} | "
            f"Total Entities (incl. ligands/lipids/water): {len(all_entities)}"
        )
#Output
#Structure: 7WC4
#Chain: A | Amino Acids: 370 | Total Entities (incl. ligands/lipids/water): 380

#Structure: 8ZMG
#Chain: A | Amino Acids: 365 | Total Entities (incl. ligands/lipids/water): 366
#Chain: B | Amino Acids: 361 | Total Entities (incl. ligands/lipids/water): 362

#Structure: 7WC6
#Chain: A | Amino Acids: 355 | Total Entities (incl. ligands/lipids/water): 368
