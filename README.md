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
> или используйте `localhost` при локальном запуске

---

## 🚀 Run

```bash
docker compose up -d --build
