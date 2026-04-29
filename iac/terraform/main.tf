terraform {
  required_providers {
    null = {
      source  = "hashicorp/null"
      version = "~> 3.2"
    }
  }
}

provider "null" {}

# Имитация сервера (как ресурс инфраструктуры)
resource "null_resource" "questplanner_server" {
  provisioner "local-exec" {
    command = "echo 'Provisioning QuestPlanner server...'"
  }
}

# Запуск деплоя через bash-скрипт
resource "null_resource" "deploy_app" {
  depends_on = [null_resource.questplanner_server]

  provisioner "local-exec" {
    command = "bash ~/scripts/deploy.sh"
  }
}
