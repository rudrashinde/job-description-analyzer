# Job Description Analyzer (CLI)

A simple Python command-line tool that compares a resume with a job description and calculates a keyword match percentage based on overlapping keywords.

This project was built as part of my journey to strengthen Python fundamentals and move from learning concepts to building practical tools.

---

## Features

- Reads resume and job description from text files
- Extracts keywords using basic text processing
- Calculates keyword match percentage
- Displays missing keywords from the job description
- Handles empty job descriptions safely (no crashes)

---

## Tech Stack

- Python
- File Handling
- String Processing
- Set Operations
- Basic CLI Interaction

---

## Project Structure

```
job-analyzer/
│
├── job_analyzer.py
├── resume.txt
├── job.txt
└── README.md
```

---

## How to Run

1. Make sure Python is installed.
2. Open terminal inside the project folder.
3. Run:

```bash
python job_analyzer.py
```

4. Enter:
   - Resume file path (example: `resume.txt`)
   - Job description file path (example: `job.txt`)

---

## Example Output

```
==============================
Match Score: 50.00%
==============================

Missing Keywords:
- aws
- docker
- communication
```

---

## Learning Goals

This project focuses on:

- Writing modular Python functions
- Understanding file paths and debugging
- Using sets for efficient keyword comparison
- Building complete, runnable CLI tools

---

## Future Improvements (V2 Ideas)

- Remove common stopwords (like "and", "the", etc.)
- Improve keyword extraction logic
- Add basic NLP processing
- Integrate OpenAI API for resume improvement suggestions
- Build a web interface version

---

## Author

Built as part of my AI & software engineering learning journey.