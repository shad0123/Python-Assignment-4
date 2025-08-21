# Python-Assignment-4

This repository contains two Python scripts (`assignment4_task1.py` and `assignment4_task2.py`) that demonstrate file handling and exception handling in Python.

## Task 1: Read a File and Handle Errors

### Description:
The `assignment4_task1.py` script attempts to open and read a file named `sample.txt`. It uses a `try-except` block to handle potential `FileNotFoundError`. If the file is found, the script reads and prints the first two lines of its content. If the file is not found, an error message is displayed.

The `sample.txt` file contains the following content:
* This is a sample text file.
* It contains multiple lines.

### Assumptions:
* The script assumes the user wants to read the first two lines of the `sample.txt` file.

### Example Output (File Found):
```
Reading file content:
Line 1:  This is a sample text file.
Line 2:  It contains multiple lines.
```

### Example Output (File Not Found):
```
Error: The file 'sample.txt' was not found.
```

### How to Run:
1.  Open a terminal or command prompt.
2.  Navigate to the directory where the file is saved.
3.  Run the script using the following command:
    ```bash
    python assignment4_task1.py
    ```

---

## Task 2: Write and Append Data to a File

### Description:
The `assignment4_task2.py` script demonstrates various file operations. It prompts the user for text, writes it to a file named `output.txt`, then prompts the user for additional text and appends it to the same file. Finally, it reads and prints the entire content of the file.

### Assumptions:
* The user will input text strings when prompted.

### Example Output:
```
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling in Python.
```

### How to Run:
1.  Open a terminal or command prompt.
2.  Navigate to the directory where the file is saved.
3.  Run the script using the following command:
    ```bash
    python assignment4_task2.py
    ```
