# Linux Commands Documentation

## 1. pwd

**Command Used**
```bash
pwd
```

**Purpose**
Displays the current working directory.

**Output Observed**
```text
/c/Users/nehab/Synergy_TP
```

---

## 2. ls

**Command Used**
```bash
ls
```

**Purpose**
Lists files and folders in the current directory.

**Output Observed**
```text
README.md  task_1  task_2
```

---

## 3. ls -la

**Command Used**
```bash
ls -la
```

**Purpose**
Displays all files including hidden files with detailed information.

**Output Observed**
```text
drwxr-xr-x task_1
drwxr-xr-x task_2
-rw-r--r-- README.md
```

---

## 4. cd

**Command Used**
```bash
cd task_1
```

**Purpose**
Changes the current directory to task_1.

**Output Observed**
```text
/c/Users/nehab/Synergy_TP/task_1
```

---

## 5. mkdir

**Command Used**
```bash
mkdir test_folder
```

**Purpose**
Creates a new directory.

**Output Observed**
```text
test_folder
```

---

## 6. touch

**Command Used**
```bash
touch sample_test.txt
```

**Purpose**
Creates an empty file.

**Output Observed**
```text
sample_test.txt
```

---

## 7. cat

**Command Used**
```bash
cat sample_test.txt
```

**Purpose**
Displays the contents of a file.

**Output Observed**
```text
Hello World
```

---

## 8. echo

**Command Used**
```bash
echo Hello Synergy
```

**Purpose**
Prints text to the terminal.

**Output Observed**
```text
Hello Synergy
```

---

## 9. cp

**Command Used**
```bash
cp sample_test.txt backup.txt
```

**Purpose**
Creates a copy of a file.

**Output Observed**
```text
backup.txt
```

---

## 10. mv

**Command Used**
```bash
mv backup.txt renamed.txt
```

**Purpose**
Renames or moves a file.

**Output Observed**
```text
renamed.txt
```

---

## 11. rm

**Command Used**
```bash
rm renamed.txt
```

**Purpose**
Removes a file.

**Output Observed**
```text
File deleted successfully
```

---

## 12. grep

**Command Used**
```bash
grep Hello sample_test.txt
```

**Purpose**
Searches for a specific word or pattern in a file.

**Output Observed**
```text
Hello World
```

---

## 13. find

**Command Used**
```bash
find . -name "*.py"
```

**Purpose**
Searches for files matching a given pattern.

**Output Observed**
```text
./task_1/src/hello.py
```

---

## 14. head

**Command Used**
```bash
head sample_test.txt
```

**Purpose**
Displays the first few lines of a file.

**Output Observed**
```text
Hello World
```

---

## 15. tail

**Command Used**
```bash
tail sample_test.txt
```

**Purpose**
Displays the last few lines of a file.

**Output Observed**
```text
Hello World
```

---

## 16. wc

**Command Used**
```bash
wc sample_test.txt
```

**Purpose**
Counts lines, words, and characters in a file.

**Output Observed**
```text
1 2 12 sample_test.txt
```

---

## 17. chmod

**Command Used**
```bash
chmod +x sample_test.txt
```

**Purpose**
Changes file permissions.

**Output Observed**
```No output is also ok.
```