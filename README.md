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

# Workshop 3 — Robust System Design and Project Management

## Overview

This repository now includes the deliverables for **Workshop #3** of the *Systems Analysis & Design* course.  
Building upon the results and architecture developed in **Workshop 1** (Systemic Analysis) and **Workshop 2** (System Design), this phase focuses on strengthening the system’s **robustness, quality assurance**, and **project management practices**.

The goal is to ensure that the predictive system for the *Kaggle House Prices* competition is not only technically functional but also **reliable, maintainable, and managed under structured project control**. The workshop integrates **robust engineering**, **risk management**, and **agile methodologies** into a coherent, high-quality development process.

---

## Objectives

- Refine and document a **robust system architecture** aligned with ISO 9000 and CMMI principles.  
- Identify potential **risks and failure points**, proposing mitigation and monitoring strategies.  
- Define a complete **project management plan** including team roles, milestones, and agile practices.  
- Apply **Scrum methodology** to manage sprints, reviews, and retrospectives.  
- Ensure **traceability, reproducibility, and continuous improvement** through version control and quality checks.  
- Document **incremental improvements** derived from previous workshops.

---

## Robust Architecture Overview

The refined system architecture emphasizes **fault tolerance, scalability, and maintainability**.  
It is structured into six modular subsystems:

1. **Data Ingestion** — Validates and loads raw data while performing schema and consistency checks.  
2. **Processing** — Applies imputation, encoding, feature scaling, and outlier mitigation.  
3. **Modeling** — Integrates preprocessing and training pipelines with hyperparameter optimization.  
4. **Serving** — Provides batch and online prediction interfaces for inference.  
5. **Monitoring** — Detects performance drift and data distribution changes.  
6. **Orchestration** — Coordinates the entire workflow via automated scheduling and retraining.

Key design principles:
- **Modularity:** Independent components with clear data interfaces.  
- **Scalability:** Support for horizontal expansion of processing and model serving.  
- **Fault Tolerance:** Use of checkpoints and recovery mechanisms during data processing.  
- **Maintainability:** Clean, version-controlled modular codebase (GitHub).  
- **Traceability:** Monitoring and logging pipelines for reproducibility and auditability.

The architecture aligns with **ISO 9000** standards for quality assurance and **CMMI maturity level practices** for process improvement and control.

---

## Risk and Quality Management

A formal **Risk Identification and Mitigation Plan** was developed to ensure system reliability across technical and operational dimensions.

| **Risk** | **Description** | **Impact** | **Mitigation Strategy** | **Monitoring Method** |
|-----------|-----------------|-------------|--------------------------|-----------------------|
| Data Loss | Dataset corruption or deletion during preprocessing or storage. | High | Maintain version-controlled backups in GitHub repositories. | Weekly checksum validation. |
| Model Drift | Decline in model performance due to changing data distributions. | Medium | Track RMSE deviations and trigger automated retraining. | Post-training performance reviews. |
| Security Breach | Unauthorized access to project repositories. | Medium | Enforce two-factor authentication and least-privilege access policies. | Access log audits. |
| Team Coordination Failure | Communication breakdown or task overlap among sub-teams. | Medium | Use Trello-based Kanban boards and weekly Scrum meetings. | Sprint review tracking. |
| Implementation Error | Bugs or inconsistencies during preprocessing or modeling. | Low | Conduct peer code reviews and automated unit tests. | Continuous integration checks. |

This framework guarantees that quality assurance and risk mitigation are continuously monitored and updated throughout each sprint.

---

## Project Management and Methodology

The team adopted the **Scrum framework** to manage development cycles. Roles and responsibilities were clearly assigned:

- **Product Owner (Juan David Zárate Moya):** Defines the project vision, manages backlog, and ensures alignment between academic and technical objectives.  
- **Scrum Master (Kevin David Rincón Valencia):** Facilitates communication, removes blockers, and ensures adherence to Scrum principles.  
- **Development Team (Jesús Mateo Múnevar Méndez & Juan David Romero Morales):** Designs, implements, and tests all technical components.

### Scrum Implementation
| **Scrum Element** | **Application in Project** |
|--------------------|----------------------------|
| Product Backlog | List of functionalities and deliverables (ingestion, preprocessing, modeling, documentation). |
| Sprint | Weekly iterations (e.g., architecture refinement, risk analysis, simulation design). |
| Daily Scrum | Asynchronous updates via WhatsApp/GitHub messages. |
| Sprint Review | Presentation of progress and outcomes from each sub-team. |
| Retrospective | Discussion of improvements for the next iteration. |

The team combined **Trello (Kanban)** and **TeamGantt (Gantt chart)** to visualize progress, ensuring task traceability and balanced workload distribution.

---

## Quality Assurance

Quality was maintained through:
- **Version control (GitHub)** with independent branches and peer review merges.  
- **Collaborative sprint reviews** for early feedback.  
- **Verification & validation** for each pipeline module (ingestion, preprocessing, modeling).  
- **Continuous improvement** via logged monitoring metrics and testing iterations.

These practices ensure system reliability, transparency, and academic integrity.

---

## Incremental Improvements and Lessons Learned

The project evolved significantly across workshops:

- **Workshop 1:** Established a systemic understanding of the real estate prediction problem, identifying sensitivity and complexity.  
- **Workshop 2:** Defined a modular architecture and integrated sensitivity management techniques (scaling, regularization, monitoring).  
- **Workshop 3:** Consolidated these insights into a robust, agile-managed system with risk control and continuous improvement practices.

Through this iterative process, the team achieved a **robust, maintainable, and scalable predictive system**, reflecting both engineering discipline and adaptability to dynamic data environments.

---

## 🧾 Deliverables

- **📄 Robust System Design Report:** [Workshop_3.pdf](Report.pdf/Workshop_3.pdf)  
- **📘 README.md:** Updated file summarizing all workshops and project progression.  
- **📂 GitHub Repository:** Includes LaTeX source files, diagrams, risk management tables, and architecture updates.

---




