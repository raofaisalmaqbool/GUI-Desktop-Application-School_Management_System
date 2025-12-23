# School Management System (Tkinter Desktop App)

A simple **School Management System** desktop application built with **Python Tkinter** and **MySQL**. It lets you manage:

- Courses (name, duration, charges, description)
- Students (basic profile, roll number, contact details)

The UI is a single-window dashboard (`dashboard.py`) that opens course and student management windows.

---

## Tech Stack

- **Python 3.x**
- **Tkinter** (standard GUI library in Python)
- **MySQL** (data storage)
- **PyMySQL** (MySQL connector)
- **Pillow** (image handling for the dashboard)
- **python-dotenv** (loads configuration from `.env`)

---

## Project Structure

```text
GUI-Desktop-Application-School_Management_System/
├── dashboard.py          # Main dashboard window (entry to the app UI)
├── courses.py            # Manage Course CRUD UI
├── student.py            # Manage Student CRUD UI
├── project_db.py         # Database helper functions (courses + students)
├── config.py             # Configuration & .env loading (DB + image paths)
├── main.py               # Recommended entry point to start the app
├── img/                  # Static image assets (logo + main image)
│   ├── logo-small.png
│   ├── img1.png
│   └── img2.png
├── .env                  # Local environment configuration (DB settings)
├── requirements.txt      # Python dependencies
└── README.md             # This documentation
```

> Note: This is a **desktop** application – there are no HTML templates or CSS files. Visual styling is handled directly via Tkinter widget options and the images in the `img/` directory.

---

## Setup Instructions

### 1. Prerequisites

- Python 3.8+ installed
- MySQL server installed and running
- A MySQL user that can create databases and tables

### 2. Create and activate a virtual environment (optional but recommended)

```bash
cd GUI-Desktop-Application-School_Management_System
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database via `.env`

Edit the `.env` file in the project root:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password_here
DB_NAME=project_lms
```

These values are loaded by `config.py` using `python-dotenv` and used by `project_db.py` when connecting to MySQL.

### 5. Create the database and tables

Log into MySQL and run the following SQL (adjust names/types as needed):

```sql
CREATE DATABASE IF NOT EXISTS project_lms;
USE project_lms;

-- Course table
CREATE TABLE IF NOT EXISTS course (
    cid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    duration VARCHAR(255),
    charges VARCHAR(255),
    description TEXT
);

-- Student table
CREATE TABLE IF NOT EXISTS student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roll_no VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    gender VARCHAR(20),
    state VARCHAR(255),
    address TEXT
);
```

The Python helpers in `project_db.py` (`insert_data`, `fetch_tabel_data`, `insert_student`, etc.) assume this schema.

---

## Running the Application

The recommended entry point is `main.py`:

```bash
python main.py
```

Alternatively, you can run the dashboard module directly:

```bash
python dashboard.py
```

Both ways will open the main window with buttons to manage Courses and Students.

---

## Environment & Configuration

- All DB connection details are centralized in `config.py`.
- `config.py` reads variables from `.env`:
  - `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`
- If `.env` is missing, sensible defaults are used (`localhost`, `root`, empty password, `project_lms`).
- Image paths (`img/logo-small.png`, `img/img2.png`) are also built in `config.py` and used from there in `dashboard.py`.

This makes the project easier to configure and move between environments (dev, test, prod).

---

## Notes on Code & Logic

- **Courses**
  - `courses.py` uses helpers in `project_db.py` (`insert_data`, `fetch_tabel_data`, `fetch_tabel_data_one`, `update_data`, `delete_record`, `search_data`).
  - The DB helpers now use parameterized queries and a reusable connection function.

- **Students**
  - `student.py` has been refactored to talk to dedicated helpers in `project_db.py` (`insert_student`, `fetch_all_students`, `fetch_student_by_roll`, `update_student`, `delete_student`, `search_students`).
  - The student table shown in the UI matches the `student` schema (ID, roll no, name, email, gender, state, address).

- **Images / Static Assets**
  - All images live under `img/`.
  - `dashboard.py` imports paths from `config.py`, avoiding hardcoded string paths.

---

## Troubleshooting

- **Cannot connect to MySQL**
  - Check that MySQL is running and credentials in `.env` are correct.
  - Verify you can connect manually with the same user/password.

- **Tables do not exist**
  - Ensure you have run the SQL in the *Create the database and tables* section.

- **Images not loading**
  - Make sure `img/logo-small.png` and `img/img2.png` exist.
  - Confirm you are running the app from the project root so relative paths resolve correctly.

---

## Future Improvements

Possible next steps to extend or further professionalize this project:

- Add more student fields (DOB, contact, course assignment) and link them to proper DB columns.
- Add teacher and results management screens.
- Package the app into an executable (e.g. with PyInstaller) for distribution.
- Add automated tests around the DB helpers.
