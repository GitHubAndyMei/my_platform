build-db:
	@docker-compose -f docker-compose-db.yml build

up-db:
	@docker-compose -f docker-compose-db.yml up -d

down-db:
	@docker-compose -f docker-compose-db.yml down

restart-db:
	@docker-compose -f docker-compose-db.yml restart