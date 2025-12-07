# HBB Gene GC Content Analysis

## Project Overview

This project analyzes the GC content percentage of Hemoglobin Beta (HBB) gene orthologs across multiple species. It parses FASTA-formatted sequence data, calculates GC percentages, and generates a publication-ready visualization comparing GC content across different species.

## Project Structure

```
Project-001-Hemoglobin-GC-Content-Analysis/
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
├── Code/
│   └── Analysis.py                    # Main analysis script
├── Data/
│   └── hbb_orthologs.fasta            # Input FASTA file with HBB sequences
└── Visualisation/
    └── gc_content_visualization.png   # Output visualization
```

## Description

The **Analysis.py** script performs the following tasks:

1. **Sequence Parsing**: Reads multi-FASTA formatted genetic sequences from `hbb_orthologs.fasta`
2. **GC Content Calculation**: Computes the percentage of Guanine (G) and Cytosine (C) nucleotides for each species
3. **Data Aggregation**: Organizes results in a pandas DataFrame with species names and their corresponding GC percentages
4. **Visualization**: Generates a professional scatter plot with connecting lines showing GC content variation across species
5. **Output**: Saves the visualization as a high-resolution PNG image (300 DPI)

## Dependencies

The project requires the following Python packages:

- **biopython**: For parsing and analyzing biological sequence data
- **pandas**: For data manipulation and organization
- **matplotlib**: For creating visualizations
- **seaborn**: For enhanced plotting aesthetics

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

1. Ensure your FASTA file is located at: `Data/hbb_orthologs.fasta`
2. Run the analysis script:

```bash
python Code/Analysis.py
```

3. The visualization will be saved to: `Visualisation/gc_content_visulation.png`

**Note**: Update the file paths in the script if your directory structure differs from the default.

## Input Format

The input file `hbb_orthologs.fasta` should be a standard FASTA format file with:
- Sequence headers containing species information (at least the first 3 space-separated fields)
- DNA sequences (containing A, T, G, C nucleotides)

Example format:
```
>species_name_1 additional info
ATGCATGCATGC...
>species_name_2 additional info
GCTAGCTAGCTA...
```

## Output

- **Visualization File**: `Visualisation/gc_content_visualization.png`
  - Format: PNG image at 300 DPI
  - Style: Publication-ready with:
    - Line plot connecting points (grey, semi-transparent)
    - Scatter plot with viridis color palette
    - Bold axis labels and title
    - Rotated species names for readability

## Features

- Automated GC content calculation from DNA sequences
- Species identification from FASTA headers
- Professional publication-quality visualization
- High-resolution output suitable for papers and presentations
- Clean plot design with minimal distracting elements

## Author

**Amarta Chowdhury**  
*Biochemistry and Molecular Biology*  
Shahjalal University of Science and Technology

---

## Author Notes

- This analysis is useful for understanding compositional biases in gene sequences across evolutionary distant species
- GC content is an important parameter in genomics as it can affect protein structure and evolutionary dynamics
- The HBB gene is highly conserved across mammals, making it ideal for comparative genomic studies
