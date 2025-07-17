# IDS-Project-Folder
#  Intrusion Detection System using Machine Learning (IDS)

This project is a Machine Learning-based Intrusion Detection System (IDS) designed to detect and classify network traffic as either normal or malicious. It uses the NSL-KDD dataset and a Random Forest Classifier to identify different types of cyberattacks. A user-friendly interface is built using Streamlit for real-time prediction and visualization.

---

# Project Objectives

- Detect network intrusions automatically using machine learning
- Improve the accuracy and efficiency of intrusion detection systems
- Provide a simple web-based interface for real-time predictions
- Offer insights through graphical representation of model results

---

# Technologies Used

| Tool        | Purpose                        |
|-------------|--------------------------------|
| Python      | Core programming language      |
| Pandas      | Data loading & manipulation    |
| NumPy       | Numerical computations         |
| Scikit-learn| Machine Learning algorithms    |
| Streamlit   | Web dashboard development      |
| Matplotlib  | Data visualization             |
| Seaborn     | Enhanced plotting              |
| Joblib      | Model saving/loading           |

---

#  Dataset Used

**NSL-KDD Dataset**  
An improved version of the KDD Cup 1999 dataset commonly used for network intrusion detection research.  
It includes attack categories such as:
- **DoS** (Denial of Service)
- **Probe**
- **R2L** (Remote to Local)
- **U2R** (User to Root)

 Download it from:
- [UNB Official Website](https://www.unb.ca/cic/datasets/nsl.html)
- [GitHub Mirror](https://github.com/defcom17/NSL_KDD)

---

# Features

- ✅ Preprocessing of dataset (Label Encoding + Normalization)
- ✅ Training using Random Forest Classifier
- ✅ Model Evaluation (Accuracy, Precision, Recall, F1-Score)
- ✅ CSV Upload for Batch Prediction
- ✅ Real-time prediction via Streamlit
- ✅ Charts (Bar/Pie) for visual output

---

# How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/IshuNishu/IDS-Project-Folder.git
cd IDS-Project-Folder
2. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
Or manually install:

bash
Copy
Edit
pip install pandas scikit-learn numpy streamlit matplotlib seaborn joblib
3. Run the App
bash
Copy
Edit
streamlit run app.py
 Output Preview


 Future Enhancements
Integration with real-time traffic monitoring (e.g., Wireshark, packet sniffers)

Deep learning models (CNN, RNN) for better pattern detection

Auto-training with updated datasets

Deployment in military/defense-grade cybersecurity environments


 Author
Nisha Singh
B.Tech CSE Student

License
This project is intended for academic and educational use only.