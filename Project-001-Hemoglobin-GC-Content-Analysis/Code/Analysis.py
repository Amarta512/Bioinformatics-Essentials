"""
Script Name: HBB Gene GC Content Analysis
Description: This script parses a multi-FASTA file containing Hemoglobin Beta (HBB) 
             orthologs, calculates the GC content percentage for each species, 
             and generates a publication-ready visualization.
Input: hbb_orthologs.fasta
Output: gc_content_visualization.png
"""

import os
from Bio import SeqIO
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define relative paths
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
input_file = os.path.join(project_root, "Data", "hbb_orthologs.fasta")
output_file = os.path.join(project_root, "Visualisation", "gc_content_visualization.png")

# Parse sequences and calculate GC content
gc_contents = []
species = []

for record in SeqIO.parse(input_file, "fasta"):
    sequence = str(record.seq).upper()
    species.append(" ".join(record.description.split()[1:3]))
    gc_count = sequence.count("G") + sequence.count("C")
    gc_contents.append((gc_count / len(sequence)) * 100)

# Create dataframe
df = pd.DataFrame({
    "Species": species,
    "GC Content (%)": gc_contents
})

# Create visualization and save figure
sns.set_style("ticks")
sns.set_context("talk")
plt.figure(figsize=(10, 8))
sns.lineplot(data=df, x="Species", y="GC Content (%)", color="grey", alpha=0.6, sort=False, zorder=1)
sns.scatterplot(data=df, x="Species", y="GC Content (%)", palette="viridis", edgecolor="black")
sns.despine()

plt.xlabel("Species", fontsize=14, fontweight="bold", labelpad=15)
plt.ylabel("GC Content (%)", fontsize=14, fontweight="bold", labelpad=15)
plt.title("GC Content of Hemoglobin Beta (HBB) gene Orthologs", fontsize=16, fontweight="bold", pad=20)
plt.xticks(rotation=45, ha="right", style="italic")
plt.tight_layout()

plt.savefig(output_file, dpi=300, bbox_inches="tight")
plt.show()



