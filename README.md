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
[Workshop_1.pdf](./Workshop_1.pdf)
