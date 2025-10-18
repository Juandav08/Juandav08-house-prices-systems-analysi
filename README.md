# Workshop 1 – House Prices: Advanced Regression Techniques

## Project Description
This repository contains the LaTeX source files and analysis for **Workshop 1**, which is based on the Kaggle competition [House Prices: Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques). The main goal of the competition is to predict the final sale price of residential homes in Ames, Iowa, using a dataset with 79 explanatory variables.

The work developed here frames the dataset and the prediction task within a **systemic analysis approach**, considering not only the features provided but also the broader socio-technical environment in which real estate markets operate.

---

## Methodology and Analysis

### 1. Dataset Overview
- **Training set (`train.csv`)**: 1460 entries with 79 features plus the target variable `SalePrice`.
- **Test set (`test.csv`)**: 1459 entries with the same features, without `SalePrice`.

The variables include numerical (e.g., lot area, year built), categorical (e.g., neighborhood, house style), and ordinal features (e.g., overall quality).

### 2. Evaluation Metric
The competition evaluates models using the **Root Mean Squared Error (RMSE)** between the logarithm of predicted and actual house prices:

$$RMSE = \sqrt { \frac{1}{n} \sum_{i=1}^{n} (\log(y_i) - \log(\hat{y}_i))^2 }$$

### 3. Systemic Analysis
The housing price prediction task was studied as a **system**, considering:
- **Key elements**: dataset, features, target variable, external factors not included, and stakeholders.
- **Relationships**: how physical, locational, and qualitative features interact to influence price.
- **Boundaries**: dataset limitations compared to the open and dynamic real-world housing market.
- **Sensitivity**: the impact of internal (missing values, nonlinearities) and external factors (interest rates, economic cycles).
- **Complexity and chaos**: the role of feedback loops, speculation, and unpredictable shocks.

A diagram was developed to visualize the relationships and feedback loops that influence housing prices.

### 4. References
- Blanchard, B. S., & Fabrycky, W. J. (2014). *Systems Engineering and Analysis* (5th ed.). Pearson.
- Kaggle. (2021). *House Prices: Advanced Regression Techniques*. Retrieved from [Kaggle](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques).

---

## Final Report
The full analysis and conclusions are available in the compiled PDF:
[Workshop_1.pdf](Report.pdf/Workshop_1.pdf)

--- 
#  Workshop 2 — Kaggle Systems Design

##  Overview

The lastest updates contains the deliverables for **Workshop #2** of the *Systems Analysis & Design* course.  
Building upon the analytical results obtained in **Workshop #1**, this phase focuses on **system design**, integrating **engineering principles**, **chaos theory considerations**, and **sensitivity management** into a comprehensive architecture.

The system designed aims to **predict house prices** for the **Ames Housing dataset** (Kaggle Competition), following a **modular, scalable, and maintainable architecture** based on systems engineering practices.

---

##  Objectives

- Develop a **system architecture** covering data ingestion, preprocessing, modeling, deployment, and monitoring.  
- Apply **systems engineering principles** such as modularity, scalability, and maintainability.  
- Incorporate strategies for managing **chaos and sensitivity**, ensuring robustness against unpredictable inputs.  
- Produce a **System Design Document (PDF)** detailing components, diagrams, and design decisions.  
- Maintain clear documentation and reproducibility across all stages of development.

---

##  System Architecture Overview

The system is structured into six primary subsystems:

1. **Data Ingestion** — Loads and validates `train.csv` and `test.csv`, performing schema and range checks.  
2. **Data Processing** — Handles missing values, encodes categorical variables, scales features, and stores processed data.  
3. **Modeling & Training** — Integrates preprocessing with model training, cross-validation, and hyperparameter tuning.  
4. **Serving & Deployment** — Provides batch and real-time prediction endpoints.  
5. **Monitoring & Feedback** — Detects data drift and triggers retraining when necessary.  
6. **Pipeline Orchestration** — Automates workflow execution using tools such as Airflow or MLflow.

This modular architecture ensures **traceability**, **adaptability**, and **continuous improvement**.

---

##  Sensitivity and Chaos Management
To handle chaotic behavior and sensitive variables in the housing market:

- **Normalization and Scaling:** Stabilize training and reduce sensitivity to feature magnitude.  
- **Regularization:** Apply L1/L2 penalties and ensemble models to improve robustness.  
- **Cross-Validation:** Use K-Fold CV to ensure stable and generalizable results.  
- **Feedback Loops:** Integrate model error monitoring to guide data enrichment and retraining.  
- **Continuous Monitoring:** Log data drift, anomalies, and performance degradation.

These mechanisms enable the system to adapt to dynamic market behaviors and maintain prediction accuracy.

---

##  Implementation Plan

1. **Data Preparation** — Load and inspect datasets.  
2. **Preprocessing** — Handle missing data, outliers, and encoding.  
3. **Feature Engineering** — Create derived features and apply scaling.  
4. **Model Training** — Train and validate multiple regression models.  
5. **Model Evaluation** — Compute RMSE and compare models.  
6. **Explainability** — Generate SHAP-based interpretability visualizations.  
7. **Output Generation** — Save final predictions and metrics to `/results`.  
8. **Integration** — Connect all modules via `main.py` for end-to-end execution.

---

##  Acceptance Criteria

- Complete end-to-end pipeline execution (ingestion → preprocessing → training → evaluation → deployment).  
- RMSE metric computed and reported for all candidate models.  
- Automatic retraining triggered upon drift or performance degradation.  
- All artifacts (models, metrics, configurations) stored in version-controlled repositories.

---
## 🧾 Deliverables

- **📄 System Design Document:** [Workshop_2.pdf](Report.pdf/Workshop_2.pdf)  
- **📘 README.md:** Current file summarizing the workshop, objectives, and implementation details.  
- **📂 GitHub Repository:** Includes all code modules, documentation, and generated results.



