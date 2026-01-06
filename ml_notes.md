
# 📌 Wine Quality Dataset — Initial Data Exploration

## 1. Loading and Inspecting the Dataset

We loaded the `wine.csv` dataset using pandas and explored it using basic inspection methods:

- `data.head()` → shows the **first five rows** of all columns
- `data.tail()` → shows the **last five rows** of all columns
- `data.describe()` → gives **summary statistics** such as count, mean, min, max, etc.

This helped in understanding the structure and range of the data.

---

## 2. Correlation Between Alcohol and Quality 

We calculated the correlation between **alcohol** and **quality**.

- The correlation value was **moderate (~0.48)**
- This means alcohol contributes to quality, but **it is not a strong or sufficient predictor by itself.**
- this not what I observe we just mathematically proved it.

---

## 3. Choosing the Right Plot

While plotting the data, we realized:

- If the data is **ordered** (e.g., time series), we use a **line plot**
- If the data is **unordered**, we use a **scatter plot**

Using a line plot for unordered data creates misleading connections, so for alcohol vs quality, **scatter plot is the correct choice**.

---

## 4. Key Insight About Real-World Data

Real-world data is **messy and noisy**, so:

- Raw data is hard to interpret directly
- The correct workflow is:

  **Load the data → Visualize it → Then analyze/model it**

Visualization comes before math.
