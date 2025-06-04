# 👶 Fetal Health Classifier — ML Web App (FastAPI + GCP + CI/CD)

An end-to-end machine learning web application that classifies fetal health into **Normal**, **Suspect**, or **Pathological** using cardiotocographic (CTG) data.

Built with ❤️, deployed with ☁️, and tracked like a pro with 🔍 MLflow.

---

## 📁 Project Structure

```
.
├── .github/workflows/        # CI/CD GitHub Actions workflows
├── data/                     # Preprocessed dataset for retraining
├── model/                    # Saved models + experiment artifacts
├── static/style/             # Custom CSS styles
├── templates/                # HTML templates for FastAPI frontend
├── Dockerfile                # Container definition for deployment
├── Train.ipynb               # Model training + experimentation
├── main.py                   # FastAPI backend + route handlers
├── requirements.txt          # Python dependencies
```

---

## 📊 Dataset

We used the **Fetal Health Classification Dataset**, containing cardiotocographic (CTG) features to classify fetal states into:

* `0` → **Normal**
* `1` → **Suspect**
* `2` → **Pathological**

Dataset Source: [Kaggle - Fetal Health Classification](https://www.kaggle.com/datasets/andrewmvd/fetal-health-classification)

---

## 🔬 Model Development

* **Feature Engineering**: Performed extensive preprocessing and feature selection
* **Algorithms Tried**:

  * Decision Tree Classifier (DTC)
  * Logistic Regression
  * Random Forest Classifier (RFC)
  * XGBoost Classifier
* **Experiment Tracking**: All experiments logged with **MLflow** for easy comparison and reproducibility
* **Final Model**: Best model selected based on accuracy and F1-score

---

## 🎨 Frontend + Backend

* **FastAPI** backend to serve prediction APIs and frontend pages
* **Jinja2** templates for dynamic HTML rendering
* **CSS** styling with custom themes under `static/style/`
* **Prediction Form**: Users can input features via UI and receive instant predictions

---

## ⚙️ CI/CD with GitHub Actions

* Whenever the `data/` folder is updated, the pipeline:

  1. Triggers a new training job using the updated data
  2. Retrains the model and saves it to `model/`
  3. Rebuilds and redeploys the FastAPI app with the new model

All of this is automated via GitHub Actions and Docker.

---

## ☁️ Deployment on Google Cloud Run

* **Dockerized** the FastAPI app
* Deployed using **Google Cloud Build** and **Cloud Run**
* Lightweight and scalable with fully managed serverless architecture
* Exposed endpoint for predictions: `https://<your-cloud-run-url>`

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repo
$ git clone https://github.com/your-username/fetal-health-classifier.git
$ cd fetal-health-classifier

# 2. Install dependencies
$ pip install -r requirements.txt

# 3. Run the app
$ uvicorn main:app --reload

# Open browser: http://127.0.0.1:8000
```

---

## 📦 Docker Support

```bash
# Build the image
docker build -t fetalhealthapp .

# Run the container
docker run -p 8080:8080 fetalhealthapp
```

---

## 🧠 Future Work

* Integrate Prometheus & Grafana for live monitoring
* Add model explainability with SHAP/Plotly
* Build a continual learning system to combat data & concept drift

---

## 🙌 Credits

* Dataset: Kaggle
* Dev: [Yash Suthar](https://github.com/yashsthr10)
* Stack: Python, FastAPI, MLflow, Docker, GitHub Actions, GCP

---

## 📢 License

MIT License — free to use, modify, or deploy.
