import numpy as np
from mendeleev import element

N = element('N')
C = element('C')
H = element('H')
O = element('O')
S = element('S')

def relative_en(Atom):
    return np.round(Atom.en_pauling - N.en_pauling,2)

print("H,O,C,S")
print(relative_en(H), relative_en(O), relative_en(C), relative_en(S))

from mendeleev.vis import create_vis_dataframe, periodic_table_plotly
import matplotlib.pyplot as plt

elements = create_vis_dataframe()
fig = periodic_table_plotly(elements)
fig.write_image("temp.png")
