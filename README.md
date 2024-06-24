# Password Generator
A Python-based Password Generator using Tkinter for the GUI. Generate strong, customizable passwords with options for uppercase letters, lowercase letters, digits, and symbols. Features include copying passwords to the clipboard and maintaining a history of generated passwords. Easy-to-use interface for enhanced password security.

## Features

- Generate passwords of varying lengths (8 to 32 characters).
- Include/exclude uppercase letters, lowercase letters, digits, and symbols.
- Copy generated passwords to the clipboard.
- View and manage a history of generated passwords.
- Clear the password history.

## Requirements

- Python 3.x
- Tkinter library

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/harpalmodasiya/Password-Generator-in-Python.git

2. Navigate to the project directory:
   ```sh
   cd Password-Generator-in-Python

3. Run the application:
   ```sh
   python PassGen.py

## Usage

1.Open the application.
2.Select the desired length of the password using the scale.
3.Choose the character sets to include (uppercase, lowercase, digits, symbols) by checking the corresponding boxes.
4.Click the "Generate Password" button to generate a password.
5.The generated password will be displayed in the password history listbox.
6.To copy a password to the clipboard, select it from the listbox and click the "Copy Password" button.
7.To clear the password history, click the "Clear History" button.

## Code Overview

-generate_password: Function to generate a password based on user-selected options.
-copy_password: Function to copy the selected password from the history listbox to the clipboard.
-clear_history: Function to clear the password history.
-The main window is created and configured with Tkinter, including labels, scales, checkboxes, buttons, and listbox.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Sample Screenshot

<img width="587" alt="PassGen" src="https://github.com/harpalmodasiya/Password-Generator-in-Python/assets/171497968/f78cfef2-6969-457f-a863-c559df4738dd">
