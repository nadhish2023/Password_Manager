# Password Manager

## Overview
This is an advanced Password Manager built using Python and Tkinter. It allows users to generate, store, and retrieve passwords securely using a JSON-based database.

## Features
- **Password Generation:** Generates strong passwords containing uppercase letters, lowercase letters, numbers, and special characters.
- **Clipboard Copy:** Automatically copies the generated password to the clipboard.
- **Password Storage:** Saves passwords securely in `data.json`.
- **Password Retrieval:** Allows users to search for saved credentials.
- **User-friendly UI:** Built with Tkinter for an easy-to-use interface.

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
1. Enter the **Website** and **Username** in the respective fields.
2. Click **Generate** to create a strong password.
3. Click **Add** to save the credentials to `data.json`.
4. Use **Search** to retrieve saved credentials.
5. The password will be copied to the clipboard automatically.

## File Structure
```plaintext
password-manager/
├── main.py        # Main application file
├── logo.png       # Logo image for the UI
├── data.json      # Stores saved passwords
├── README.md      # Documentation
```

## Screenshot
![image](https://github.com/user-attachments/assets/111bbade-f596-4906-ae1a-5a60bf1dedef)

---
Feel free to contribute and improve the project!
```
