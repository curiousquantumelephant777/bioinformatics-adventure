class Bfactorpdbvisual:
  # Set up starting data for visual
  def __init__(self, pdb_id, background_color='#ffffff'):
    self.pdb_id = pdb_id
    self.background_color = background_color
    self.view = py3Dmol.view(query=f'pdb:{pdb_id}', width=800, height=600)
    self.view.setBackgroundColor(self.background_color)
    self.view.setStyle({'cartoon': {'colorscheme': {'prop':'b','gradient': 'bwr', 'min':20, 'max':80}}})
    self.view.zoomTo()
    self.view.show()
# This plots the B factor visualization for your chosen PDB id protein (6Q2N represents the Cryo-EM structure of the RET/GFRα1/GDNF extracellular complex here, Reference: (PDB bank website)
# You can change the background color using your chosen hex code. The default is #ffffff (white background)
my_protein = Bfactorpdbvisual(pdb_id='6Q2N', background_color='#4A0E4E')
