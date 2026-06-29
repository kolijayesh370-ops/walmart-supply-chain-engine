# 📊 Walmart Predictive Supply Chain Engine

An end-to-end Machine Learning pipeline and interactive simulation dashboard designed to forecast weekly retail demand and optimize store inventory fulfillment.

## 🚀 Project Overview
In large-scale retail supply chains, understocking leads to lost revenue, while overstocking incurs massive warehousing overhead. This project bridges that gap by building an intelligent forecasting engine using historical Walmart data. 

By feeding structural features like region profiles, temperature swings, macroeconomics (CPI, Unemployment), and seasonal holiday flags into an ensemble model, the engine instantly computes stock volume targets.

---

## 🔄 Step-by-Step Engineering Pipeline

### 1. Data Cleaning & Structural Ingestion
* **Datetime Standardization:** Raw strings are cast to explicit pandas datetime objects to isolate temporal dependencies (`Week_of_Year`, `Year`).
* **Categorical Feature Optimization:** Location fields (`Store`) are transformed into high-dimensional indicators using One-Hot categorical dummy encoding to map store-specific performance behaviors.
* **Imputation Strategy:** Sparse data entries and missing parameters are systematically filled using feature column medians to maintain mathematical matrix consistency.

### 2. Anomaly Mitigation
* To protect the predictive model from skewing due to extreme, non-replicable revenue events, a target outlier filter clamps data arrays at the **99th percentile cutoff threshold**.

### 3. Model Architecture & Training
* **Algorithm:** Random Forest Regressor Engine (Ensemble Decision Trees).
* **Validation:** 80/20 non-overlapping train/test matrix split.
* **Parallel Processing:** Multi-threaded initialization (`n_jobs=-1`) to maximize compute speeds.

### 4. Interactive Interface Deployment
* Built using an embedded structural interface framework (**Gradio**), bypassing browser proxy limitations and local hosting bottlenecks to deliver live, inline sandbox simulations directly within the runtime workspace.

---

## 📈 Technical Performance Metrics
* **R² Accuracy Score:** ~93% to 95% (variance scales with random seed split).
* **Inference Speed:** Real-time array mapping (<0.5 seconds per query matrix).

---

## 💻 How to Replicate and Run Natively

1. Clone this repository to your local directory:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/walmart-supply-chain-engine.git](https://github.com/YOUR_USERNAME/walmart-supply-chain-engine.git)
