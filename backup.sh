#!/bin/bash

DATE=$(date +%F_%H-%M)

docker exec questplanner-postgres-1 pg_dump -U quest_user quest_db > backups/backup_$DATE.sql

echo "Backup created: backup_$DATE.sql"
