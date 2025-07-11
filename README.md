# Normalized Group Performance Assessment Formula

This repository describes and shares the **Normalized Group Performance (P_i)** formula for comparing groups with uneven sample sizes using rank-based statistics. It provides a systematic approach for fair and interpretable assessment of relative group performance.

## Abstract

This formula can numerically identify the performance of a group, **P_i**, within a collection of groups containing uneven numbers of elements. This novel approach accounts for weight bias inherent in the formula itself. The performance value **P_i** falls within the normalized range of [0,1], representing non-dominant to dominant performance within the collection.

This range offers a more interpretable and practical scale, which can be visualized as 0 to 100% dominance in performance via **P_i × 100**. This standardized scale enables comparisons across collections that may use different measurement scales.

## Formula

The core formula is:

P_i = (-n_i + Σ r_j) / [n_i * (N - 1)]

Or, in LaTeX:

P_i = \frac{-n_i + \sum_{j=1}^{n_i} r_j}{n_i \cdot (N - 1)}

## Description of Terms

- **Ranks**: Sequential ranks assigned to items within and across groups. Tied ranks are averaged.
  - Ranks are in ascending order of dominance: Rank 1 = lowest, Rank N = highest.
  - This mirrors standard usage in rank-based statistical methods such as the [Mann–Whitney U test](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test).

- **P_i**: Normalized performance value for group *i*, ranges from 0 (least dominant) to 1 (most dominant).

- **Σ r_j**: Sum of ranks for all items in group *i*.

- **n_i**: Number of items in group *i*.

- **N**: Total number of items across all groups.
N = sum of n_i over all groups

 ## 📁 Folder Structure

<pre>
├── Code
│ ├── numerical_validation/
│ │ ├── implementation_classes/
│ │ │ ├── init.py
│ │ │ ├── data_collection.py
│ │ │ ├── data_group.py
│ │ │ └── data_element.py
│ │ ├── numerical_validation_kruskal_dunnett_performance_measure
│ │ └── numerical_validation_minima_maxima_performance_measure
│ └── mathematical_validation/
│ └── mathematical_validation_normalized_performacne_measure.ipynb
├── Latex
│ ├── normalized-rank-comparison.tex
│ ├── normalized-rank-comparison.pdf
│ └── refs.bib 
</pre>


### 🔍 Description of Folders

- **`Code/`**  
  Main directory for the source code of the project.

- **`Code/numerical_validation/implementation_classes/`**  
  Core Python classes used for data structuring, grouping, and collection.  
  - `data_element.py`: Defines the atomic unit of a data element.  
  - `data_group.py`: Groups data elements and calculates related stats.  
  - `data_collection.py`: Manages multiple groups.  
  - `__init__.py`: Initializes the folder as a Python module.

- **`Code/numerical_validation/numerical_validation_kruskal_dunnett_performance_measure/`**  
  Contains scripts and logic applying Kruskal-Wallis H-test and Dunnett post-hoc test for comparing groups on performance.

- **`Code/numerical_validation/numerical_validation_minima_maxima_performance_measure/`**  
  Focuses on normalized scoring based on identifying minima and maxima in rank comparison.

- **`Code/mathematical_validation/`**  
  Symbolic or mathematical validation of the Normalized Performance Measure.  
  - `mathematical_validation_normalized_performacne_measure.ipynb`: A Jupyter notebook validating formulas symbolically.

- **`Latex/`**  
  Contains the academic report/paper written in LaTeX.  
  - `normalized-rank-comparison.tex`: Main TeX document.  
  - `normalized-rank-comparison.pdf`: Compiled PDF report.  
  - `refs.bib`: Bibliography used in the paper.

---

## ▶️ How to Run

To ensure your imports work correctly, always run scripts using the `-m` flag from the root of the project:

```bash
cd Code
python -m numerical_validation.implementation_classes.data_group


## Purpose

✅ Normalize performance scores across groups of unequal sizes.  
✅ Provide a standardized scale (0 to 1, or 0% to 100%) for easy interpretation.  
✅ Allow fair comparison even when underlying measurement scales differ.  
✅ Support visualization of group performance in dashboards or reports.  

## Example Use Cases

- **Education**: Comparing class performance when class sizes differ or grading scales vary.
- **Business**: Evaluating team performance across departments with unequal headcounts.
- **Organizational Restructuring**: Identifying top- or bottom-performing units for guidance or resource allocation.
- **Social Science Research**: Comparing survey responses across unequal demographic groups while controlling for sample size differences.

## Advantages

- Handles tied ranks properly.  
- Adjusts automatically for different group sizes (removes sample-size bias).  
- Easy to interpret and visualize (0–1 or 0–100% scale).  
- Conceptually consistent with rank-based non-parametric statistics.  
- Simple to implement in R, Python, Excel, or other statistical tools.

- # License

## Paper and Documentation

This work (including the LaTeX paper, formula, and README documentation) is licensed under:

Creative Commons Attribution 4.0 International (CC BY 4.0)

You are free to:

- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:

- Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

See: https://creativecommons.org/licenses/by/4.0/

---

## Code

Any code in this repository is licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED.

See: https://opensource.org/licenses/MIT
