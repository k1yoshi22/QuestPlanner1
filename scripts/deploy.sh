#!/bin/bash

echo "🚀 Deploying QuestPlanner..."

# запуск docker проекта
sudo docker compose up -d --build

# перезапуск nginx
sudo systemctl restart nginx

echo "✅ Deployment finished!"
