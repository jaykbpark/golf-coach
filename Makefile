COMPOSE_FILE := docker-compose.yml

.PHONY: infra-up infra-down infra-logs infra-ps

infra-up:
	docker compose -f $(COMPOSE_FILE) up -d

infra-down:
	docker compose -f $(COMPOSE_FILE) down

infra-logs:
	docker compose -f $(COMPOSE_FILE) logs -f

infra-ps:
	docker compose -f $(COMPOSE_FILE) ps
