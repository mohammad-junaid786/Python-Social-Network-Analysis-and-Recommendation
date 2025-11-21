# Social Network Analysis & Recommendation System (Pure Python)

Welcome to the **Social Network Analysis & Recommendation System** repository!  
This project was built entirely in **Jupyter Lab** using **pure Python**.

It simulates a small social network dataset and performs:
- 📄 Data reporting (users, friends, liked pages)
- 🧹 Data cleaning
- 👥 “People You May Know” recommendations
- 👍 “Posts You Might Like” suggestions

This project demonstrates how a social platform might suggest **new people to connect with** and **new pages to engage with**, using only **Python logic** (no external libraries).

---

## 🧠 Purpose of the Project

This project helped me strengthen my understanding of:

- Python fundamentals
- JSON data handling
- Data cleaning and preprocessing
- Functions, loops, sets, and dictionaries
- Building basic recommendation logic
- Writing structured scripts instead of scattered code

All code was **first practiced in Jupyter Lab** and later organized into Python scripts for clarity and GitHub structure.

---

## 📂 Repository Structure

```text
social-network-analysis-project/
│
├── data/
│   ├── data.json                # Raw social network data
│   ├── data2.json               # Data before cleaning
│   └── massive_data.json        # Larger dataset for recommendations
│
├── scripts/
│   ├── 01_data_report.py        # Reads + displays users & pages
│   ├── 02_clean_data.py         # Data cleaning logic
│   ├── 03_find_people.py        # "People You May Know"
│   └── 04_recommend_pages.py    # "Posts You Might Like"
│
└──  README.md                    # Project documentation

```

---

## 📌 Project Workflow & Scripts

### 1️⃣ `01_data_report.py` – Data Report
- Loads data.json
- Displays:
    • User ID and name  
    • Their list of friends  
    • Their liked pages  
- Prints all page IDs and names  
- Purpose: understand dataset structure  

### 2️⃣ 02_clean_data.py – Data Cleaning
- Removes users with empty names  
- Removes duplicate friends  
- Removes inactive users  
- Removes duplicate pages  
- Saves clean data to cleaned_data_2.json  

### 3️⃣ 03_find_people.py – “People You May Know”
- Builds a dictionary: user_id → friends  
- Finds mutual friends  
- Calculates scores using friend connections  
- Recommends new people to connect with  

### 4️⃣ 04_recommend_pages.py – “Posts You Might Like”
- Builds a dictionary: user_id → liked pages  
- Finds similar users (with common page interests)  
- Recommends pages not yet liked by the main user  

---

## 🔹 Run in Jupyter Lab (Recommended)
1. Open Jupyter Lab
2. Create a new notebook
3. Copy code from each script into separate cells
4. Run step by step for output and learning

---

## 📖 What I Learned from This Project
- Handling JSON data  
- Cleaning and preprocessing raw data  
- Using sets and dictionaries efficiently  
- Writing reusable Python functions  
- Building logic-based recommendation systems  
- Thinking like a data analyst/programmer  


---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and share this project with proper attribution.

---

## 🎓 Acknowledgment

This project was created by following along with the course:  
**[The Ultimate Job Ready Data Science Course](https://www.codewithharry.com/courses/the-ultimate-job-ready-data-science-course)**  
by **CodeWithHarry**.

All credit goes to the instructor for explaining the concepts clearly.  
I built this project as part of my learning journey — by practicing in Jupyter Lab and **replicating the steps to better understand Python, data cleaning, and logic-based recommendation systems**.

This repository represents my **hands-on practice**, where I wrote each script manually to strengthen my Python fundamentals.

---

## 🌟 About Me

Hi there! I'm **Mohammad Junaid**, a dedicated learner with a background in **Business Administration** and a strong interest in **data, analytics, and technology**. I enjoy working on projects that allow me to explore real-world data, improve my technical skills, and deliver valuable insights.

Always curious and committed to growth, I’m on a continuous journey of learning and applying practical knowledge in tech.


