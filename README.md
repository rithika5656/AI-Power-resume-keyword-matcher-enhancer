📄 Resume Keyword Matcher

A simple yet powerful Streamlit-based Resume Analyzer that compares a candidate's resume with a job description and calculates a skill matching score.

This tool extracts text from PDF, DOCX, and TXT files, identifies relevant skills, and highlights matching keywords. Perfect for students, job seekers, or recruiters who want a quick resume–JD matching tool.

🚀 Features

Upload Resume (PDF/DOCX)

Upload Job Description (PDF/DOCX/TXT)

Auto-extract text using pdfplumber and python-docx

Detect predefined skills in resume and JD

Show:

Resume skills found

Job description skills

Matched skills

Match percentage score

Clean and interactive Streamlit UI

🛠️ Tech Stack

Python

Streamlit

pdfplumber

python-docx

Regex

File handling (PDF/DOCX/TXT)

📥 Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Install Dependencies

Create a virtual environment (optional):

pip install -r requirements.txt


Your requirements.txt should contain:

streamlit
pdfplumber
python-docx

3️⃣ Run the Streamlit App
streamlit run app.py

📌 How It Works

User uploads a resume and a job description.

App extracts text from both using:

pdfplumber → PDFs

python-docx → DOCX

Direct decode → TXT

Predefined skills list is checked against both texts.

Matched skills are highlighted.

A Match Score (%) is calculated:

(matched skills / job description skills) * 100

🧩 Predefined Skills Checked
python, java, c++, sql, machine learning, 
data analysis, deep learning, tensorflow, pytorch, 
react, nlp, excel, communication


You can edit the skill list in the code.

📷 App UI Preview

(Add screenshot if you have one)

📚 Folder Structure
📁 Resume-Keyword-Matcher
│── app.py
│── requirements.txt
│── README.md

🧑‍💻 Code Snippet (Main Logic)
resume_text = extract_text(resume_file)
job_text = extract_text(job_file)

resume_skills = extract_skills(resume_text, skills_list)
job_skills = extract_skills(job_text, skills_list)

matched_skills = list(set(resume_skills) & set(job_skills))
match_score = round(len(matched_skills) / len(job_skills) * 100, 2)

🤝 Contributing

Pull requests are welcome! If you'd like to add features like:
✔ NLP-based skill extraction
✔ Resume scoring model
✔ Dashboard & charts
✔ Custom skill uploads

Feel free to contribute.

⭐ Show Some Love

If you found this useful, please give the repository a ⭐ star to support!
