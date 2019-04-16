import pymol

pymol.finish_launching()
pymol.cmd.load('Protein/1buw.pdb')
pymol.cmd.do('hide everything')
pymol.cmd.do('sel ex, (id 14,15,67,68,69,70,71,72,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,119,120,121,123,124,125,126,129,137,138,145,146,147,148,149,150,151,152,153,154,155,156,157,158,163,164,165,166,167,168,169,170,171,172,173,175,176,177,178,179,180)')
pymol.cmd.do('show cartoon, ex')
pymol.cmd.do('color blue, ex')
pymol.cmd.do('png Protein/ex.png')
pymol.cmd.refresh()
pymol.cmd.quit()