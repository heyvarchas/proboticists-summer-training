# Project Title

Implementation of Linear Regression from scratch using both the Pseudo-Inverse method and Gradient Descent, with model evaluation and convergence visualization.

---

# Overview

This project demonstrates the complete implementation of Linear Regression on a multivariate dataset containing 10 input features and 1 target variable. The project explores two different approaches for learning model parameters:

* Closed-form solution using the Pseudo-Inverse
* Iterative optimization using Gradient Descent

The notebook also evaluates model performance using standard regression metrics and visualizes prediction quality and convergence behavior.

---

# Features

* Dataset loading and exploration using Pandas.
* Data preparation and feature-target separation.
* Bias term incorporation for linear regression.
* Linear Regression implementation using the Pseudo-Inverse method.
* Linear Regression implementation using Gradient Descent.
* Prediction generation using both approaches.
* Performance evaluation using:

  * Mean Squared Error (MSE)
  * Root Mean Squared Error (RMSE)
  * R² Score
* Loss convergence visualization across training epochs.
* Comparison of actual vs predicted values.
* Fully documented notebook with references and explanations.

---

# System Workflow

1. Load the dataset from CSV format.
2. Explore dataset structure, shape, and statistics.
3. Separate feature variables and target variable.
4. Add a bias column to the feature matrix.
5. Train a Linear Regression model using the Pseudo-Inverse method.
6. Generate predictions and evaluate model performance.
7. Implement Gradient Descent from scratch.
8. Train the Gradient Descent model over multiple epochs.
9. Visualize convergence of the training process.
10. Compare predictions from both approaches.
11. Analyze results and draw conclusions.

---

# Demo

The notebook demonstrates:

* Dataset exploration and preprocessing.
* Parameter computation using matrix operations.
* Gradient Descent optimization.
* Evaluation metric calculation.
* Convergence plots.
* Prediction comparison visualizations.

The outputs generated throughout the notebook provide a complete walkthrough of the Linear Regression pipeline.

---

# Hardware Requirements

* Any modern laptop or desktop computer.
* Minimum 4 GB RAM recommended.
* No GPU is required.

---

# Software Requirements

* Python 3.x
* Jupyter Notebook

Required Python libraries:

* pandas
* numpy
* matplotlib

---

# Project Structure

```text
.
├── Documentation.ipynb
├── linear_regression_dataset.csv
├── grad_descent_convergence.png
├── models_visualisation.png
├── result.png
└── README.md
```

* `Documentation.ipynb` contains the complete implementation, explanations, references, visualizations, and analysis.
* `linear_regression_dataset.csv` contains the dataset used for training and evaluation.
* `grad_descent_convergence.png` shows the convergence of the model using gradient descent.
* `models_visualisation.png` shows the actual v/s predicted values for the data points using both models.
* `result.png` shows the final result obtained and compares the two approaches for linear prediction.
* `README.md` provides project documentation.

---

# Installation

1. Clone the repository:

```bash
git clone https://github.com/heyvarchas/proboticists-summer-training.git
cd .\proboticists-summer-training\machine-learning_subsystem\linear-regression\
```

2. Create and activate a virtual environment (optional):

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

3. Install the required dependencies:

```bash
pip install pandas numpy matplotlib jupyter
```

4. Launch Jupyter Notebook:

```bash
jupyter notebook
```

5. Open `Documentation.ipynb` and run the cells sequentially.

---

# Usage

1. Place the dataset file in the project directory.
2. Open the notebook.
3. Run all cells in order.
4. Observe:

   * Data preprocessing steps
   * Model training
   * Evaluation metrics
   * Convergence plots
   * Prediction visualizations

---

# How It Works

### Data Preparation

The dataset is loaded using Pandas. Feature columns are separated from the target column and converted into NumPy arrays for numerical computation.

### Bias Addition

A column of ones is appended to the feature matrix so that the intercept term can be incorporated into matrix operations.

### Pseudo-Inverse Method

The Linear Regression coefficients are computed directly using the Moore-Penrose Pseudo-Inverse:

* No iterative training required.
* Produces the least-squares solution.
* Efficient for smaller datasets.

### Gradient Descent

Gradient Descent is implemented from scratch and trained over multiple epochs.

Key components:

* Learning rate: 0.01
* Epochs: 400
* Iterative parameter updates
* Loss minimization through gradient computation

### Model Evaluation

Both approaches are evaluated using:

* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

These metrics help quantify prediction accuracy and goodness of fit.

### Visualization

The notebook visualizes:

* Loss reduction during Gradient Descent training.
* Comparison of actual vs predicted values.
* Relative performance of both implementations.

---

# Results

The project successfully:

* Loads and preprocesses the dataset.
* Implements Linear Regression using the Pseudo-Inverse method.
* Implements Linear Regression using Gradient Descent.
* Generates predictions for both models.
* Evaluates model performance using multiple metrics.
* Visualizes convergence behavior.
* Compares prediction quality across both approaches.

The results show that both methods achieve strong predictive performance, with the Pseudo-Inverse solution providing the exact least-squares result and Gradient Descent converging closely to the same solution.

---

# Challenges Faced

* Understanding matrix-based implementation of Linear Regression.
* Learning the mathematical intuition behind the Pseudo-Inverse.
* Implementing Gradient Descent from scratch without machine learning libraries.
* Selecting suitable hyperparameters such as learning rate and number of epochs.
* Visualizing model performance effectively for a multivariate dataset.

These challenges were addressed through experimentation, reference materials, and iterative testing.

---

# Future Improvements

* Add train-test splitting for more realistic evaluation.
* Implement feature scaling and normalization.
* Experiment with different learning rates.
* Add regularization techniques such as Ridge and Lasso Regression.
* Compare results with Scikit-Learn implementations.
* Extend the notebook to support polynomial regression.
* Introduce cross-validation for robust performance analysis.

---

# Dependencies

* pandas
* numpy
* matplotlib
* jupyter

---

# Contributors

* Varchas Jasti

---

# License

MIT License.