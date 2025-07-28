# 📈 Stock Alert App

Get instant SMS alerts when a company's stock price changes significantly, along with the top 3 latest news articles.  
Built using **Python**, **Alpha Vantage**, **NewsAPI**, and **Twilio**.

---

## 🚀 Features

- 📊 Tracks stock price difference (%)
- 📰 Fetches top 3 latest news related to the company
- 📱 Sends SMS alert using Twilio
- ✅ Clean & modular code with error handling
- 📂 Environment variables secured with `.env` file

---

## 📦 Tech Stack

- **Python**
- **Alpha Vantage API**
- **NewsAPI**
- **Twilio API**
- **dotenv** (to manage API keys securely)
- **requests** (for API calls)

---

## 🧠 How It Works

1. Fetches daily stock data for `TSLA (Tesla)`
2. Checks the % difference between yesterday & day-before-yesterday
3. If difference > 1%, fetches 3 latest news headlines
4. Sends nicely formatted SMS to your phone

---

## 📁 Project Structure

📦 Stock-Alert-App
┣ 📄 stock_alert.py
┣ 📄 .env (not uploaded to GitHub)
┣ 📄 .gitignore


## 🔐 .env File Format
ALPHA_VANTAGE_API_KEY=your_alpha_key
NEWS_API_KEY=your_newsapi_key
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE_NUMBER=+1234567890
YOUR_PHONE_NUMBER=+919999999999

## 🔗 Connect With Me

Made with 💙 by Harshit Pundir  
📧 harshitpundir36@example.com  
🌐 [LinkedIn](https://www.linkedin.com/in/harshit-pundir-a5b112332/)  
🔗 [More Projects](https://github.com/Harshit-pundir)