# Payload Generator Project

A modular and extensible security payload generator designed to produce **XSS**, **SQL Injection**, and **encoded payloads** for testing web applications. The project includes a clean registry-based architecture, independent payload generators, and multiple encoding utilities.

---

## 🚀 Features

* **XSS Payload Generator**
* **SQL Injection Payload Generator**
* **Central Payload Registry**
* **Base64, URL, and HTML Encoders**
* **Easy-to-extend architecture**
* Organized & test‑friendly module structure

---

## 📂 Project Structure

```
payload-generator/
│
├── registry.py
├── generator_xss.py
├── generator_sqli.py
├── encoder.py
├── README.md
└── ... (future modules)
```

---

## 🧩 Modules Overview

### ✅ **registry.py**

Contains a global dictionary with all payload IDs and placeholder values.

### ✅ **generator_xss.py**

Lists available XSS payloads and returns payload by ID.

### ✅ **generator_sqli.py**

Lists SQL Injection payloads and returns payload by ID.

### ✅ **encoder.py**

Encodes payloads using Base64, URL encoding, or HTML escaping.

---

## 🛠 Usage Example

### List XSS Payloads

```python
from generator_xss import XSSGenerator
xss = XSSGenerator()
print(xss.list_ids())
```

### Generate a SQLi Payload

```python
from generator_sqli import SQLiGenerator
sqli = SQLiGenerator()
payload = sqli.generate_by_id("SQLI_UNION_001")
print(payload)
```

### Encode a Payload

```python
from encoder import Encoder
enc = Encoder()
print(enc.url_encode("A+B C&D"))
```

---

## 🔮 Future Enhancements

* Real payload signatures
* WAF bypass engines (XSS + SQLi)
* Payload fuzzing system
* PDF report generator
* Full menu-based CLI UI

---

## 🤝 Contributing

Pull requests are welcome! Suggestions for new payloads or modules are appreciated.

---

## 📜 License

This project is open-source. You may modify and extend it freely.
