**AI Resume Generator & Optimizer**

**DEMO:** https://drive.google.com/file/d/1gU8q5dsQCDQlcPYde8o-C8Q36qnDpeC9/view

An intelligent resume-enhancement system built using Next.js, Flask, LangChain, DeepSeek, and Ollama.
This project takes an existing resume and a job description, analyzes both, and rewrites the resume to maximize ATS (Applicant Tracking System) keyword match, clarity, and relevance.

The system currently focuses on resume optimization, and new features like resume creation from scratch are being developed.

**🚀 Tech Stack**
**Frontend**

Next.js 

Handles:

Resume file upload

Job description input

Displaying optimized resume

Downloading generated PDF

**Backend**

Flask (Python)

LangChain for LLM orchestration

DeepSeek LLM (7B) running locally via Ollama

Sentence extraction + preprocessing utilities

PDF generation using FPDF

**AI**

Local LLM inference through Ollama

DeepSeek LLM for:

Content rewriting

ATS optimization

Keyword injection

Maintaining professional tone

(Model may be upgraded later for better accuracy or performance.)

**🧠 How It Works (Architecture Overview)**

1️⃣ User Uploads Resume + Job Description

From the Next.js UI:

User uploads a .pdf, .docx, or .txt resume

User pastes the job description

A FormData POST request is sent to the Flask backend.

2️⃣ Backend Preprocessing

Flask:

Reads the uploaded file

Converts it to plain text using a custom parser

Cleans and formats the extracted text

If parsing fails, a helpful error is returned.

3️⃣ Resume Optimization via DeepSeek (LangChain + Ollama)

The backend generates a system + user prompt:

Matches keywords

Rewrites bullet points

Adds responsibilities relevant to the JD

Keeps resume one page

Keeps tone professional

Avoids fake information

Focuses on ATS-friendly structure

The rewritten resume is returned as clean text.

4️⃣ PDF Generation

The optimized text is converted into a downloadable PDF using FPDF:

Proper margins

Clean formatting

UTF-8 handling

Sent as a binary stream to the frontend

5️⃣ Frontend Display + Download

Next.js:

Shows the optimized resume

Shows download button

Handles error messaging

Smooth UI indicates loading & processing states

**✨ Current Features**

✔ Upload existing resume
✔ Paste job description
✔ Intelligent rewriting using DeepSeek LLM
✔ ATS-friendly resume generation
✔ Keyword optimization
✔ Clean, formatted PDF output
✔ UI/UX with validation and animations
✔ Fast local inference (no API cost)

**🔮 Upcoming Features**

🟦 Resume creation from scratch
Users enter:

Name

Experience

Skills

Projects

Education
…and the system builds a complete resume with layout templates.

🟩 Multiple templates (Modern, Minimal, Professional)

🟧 Support for cloud models
(e.g., GPT-4o, Claude, DeepSeek-API)

🟩 Resume similarity scoring
Using embeddings + cosine similarity measuring (already partially implemented).

🟪 Automatic missing-keyword detection

**👨‍💻 Author**

Sahran Khuwaja 🚀 Maching Learning Engineer | AI & Robotics Enthusiast | Full-Stack Developer | Data Scientist
