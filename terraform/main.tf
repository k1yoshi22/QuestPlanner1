terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_network" "quest_network" {
  name = "questplanner_terraform_network"
}

resource "docker_volume" "postgres_data" {
  name = "questplanner_terraform_postgres_data"
}

resource "docker_image" "postgres" {
  name = "postgres:15"
}

resource "docker_container" "postgres" {
  name  = "quest_terraform_postgres"
  image = docker_image.postgres.image_id

  env = [
    "POSTGRES_USER=quest_user",
    "POSTGRES_PASSWORD=quest_pass",
    "POSTGRES_DB=quest_db"
  ]

  ports {
    internal = 5432
    external = 5433
  }

  volumes {
    volume_name    = docker_volume.postgres_data.name
    container_path = "/var/lib/postgresql/data"
  }

  networks_advanced {
    name = docker_network.quest_network.name
  }
}

resource "docker_image" "nginx" {
  name = "nginx:latest"
}

resource "docker_container" "nginx" {
  name  = "quest_terraform_nginx"
  image = docker_image.nginx.image_id

  ports {
    internal = 80
    external = 8088
  }

  networks_advanced {
    name = docker_network.quest_network.name
  }
}
