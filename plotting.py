import numpy as np
import pandas
import matplotlib.pyplot as plt
from fluentxy import parse_data

plt.rc('text', usetex=True)     #Latex compatibility
plt.rc('font', family='serif')  #Setting font, alternative 'sans-serif'


def create_plot(filename, ax=None):
    with open(filename, 'r') as f:
        lines = f.readlines()
    data = parse_data(lines)
    plt.style.use('seaborn-bright')
    label_text = r'\textbf{' + filename.split("/")[-1].replace(".xy", "").replace("_", r"\_") + '}'
    new_ax = data["_outlet"].plot(x="Position", y="Velocity Magnitude", ax=ax, label=label_text)
    plt.grid(True)
    plt.ylabel(r'\textbf{Geschwindigkeit [m/s]}')
    plt.xlabel(r'\textbf{Position}')
    return new_ax

def create_graph(name, files):
    complete_ax = None  
    for file in files:
        complete_ax = create_plot(file, ax=complete_ax)
    plt.savefig("./graphs/" + name + ".pdf", bbox_inches='tight')
    

quad_map =  ["2d_quad_map_1stO_cv.xy",
             "2d_quad_map_1stO_nv.xy",
             "2d_quad_map_2ndO_cv.xy",
             "2d_quad_map_2ndO_nv.xy"]

create_graph("quad_map", quad_map)


             


