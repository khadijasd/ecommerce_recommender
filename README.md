# 🛍️ E-commerce Product Recommendation System

This is a simple **content-based recommender system** for an online store.  
It suggests similar products based on their category, brand, and other metadata using **cosine similarity**.

---

## 📌 Features

- Content-based product recommendations
- Product similarity using TF-IDF + cosine similarity
- Modular and testable Python code
- Jupyter notebook for interactive testing
- Scalable project structure

---

## 📁 Project Structure

ecommerce_recommender/
├── data/
│ ├── products.csv # Product data
│ └── users.csv  # Customer preferences
├── ecommerce_recommender/
│ ├── recommender.py # Core recommendation logic
│ ├── utils.py # Display helpers
│ └── init.py
├── notebooks/
│ └── exploration.ipynb # Jupyter notebook for testing
├── tests/
│ └── test_recommender.py # Unit test
├── requirements.txt # Dependencies
└── README.md # This file



---

## ⚙️ How It Works

1. Loads product data from `products.csv`
2. Combines category and brand into a single text feature
3. Vectorizes product features using **TF-IDF**
4. Calculates similarity between products using **cosine similarity**
5. Returns top N similar products for any given product

---

## 📦 Example Data (`data/products.csv`)

```csv
product_id,product_name,category,brand,price
1,Sneakers,Shoes,Nike,79.99
2,Running Shoes,Shoes,Adidas,89.99
3,T-shirt,Clothing,Nike,25.99
4,Jeans,Clothing,Levis,45.00
5,Hoodie,Clothing,Adidas,39.99

---


```bash
## ⚙️Install dependencies:
pip install -r requirements.txt