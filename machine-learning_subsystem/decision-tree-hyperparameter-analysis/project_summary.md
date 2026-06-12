# Decision Tree Hyperparameter Tuning

## Project Overview

This project studies the effect of different Decision Tree hyperparameters on classification performance using the Breast Cancer Wisconsin Dataset from Scikit-Learn.

The objective was to identify the combination of hyperparameters that provides the best balance between model accuracy and generalization using:

- Train/Test Split
- 5-Fold Cross Validation
- Accuracy
- Log Loss

---

# Dataset Overview

### Dataset Head

![Dataset Head](images/dataset_head.png)

### Dataset Shape and Information

![Dataset Shape and Info](images/dataset_shape_and_info.png)

### Dataset Description

![Dataset Description](images/dataset_description.png)

---

# Baseline Model

A default Decision Tree Classifier was trained to establish a reference point for all subsequent experiments.

### Baseline Parameters

![Baseline Parameters](images/baseline_parameters.png)

### Baseline Tree

![Baseline Tree](images/baseline_tree.png)

---

# Hyperparameter Studies

Each hyperparameter was varied independently while all others remained unchanged.

---

## 1. Criterion

### Accuracy

![Criterion Accuracy](images/criterion_accuracy.png)

### Log Loss

![Criterion Loss](images/criterion_loss.png)

**Observation:**  
The study compares Gini and Entropy criteria to determine which splitting strategy produces better predictive performance.

---

## 2. Maximum Depth

### Accuracy

![Depth Accuracy](images/depth_accuracy.png)

### Log Loss

![Depth Loss](images/depth_loss.png)

**Observation:**  
Tree depth strongly influences underfitting and overfitting behaviour.

---

## 3. Maximum Leaf Nodes

### Accuracy

![Leaf Accuracy](images/leaf_accuracy.png)

### Log Loss

![Leaf Loss](images/leaf_loss.png)

**Observation:**  
Restricting the number of leaf nodes reduces model complexity and can improve generalization.

---

## 4. Minimum Samples Split

### Accuracy

![Split Accuracy](images/split_accuracy.png)

### Log Loss

![Split Loss](images/split_loss.png)

**Observation:**  
Changing the minimum samples required for a split affects how aggressively the tree grows.

---

## 5. Minimum Samples Leaf

### Accuracy

![Leaf Sample Accuracy](images/leafsample_accuracy.png)

### Log Loss

![Leaf Sample Loss](images/leafsample_loss.png)

**Observation:**  
Larger leaf sizes create smoother and less complex decision boundaries.

---

## 6. CCP Alpha (Cost Complexity Pruning)

### Accuracy

![Alpha Accuracy](images/alpha_accuracy.png)

### Log Loss

![Alpha Loss](images/alpha_loss.png)

**Observation:**  
Pruning helps remove unnecessary branches and improve model generalization.

---

# Hyperparameter Summary

The best-performing value from each tuning experiment was collected and used to construct the final model.

![Hyperparameter Summary](images/hyperparameter_summary.png)

---

# Final Tuned Model

The optimal hyperparameters obtained from the individual studies were combined to create the final Decision Tree model.

### Tuned Tree

![Tuned Tree](images/tuned_tree.png)

---

# Model Comparison

### Performance Comparison

![Comparison](images/comparison.png)

### Confusion Matrices

![Confusion Matrices](images/confusion_matrices.png)

---

# Conclusion

- Hyperparameter tuning improved model performance over the baseline Decision Tree.
- Cross-validation helped identify robust parameter values.
- Pruning and complexity-control parameters contributed significantly to better generalization.
- The final tuned model achieved stronger overall classification performance while maintaining interpretability.

---