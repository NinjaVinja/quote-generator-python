# Quote Generator 💬

A simple desktop GUI app built with **Python (Tkinter)** that fetches and displays a random inspirational quote every time you click the button. Quotes are pulled live from the [ZenQuotes API](https://zenquotes.io/).

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)

## 🖼️ Preview

The app displays a quote card with a background image and a button — click the button to fetch a new random quote and author.

## ✨ Features

- Fetches random quotes in real-time from the ZenQuotes API
- Clean, minimal GUI built entirely with Tkinter
- Displays quote text along with the author's name
- Lightweight — no heavy dependencies

## 🛠️ Tech Stack

- **Python 3**
- **Tkinter** — for the GUI
- **Requests** — for API calls
- **ZenQuotes API** — quote data source

## 📂 Project Structure

```
quote-generator/
│
├── main.py            # Main application script
├── background.png     # Background image for the canvas
├── button.png          # Button image
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3 installed. Then install the required package:

```bash
pip install requests
```

### Run the App

1. Clone the repository:
   ```bash
   git clone https://github.com/NinjaVinja/quote-generator.git
   cd quote-generator
   ```
2. Make sure `background.png` and `button.png` are present in the project folder.
3. Run the script:
   ```bash
   python main.py
   ```

## 📌 How It Works

1. The app opens a window with a canvas showing a background image and placeholder text.
2. Clicking the button sends a `GET` request to the ZenQuotes API.
3. The response JSON is parsed to extract the quote and author.
4. The canvas text updates instantly with the new quote.

## 🙌 Author

**Muhammad Taha Ahmad** ([@NinjaVinja](https://github.com/NinjaVinja))
*Code Ninja by Night, Student by Day* 🥷

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
