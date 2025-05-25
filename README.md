# 🌐 ExtractionTool

A simple Python-based web content extractor that allows you to download and save the HTML source of any website to a local file.

---

## 📋 Description

**ExtractionTool** prompts the user to:

1. Enter a file name.
2. Provide a website URL.

It then fetches the page content using `requests` and saves it as an HTML/text file.

---

## ⚙️ Features

- Download and save the full HTML content of any website.
- Automatically names the saved file as per user input.
- UTF-8 encoding to support international characters.
- Basic status code check for successful fetch.

---

## 🧰 Requirements

- Python 3.x
- `requests` module  
  → Install via pip if not already installed:

```bash
pip install requests
```

---

## 🚀 How to Use

1. Run the script:

```bash
python extraction_tool.py
```

2. Follow the prompts:

```
How you want to call your file: mypage.html
Paste the website url here: https://example.com
```

3. If the site is reachable, the HTML will be saved into `mypage.html`.

---

## 📂 Output

Example of a saved file:

```
mypage.html
└── Contains raw HTML source from https://example.com
```

---

## 🛑 Error Handling

- If the website is unreachable or returns a non-200 status code, you'll see an error message with the status.

---

## ✅ Example

```
How you want to call your file: blog.html
Paste the website url here: https://myblogsite.com

Le contenu du site a été sauvegardé dans le fichier blog.html.
```

---

## 🔒 Disclaimer

This tool is intended for educational and ethical use only. Always ensure you have permission to download and store content from the target site.

---

## 📄 License

Free to use and modify for personal or academic projects.
