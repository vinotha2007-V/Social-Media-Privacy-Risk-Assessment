# 🔐 Social Media Privacy Risk Assessment Framework

A web-based privacy assessment application that helps users evaluate potential privacy risks associated with their social media habits. It calculates an overall risk score, analyzes ten privacy categories, and provides recommendations to encourage safer online practices.

## 📌 Project Overview

Social media users may unintentionally expose personal information through public profiles, posts, location sharing, third-party applications, and insecure account practices.

The **Social Media Privacy Risk Assessment Framework** provides an interactive questionnaire with 40 questions across 10 privacy categories. Based on user responses, the application calculates privacy risk scores and displays category-wise results with recommendations.

This project is developed for educational purposes and demonstrates web development, REST API integration, data validation, automated testing, and database management.

## ✨ Key Features

* 🔎 **Privacy Risk Assessment** — Evaluate social media privacy habits using an interactive questionnaire.
* 📊 **Overall Risk Score** — Calculate a score from 0 to 100.
* 🗂️ **Category-Wise Analysis** — Analyze privacy risks across ten categories.
* 💡 **Personalized Recommendations** — Display suggestions based on identified risk areas.
* 💾 **Assessment History** — Store assessment results in an SQLite database.
* 🔗 **REST API Integration** — Connect the frontend with a Flask backend.
* 🧪 **Automated Testing** — Validate core risk calculation functionality using pytest.
* 📱 **Responsive Dashboard** — Present results through a user-friendly web interface.

## 🗂️ Privacy Assessment Categories

1. Profile Visibility
2. Personal Information
3. Location Privacy
4. Posts and Content
5. Friends and Followers
6. Tagging and Mentions
7. Authentication and Account Security
8. Third-Party Applications
9. Messaging and Social Engineering
10. Digital Footprint

## 🛠️ Technology Stack

| Component             | Technology            |
| --------------------- | --------------------- |
| Frontend              | HTML, CSS, JavaScript |
| Backend               | Python, Flask         |
| API                   | REST API              |
| Database              | SQLite                |
| Data Processing       | Python                |
| Testing               | pytest                |
| Cross-Origin Requests | Flask-CORS            |
| Version Control       | Git and GitHub        |

## 🏗️ Project Structure

```text
Social-Media-Privacy-Risk-Assessment/
├── backend/
│   ├── app.py
│   ├── risk_engine.py
│   ├── category_analyzer.py
│   ├── recommendations.py
│   ├── assessment_service.py
│   └── database.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── data/
├── tests/
│   └── test_risk_engine.py
├── reports/
├── docs/
├── screenshots/
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### Prerequisites

* Python 3.10 or later
* Git
* A modern web browser
* Visual Studio Code (recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/vinotha2007-V/Social-Media-Privacy-Risk-Assessment.git
cd Social-Media-Privacy-Risk-Assessment
```

### 2. Create a Virtual Environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Backend Server

```bash
cd backend
python app.py
```

The Flask API should run at:

`http://127.0.0.1:5000`

Keep the backend terminal open while using the application.

### 5. Open the Frontend

Open `frontend/index.html` in a browser, or use the VS Code Live Server extension.

If browser requests are blocked when opening the file directly, serve the frontend through a local development server and ensure Flask-CORS is configured appropriately.

## 🔌 API Endpoints

| Method | Endpoint           | Description                        |
| ------ | ------------------ | ---------------------------------- |
| GET    | `/`                | Check API status                   |
| POST   | `/api/assess`      | Calculate and save an assessment   |
| POST   | `/api/categories`  | Analyze category-wise privacy risk |
| GET    | `/api/assessments` | Retrieve assessment history        |

### Example Request

`POST /api/assess`

```json
{
  "answers": [1, 2, 3, 1, 2, 0, 1, 2, 3, 1]
}
```

The API validates the answers and returns an assessment score, risk classification, and assessment identifier.

## 📈 Risk Classification

| Score Range | Risk Level |
| ----------- | ---------- |
| 0–20        | LOW        |
| 21–40       | MODERATE   |
| 41–70       | HIGH       |
| 71–100      | CRITICAL   |

Higher scores indicate more potentially risky privacy habits according to the questionnaire's scoring model.

## 🧪 Run Tests

From the project root, activate the virtual environment and run:

```bash
python -m pytest tests -v
```

The tests cover risk score calculation, risk classification, and invalid input handling.

## 🔒 Security and Privacy Considerations

* Use synthetic answers when demonstrating or testing the application.
* Do not commit `.env` files, credentials, virtual environments, or local database files.
* Validate incoming API data on the backend.
* Avoid entering sensitive personal information during demonstrations.
* Review access controls and deployment security before making the application publicly available.

## 🚀 Future Enhancements

* Interactive analytics and historical risk trends.
* PDF report generation.
* Expanded category-specific assessment tests.
* Improved input validation and API error handling.
* Cloud database integration.
* Authentication and user-specific assessment history.
* Deployment to a cloud hosting platform.

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Python backend development
* Flask REST API development
* Frontend and backend integration
* SQLite database operations
* Data validation and risk scoring
* Automated testing with pytest
* Git and GitHub workflows

## ⚠️ Disclaimer

This application is an educational privacy-awareness tool. Its scores are based on a simplified questionnaire and do not constitute a professional security audit, guarantee of privacy, or comprehensive assessment of any social media platform.

## 👩‍💻 Author

**Vinotha**

GitHub: [vinotha2007-V](https://github.com/vinotha2007-V)

---

⭐ If you find this project useful, consider starring the repository.
