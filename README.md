# 🎓 Autonomous Student Life AI Agent (OpenClaw + Groq)

An **autonomous AI-powered student assistant** that proactively monitors assignments, detects urgent deadlines, and sends real-time notifications via Telegram.

This project demonstrates a **real-world AI agent architecture** combining:

* 🧠 LLM reasoning (Groq Llama-3)
* ⚙️ Tool-based execution
* 🔌 OpenClaw integration (execution layer)
* ⏰ Autonomous scheduling
* 📩 Telegram notifications

---

## 🚀 Features

* 📚 **Assignment Monitoring**

  * Tracks academic tasks and deadlines

* ⚠️ **Urgency Detection**

  * Identifies assignments due soon using intelligent logic

* 🧠 **AI Decision-Making**

  * Uses LLM to decide which tools to use dynamically

* 🔄 **Autonomous Execution**

  * Runs automatically on a schedule (no user input required)

* 📩 **Telegram Notifications**

  * Sends daily updates directly to the user

* 🔌 **OpenClaw Integration**

  * Used as the execution layer for agent actions

---

## 🧠 System Architecture

```
Scheduler
   ↓
AI Agent (LLM + Rules)
   ↓
OpenClaw (Execution Layer)
   ↓
Tools (Assignments, Risk Detection)
   ↓
LLM (Final Response Generation)
   ↓
Telegram Notification
```

---

## ⚙️ Tech Stack

* **Python 3.11**
* **FastAPI** – Backend API
* **Groq API (Llama-3)** – LLM reasoning
* **OpenClaw** – Execution layer
* **Schedule** – Task automation
* **Telegram Bot API** – Notifications
* **WSL (Ubuntu)** – Development environment

---

## 📁 Project Structure

```
student-life-agent/
│
├── agents/
│   ├── student_agent.py
│   ├── tools_registry.py
│   └── openclaw_wrapper.py
│
├── tools/
│   ├── classroom_tool.py
│   └── risk_detector_tool.py
│
├── scheduler/
│   └── daily_runner.py
│
├── telegram_utils/
│   └── send_message.py
│
├── llm/
│   └── groq_client.py
│
├── api/
│   └── server.py
│
├── config/
│
├── prompts/
│
├── .env
├── requirements.txt
└── README.md
```

---

## 🔧 Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd student-life-agent
```

---

### 2️⃣ Create Environment

Using Conda:

```bash
conda create -n student_agent_env python=3.11
conda activate student_agent_env
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
TELEGRAM_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

---

### 5️⃣ Run FastAPI Server

```bash
uvicorn api.server:app --reload
```

Access API docs:

```
http://127.0.0.1:8000/docs
```

---

### 6️⃣ Run Autonomous Agent

```bash
python -m scheduler.daily_runner
```

---

## 🧪 Example Output

### Telegram Notification

```
📚 Daily Academic Update

⚠️ URGENT TASKS:
- ML Report is due very soon!
- Dependency Parsing Lab is due very soon!
```

---

## 🔌 OpenClaw Integration

OpenClaw is used as the **execution layer** of the agent.

* AI decides *what to do*
* OpenClaw executes the action
* Results are passed back to the LLM

> Note: A simulated wrapper is used since OpenClaw requires a configured transport layer for full execution.

---

## 🧠 Key Concepts Demonstrated

* AI Agent Design (Think → Act → Respond)
* Tool Calling Architecture
* Hybrid Intelligence (LLM + Rule-based logic)
* Autonomous Systems (Scheduled execution)
* Real-world AI Integration (Telegram + APIs)

---

## 📌 Future Improvements

* 📧 Gmail integration (auto-detect assignments)
* 📅 Google Calendar scheduling
* 🧠 Memory system (track progress over time)
* 🌐 Web dashboard (Streamlit or React)
* 🔍 Real-time data scraping via OpenClaw

---

## 💼 Resume Description

> Built an autonomous AI student assistant using FastAPI, Groq Llama-3, and OpenClaw that proactively monitors assignments, detects urgent deadlines, and sends real-time notifications via Telegram.

---

## 🎯 Demo Script (Quick Pitch)

* "This is an autonomous AI agent, not just a chatbot."
* "It runs on a schedule and proactively checks academic tasks."
* "It uses LLM reasoning to decide actions and OpenClaw to execute them."
* "It then sends real-time updates via Telegram."

---

## 🏆 Why This Project Stands Out

* Goes beyond basic chatbots
* Demonstrates real AI agent architecture
* Combines automation + intelligence
* Shows practical real-world use case

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Shivam

---
