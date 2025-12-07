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

## Author

**Amarta Chowdhury**  
*Biochemistry and Molecular Biology*  
Shahjalal University of Science and Technology


