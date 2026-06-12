# Project Title

Decision Tree Hyperparameter Tuning on the Breast Cancer Wisconsin Dataset

---

# Overview

This project investigates how different Decision Tree hyperparameters influence classification performance on the Breast Cancer Wisconsin Dataset.

The objective is to systematically study each major hyperparameter independently using 5-fold cross-validation and evaluate its effect on model accuracy and log loss. After identifying the best-performing values, a tuned Decision Tree model is constructed and compared against a baseline model.

---

# Features

* Breast Cancer Wisconsin Dataset classification
* Data exploration and preprocessing
* Train-test data splitting with stratification
* Baseline Decision Tree implementation
* Decision Tree visualization
* 5-Fold Stratified Cross Validation
* Hyperparameter tuning using validation metrics
* Cost Complexity Pruning (CCP Alpha) analysis
* Accuracy and Log Loss evaluation
* Tuned model construction
* Baseline vs Tuned model comparison
* Confusion matrix visualization
* Performance metric comparison (Accuracy, Precision, Recall, F1-Score)

---

# System Workflow

1. Load Breast Cancer Wisconsin Dataset from Scikit-Learn.
2. Convert data into a Pandas DataFrame.
3. Perform exploratory analysis and data validation.
4. Split dataset into training and testing subsets.
5. Train a baseline Decision Tree classifier.
6. Evaluate baseline performance.
7. Create a 5-fold stratified cross-validation pipeline.
8. Study individual hyperparameters:

   * Criterion
   * Maximum Depth
   * Maximum Leaf Nodes
   * Minimum Samples Split
   * Minimum Samples Leaf
   * CCP Alpha
9. Plot Accuracy and Log Loss for each study.
10. Select the best-performing value for every hyperparameter.
11. Train a final tuned Decision Tree model.
12. Compare baseline and tuned models using multiple evaluation metrics.
13. Visualize confusion matrices and final tree structure.

---

# Demo

Include:

* Dataset overview screenshots
* Baseline Decision Tree visualization
* Hyperparameter tuning graphs
* Final Tuned Tree visualization
* Confusion Matrix comparison
* Metric comparison table

---

# Hardware Requirements

* Any modern desktop or laptop
* Minimum 4 GB RAM
* Dual-core processor or higher

---

# Software Requirements

* Python 3.x
* Jupyter Notebook / JupyterLab
* Scikit-Learn
* Pandas
* NumPy
* Matplotlib

---

# Project Structure

```text
./
│
├── Documentation.ipynb
├── project_summary.md
├── README.md
├── images/
│   ├── dataset_head.png
│   ├── dataset_shape_and_info.png
│   ├── dataset_description.png
│   ├── baseline_parameters.png
│   ├── baseline_tree.png
│   ├── criterion_accuracy.png
│   ├── criterion_loss.png
│   ├── depth_accuracy.png
│   ├── depth_loss.png
│   ├── leaf_accuracy.png
│   ├── leaf_loss.png
│   ├── split_accuracy.png
│   ├── split_loss.png
│   ├── leafsample_accuracy.png
│   ├── leafsample_loss.png
│   ├── alpha_accuracy.png
│   ├── alpha_loss.png
│   ├── hyperparameter_study.png
│   ├── tuned_tree.png
│   ├── comparison.png
│   └── confusion_matrices.png
│
└── requirements.txt
```

### File Descriptions

| File                | Purpose                                       |
| ------------------- | --------------------------------------------- |
| Documentation.ipynb | Complete implementation and analysis notebook |
| project_summary.md  | Visual overview of the entire project         |
| README.md           | Project documentation                         |
| images/             | Stores plots and visualizations               |
| requirements.txt    | Python dependencies                           |

---

# Installation

1. Clone the repository:

```bash
git clone https://github.com/heyvarchas/proboticists-summer-training.git
```

2. Navigate into the project directory:

```bash
cd .\proboticists-summer-training\machine-learning_subsystem\decision-tree-hyperparameter-analysis\
```

3. Create and activate a virtual environment (optional):

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

4. Install required packages:

```bash
pip install -r requirements.txt
```

---

# Usage

1. Launch Jupyter Notebook:

```bash
jupyter notebook
```

or

```bash
jupyter lab
```

2. Open:

```text
Documentation.ipynb
```

3. Run all cells sequentially.

---

# How It Works

### Dataset Loading and Exploration

The Breast Cancer Wisconsin Dataset is loaded directly from Scikit-Learn and converted into a Pandas DataFrame. Dataset dimensions, feature information, statistical summaries, target distribution, and missing values are examined before training.

### Baseline Decision Tree

A default Decision Tree Classifier is trained using training data. This serves as the reference model for all future comparisons.

### Cross Validation

A 5-fold Stratified Cross Validation scheme is used to evaluate model performance more reliably than a single train-test split.

### Hyperparameter Tuning

Each hyperparameter is studied independently:

* Criterion (`gini`, `entropy`)
* Maximum Depth
* Maximum Leaf Nodes
* Minimum Samples Split
* Minimum Samples Leaf
* Cost Complexity Pruning (`ccp_alpha`)

Accuracy and Log Loss are recorded for each value and plotted for analysis.

### Final Model Construction

The best-performing value from each tuning experiment is selected and combined to build the final Decision Tree model.

### Model Comparison

The baseline and tuned models are compared using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrices

---

# Results

Key outcomes:

* Successfully trained a baseline Decision Tree classifier.
* Evaluated six important Decision Tree hyperparameters.
* Generated performance plots using cross-validation.
* Identified optimal hyperparameter values.
* Constructed a tuned Decision Tree model.
* Compared baseline and tuned models using multiple metrics.
* Visualized both baseline and tuned tree structures.

---

# Challenges Faced

* Preventing overfitting in large Decision Trees.
* Selecting optimal hyperparameter ranges.
* Balancing model complexity and predictive performance.
* Evaluating models using both Accuracy and Log Loss.
* Understanding the effect of Cost Complexity Pruning.

---

# Future Improvements

* Grid Search based hyperparameter optimization.
* Randomized Search Cross Validation.
* Feature importance analysis.
* Ensemble methods such as Random Forests.
* Gradient Boosting based classifiers.
* ROC Curve and AUC analysis.
* Automated hyperparameter selection pipelines.
* Comparison with other classification algorithms.

---

# Dependencies

```text
pandas
numpy
matplotlib
scikit-learn
jupyter
```

Install manually:

```bash
pip install pandas numpy matplotlib scikit-learn jupyter
```

---

# Contributors

* Varchas Jasti

---

# License

MIT License