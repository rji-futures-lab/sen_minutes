.PHONY: .env

env:
	echo 'DJANGO_SECRET_KEY=dev123' >> .env
	echo 'DATABASE_URL=psql://'`whoami`':@127.0.0.1:5432/senate' >> .env
	echo 'DEBUG=True' >> .env

syncdb:
	dropdb senate
	createdb senate
	rm -rf minutes_search/migrations
	python manage.py makemigrations minutes_search
	python manage.py migrate

createrds:
	aws --profile rji-futures-lab rds create-db-instance \
	--db-instance-identifier "senate-minutes" --db-name "senate" \
	--region "us-east-2" \
	--db-instance-class "db.t2.micro" --engine "postgres" \
	--master-username "postgres" --master-user-password ${DB_PASSWORD} \
	--allocated-storage 20 --vpc-security-group-ids "sg-0f98cf25206b5c515" \
	--tags Key='name',Value='senate-minutes'

	aws --profile rji-futures-lab rds wait db-instance-available \
	--region "us-east-2" \
	--db-instance-identifier "senate-minutes"

	aws --profile rji-futures-lab rds wait db-instance-available --region "us-east-2" --db-instance-identifier "senate-minutes"

	zappa manage dev migrate
	zappa manage dev loaddata

deleterds:
	aws --profile rji-futures-lab rds delete-db-instance \
	--db-instance-identifier "senate-minutes" --skip-final-snapshot \
	--delete-automated-backups

	aws --profile rji-futures-lab rds wait db-instance-deleted \
	--db-instance-identifier "senate-minutes"


recreaterds:
	make deleterds

	make createrds
