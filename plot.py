import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
from matplotlib.ticker import ScalarFormatter, AutoMinorLocator, MultipleLocator

csvname = "exinfo_data.csv"
tags = ["Composite:Aperture", "EXIF:FocalLength"]

focallength_label = [24, 35, 50, 70, 85, 120, 135, 150, 200, 240]
aperture_label = [2.8, 4, 5.6, 8, 11.3, 16, 22.6, 32, 45]

df = pd.read_csv(csvname, usecols=tags)

# For Canon APSC cameras, you need to consider the 1.6 factor.
aperture = df[tags[0]] * 1.6
focallength = df[tags[1]] * 1.6

# For full frame cameras, just ignore the scale factor
#aperture = df[tags[0]]
#focallength = df[tags[1]]


def plot_hist(data, xticklabel, xlabel, savename, bin_step=5):
    nbins = int((data.max() - data.min()) / bin_step)
    logbins = np.geomspace(data.min(), data.max(), nbins + 1)

    fig, ax = pl.subplots(figsize=[12, 8])
    pl.hist(data, bins=logbins, rwidth=0.9)
    pl.xscale("log")
    pl.xticks(xticklabel, [str(ele) for ele in xticklabel])
    ax.xaxis.set_minor_formatter(ScalarFormatter())
    pl.minorticks_off()
    ax.tick_params(axis="both", which="major", labelsize=18)
    pl.xlabel(xlabel, fontsize=22)
    pl.ylabel("Count", fontsize=22)

    pl.savefig(savename, dpi=300, bbox_inches='tight')
    pl.close()


plot_hist(focallength, focallength_label, "Focal length / mm", "FocalLength.png", 5)
plot_hist(aperture, aperture_label, "Aperture F", "Aperture.png", 1)
