# 📁 File Manager CLI
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Project Type](https://img.shields.io/badge/project-CLI-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

A **command-line file manager (CLI)** written in Python, focused on **best practices**, **clean code**, and **professional architecture**.

This project allows you to **list**, **create**, **rename**, and **remove** files and directories safely and efficiently directly from the terminal.

---

## 🚀 Features

* 📄 List files and directories
* ➕ Create files
* ✏️ Rename files or directories
* 🗑️ Remove files and empty directories
* ⚠️ Error handling and validations
* 🧠 Clear separation between **core logic** and **CLI interface**

---

## 🧰 Technologies Used

* **Python 3.10+**
* Standard library (`argparse`, `pathlib`)

> No external dependencies are required.

---

## 📦 Project Structure

````text
file-manager-cli/
├── file_manager.py      # Core logic (business rules)
├── cli.py               # Command-line interface
├── requirements.txt     # Project dependencies
└── README.md            # Documentation
```text
file-manager-cli/
├── file_manager.py      # Core logic (business rules)
├── cli.py               # Command-line interface
├── requirements.txt     # Project dependencies
└── README.md            # Documentation
````

---

## ⚙️ How to Use

### 1️⃣ Clone the repository

```bash
git clone https://github.com/nicgualberto/file-manager-cli.git
cd file-manager-cli
```

### 2️⃣ Run commands

#### 📄 List files

```bash
python cli.py list path/to/directory
```

#### ➕ Create a file

```bash
python cli.py create path/to/directory filename.txt
```

#### ✏️ Rename a file

```bash
python cli.py rename path/to/directory old_name.txt new_name.txt
```

#### 🗑️ Remove a file or empty directory

```bash
python cli.py remove path/to/directory filename_or_directory
```

bash
git clone [https://github.com/nicgualberto/file-manager-cli.git](https://github.com/nicgualberto/file-manager-cli.git)
cd file-manager-cli

## 🧪 Example Usage

  ```bash
    $ python cli.py list .
    Documents
    example.txt
    
    $ python cli.py create . test.txt
    File "test.txt" created successfully.
    
    $ python cli.py rename . test.txt demo.txt
    "test.txt" renamed to "demo.txt".
    
    $ python cli.py remove . demo.txt
    File "demo.txt" removed successfully.
  ```
---

## 🛡️ Important Rules

* Directories are **only removed if they are empty**
* Existing files are never overwritten
* Clear success and error messages are returned

---

## 📌 Project Purpose

This project was developed for **educational purposes** and as a **portfolio project**, focusing on:

* Code organization
* Proper use of `argparse`
* File system manipulation with `pathlib`
* Patterns commonly used in real-world projects

---

## 📄 License

This project is licensed under the **MIT License**.

---

Developed with dedication by **Nic** 🚀
