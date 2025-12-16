# 📁 File Manager CLI

A **command-line file manager (CLI)** written in Python, focused on **best practices**, **clean code**, and **professional architecture**.

This project allows you to **list**, **create**, **rename**, and **remove** files and directories safely and efficiently directly from the terminal.

---

## 🚀 Features

- 📄 List files and directories
- ➕ Create files
- ✏️ Rename files or directories
- 🗑️ Remove files and empty directories
- ⚠️ Error handling and validations
- 🧠 Clear separation between **core logic** and **CLI interface**

---

## 🧰 Technologies Used

- **Python 3.10+**
- Standard library (`argparse`, `pathlib`)

> No external dependencies are required.

---

## 📦 Project Structure

```text
file-manager-cli/
├── file_manager.py      # Core logic (business rules)
├── cli.py               # Command-line interface
├── requirements.txt     # Project dependencies
└── README.md            # Documentation
```

---

## ⚙️ How to Use

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/file-manager-cli.git
cd file-manager-cli
```

### 2️⃣ Run commands

#### 📄 List files
```bash
python cli.py listar path/to/directory
```

#### ➕ Create a file
```bash
python cli.py criar path/to/directory filename.txt
```

#### ✏️ Rename a file
```bash
python cli.py renomear path/to/directory old_name.txt new_name.txt
```

#### 🗑️ Remove a file
```bash
python cli.py remover path/to/directory filename.txt
```

---

## 🛡️ Important Rules

- Directories are **only removed if they are empty**
- Existing files are never overwritten
- Clear success and error messages are returned

---

## 📌 Project Purpose

This project was developed for **educational purposes** and as a **portfolio project**, focusing on:

- Code organization
- Proper use of `argparse`
- File system manipulation with `pathlib`
- Patterns commonly used in real-world projects

---

## 📄 License

This project is licensed under the **MIT License**.

---

Developed with dedication by **Nic** 🚀

