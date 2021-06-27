FROM postgres:latest
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_USER=username
ENV POSTGRES_DB=warung_pintar_db
COPY warung_pintar_db.pgsql /docker-entrypoint-initdb.d/warung_pintar_db.pgsql
