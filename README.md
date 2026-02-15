# Customer Segmentation System (KMeans + Streamlit)

## 📌 Project Overview

This project is an **end-to-end Customer Segmentation System** that groups customers into meaningful clusters using Machine Learning. The model is trained dynamically on the dataset and deployed using an interactive **Streamlit dashboard**.

The application helps businesses understand different customer segments and take **data-driven marketing decisions**.

---

## 🚀 Features

✔ Customer segmentation using KMeans clustering

✔ Interactive Streamlit dashboard

✔ Real-time customer prediction

✔ Business recommendations for each segment

✔ Data visualization and cluster analysis

✔ Upload CSV file for bulk segmentation

✔ Download segmented results

✔ Model training inside the application

---

## 🎯 Business Problem

Businesses have large volumes of customer data but lack clear segmentation strategies.
This system helps to:

* Identify premium and budget customers
* Improve targeted marketing
* Increase customer retention
* Optimize pricing and product strategies

---

## 🧠 Machine Learning Approach

The system uses **unsupervised learning (KMeans clustering)**.
Instead of loading a pre-trained model, the application:

1. Loads the dataset
2. Preprocesses and scales features
3. Trains the KMeans model dynamically
4. Predicts customer segments in real time

Features used:

* Income
* Age
* Family size
* Recency
* Spending score

The model assigns new customers to the closest cluster based on similarity.

---

## 📊 Customer Segments Example

| Cluster   | Description            | Business Strategy |
| --------- | ---------------------- | ----------------- |
| Premium   | High income & spending | Exclusive offers  |
| Budget    | Low spending           | Discounts         |
| Potential | Medium customers       | Targeted ads      |
| Family    | Family-oriented        | Bundle products   |

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* Pandas, NumPy
* Matplotlib / Plotly
* Streamlit

---

## 📈 Visualizations

The dashboard includes:

* Cluster distribution
* Feature insights
* Elbow method for optimal cluster selection

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Aryan-H2005/customer-segmentation.git
cd customer-segmentation
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate:

```bash
# Windows
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
customer-segmentation/
│
├── app.py
├── data/
│   └── customer_segmentation.csv
├── notebooks/
├── requirements.txt
└── README.md
```

---

## 🌐 Deployment

The application can be deployed on:

* Streamlit Cloud
* Render
* AWS

---

## 💡 Future Improvements

* Save trained model for faster predictions
* RFM segmentation
* Customer Lifetime Value
* Churn prediction
* Recommendation system
* FastAPI backend

---

## 📌 Resume Impact

This project demonstrates:

* Machine Learning
* Data preprocessing
* Visualization
* Deployment
* Business decision-making

---

## 👨‍💻 Author

Aryan Harke

---

## ⭐ Support

If you like this project, give it a star and feel free to contribute.
