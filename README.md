# 🔐 Password Generator Tool

A simple but powerful Python script that generates customized password lists based on user input — useful for ethical hacking, penetration testing, OSINT investigations, or CTF practice.

## 📌 Features

- 💡 Accepts user-defined keywords (e.g., names, dates, numbers, symbols)
- 🔁 Creates permutations and combinations
- 🔄 Adds reversed variations of passwords
- 📝 Exports the entire list to `passwords.txt`
- 🎨 Fancy terminal header with `pyfiglet`


## 🧰 Requirements

- Python 3.x
- `pyfiglet` module

Install `pyfiglet` using pip:

```bash
pip install pyfiglet
```

---

## 🚀 Usage

Run the script:

```bash
python Pass_Generator.py
```

You will be prompted to enter keywords such as:

```
Enter all known information (names, dates, numbers, symbols) separated by spaces:
```

Example input:

```
john 1995 ! soccer
```

The script will generate combinations like:

```
john1995
!soccer
soccerjohn!
john!1995
...
```

All results are saved automatically to a file named:

```
passwords.txt
```


## 📁 Output

- `passwords.txt`: Contains all the generated password combinations (duplicates removed).

## ⚠️ Disclaimer

> This tool is intended **only for educational and ethical testing purposes**.  
> Do not use it to attempt unauthorized access to systems or accounts.  
> **Always respect the privacy and security of others.**

---

## 👨‍💻 Author

**MO KHALED**  
