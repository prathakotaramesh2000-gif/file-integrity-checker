# 🔐 File Integrity Checker

<p align="center">
  <strong>A Python-based cybersecurity tool to detect file modifications using SHA-256 hashing.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows&logoColor=white" alt="Windows">
  <img src="https://img.shields.io/badge/Editor-VS%20Code-007ACC?logo=visualstudiocode&logoColor=white" alt="VS Code">
  <img src="https://img.shields.io/badge/Security-File%20Integrity-red" alt="File Integrity">
  <img src="https://img.shields.io/badge/Level-Beginner-brightgreen" alt="Beginner">
</p>

## 📌 Project Overview

The **File Integrity Checker** is a beginner-friendly cybersecurity project developed using Python. It calculates the SHA-256 cryptographic hash of a file to help identify changes in its contents.

Every file produces a hash based on its contents. If the contents change, the resulting SHA-256 hash will normally change as well. By comparing a previously saved hash with a newly calculated hash, users can detect unexpected file modifications.

This project introduces important concepts used in digital forensics, file integrity monitoring, and cybersecurity investigations.

## 🎯 Project Objectives

- Calculate SHA-256 hashes for files.
- Detect changes by comparing file hashes.
- Understand cryptographic hashing fundamentals.
- Learn Python file handling and exception management.
- Explore basic digital forensics techniques.
- Develop practical cybersecurity skills using Windows and VS Code.

## ✨ Features

- 🔒 **SHA-256 Hash Generation** — Calculate a cryptographic hash for a selected file.
- 🔍 **File Change Detection** — Compare current hashes with previously stored baseline hashes.
- 📁 **File Handling** — Read files in binary mode for reliable hashing.
- ⚡ **Lightweight Application** — Uses Python's built-in libraries for core hashing functionality.
- 💻 **Windows Support** — Run the application through PowerShell or the VS Code terminal.
- 🛡️ **Digital Forensics Learning** — Understand how hashes support file integrity verification.

*Note: Automatic baseline saving and comparison require implementation in the application. The initial version may only calculate and display a hash.*

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| hashlib | SHA-256 hash calculation |
| pathlib | File path handling |
| Visual Studio Code | Code editing and debugging |
| Windows PowerShell | Running the application |
| Git and GitHub | Version control and project hosting |

## 📂 Project Structure

```text
File-Integrity-Checker/
│
├── main.py          # Main Python application
├── README.md        # Project documentation
└── .gitignore       # Files excluded from Git
```

## ⚙️ Installation and Setup

### Step 1: Install the prerequisites

Make sure you have:

- Windows 10 or Windows 11
- Python 3.10 or later
- Visual Studio Code
- Git (for GitHub operations)

### Step 2: Clone the repository

Open PowerShell or the VS Code terminal:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository HTTPS URL.

### Step 3: Open the project folder

```bash
cd File-Integrity-Checker
code .
```

If the cloned folder has a different name, use its actual name.

### Step 4: Verify Python

```bash
python --version
```

### Step 5: Run the application

```bash
python main.py
```

Enter the path of the file you want to check when prompted.

For example:

```text
C:\Users\YourUserName\Desktop\sample.txt
```

The application displays the SHA-256 hash of the selected file.

## 🧪 How to Test the Project

1. Create a text file named `sample.txt`.
2. Add some text and save the file.
3. Run the application and calculate its SHA-256 hash.
4. Save the displayed hash as your original reference.
5. Modify the contents of `sample.txt`.
6. Run the application again.
7. Compare the new hash with the original hash.

**Expected result:** If the file contents have changed, the SHA-256 hashes should differ, allowing you to identify a modification.

## 🔐 Understanding SHA
