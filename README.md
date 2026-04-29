# 🚀 QuestPlanner

AI-планировщик задач с Telegram-ботом и DevOps инфраструктурой.

---

## ⚡ Features

- 🤖 AI ответы (OpenAI)
- 📱 Telegram бот
- ⚙️ FastAPI backend
- 🐳 Docker (multi-container)
- 🔁 Jenkins CI/CD
- 📊 Monitoring (Prometheus + Grafana)
- ☁️ Terraform (IaC)

---

## 🧠 AI Planner

Система помогает пользователю составлять планы, ставить цели и структурировать задачи с помощью искусственного интеллекта.

---

## 📷 Preview

### 🤖 Telegram Bot

<p align="center">
  <img src="screenshots/telegram.png" width="500"/>
</p>

---

### ⚙️ API (Swagger)

<p align="center">
  <img src="screenshots/swagger.png" width="700"/>
</p>

---

## 🏗 Architecture

<p align="center">

Client → Nginx → FastAPI → PostgreSQL  
Monitoring → Prometheus → Grafana  
CI/CD → Jenkins  
AI → OpenAI + Telegram Bot  

</p>

---

## 🤖 Telegram Bot

Бот позволяет:

- 📅 составлять планы (день / неделя / месяц)
- 🎯 ставить цели
- 🧠 получать AI-рекомендации

---

## ⚙️ API (Swagger)

Документация доступна по адресу:

👉 http://YOUR_IP:8000/docs  

> ⚠️ Замените `YOUR_IP` на адрес вашего сервера  
> или используйте `localhost`

---

## 🚀 Run

```bash
docker compose up -d --build
