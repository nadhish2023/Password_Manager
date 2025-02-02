# Password Manager

## Overview
The **Password Manager** is a simple and efficient tool built using Python and Tkinter to help users generate, store, and manage their passwords securely. It ensures that users can generate strong passwords and save them in a structured format.

## Features
- **Random Password Generation**: Creates secure passwords using a mix of uppercase, lowercase, numbers, and special characters.
- **Save Credentials**: Stores website, username, and password in a text file (`password.txt`).
- **Clipboard Support**: Automatically copies the generated password to the clipboard for easy pasting.
- **User Confirmation**: Asks for confirmation before saving credentials to prevent accidental entries.
- **Graphical User Interface (GUI)**: Built using Tkinter for an intuitive user experience.

## Installation

### Prerequisites
Ensure you have Python installed. You can download it from [Python's official website](https://www.python.org/downloads/).

### Steps
```bash
# Clone the repository
git clone https://github.com/your-username/password-manager.git
cd password-manager

# Install dependencies (if needed)
pip install tk

# Run the application
python main.py
```

## Usage
1. Enter the **Website** and **Username**.
2. Click **Generate** to create a strong password.
3. Click **Add** to save the credentials in `password.txt`.
4. The password is automatically copied to the clipboard.

## File Structure
```plaintext
password-manager/
│── main.py       # Main program
│── logo.png      # App logo
│── password.txt  # Stored passwords (auto-created)
│── README.md     # Project documentation
```

## Screenshot
![image](https://github.com/user-attachments/assets/111bbade-f596-4906-ae1a-5a60bf1dedef)

---
Feel free to contribute and improve the project!
```
