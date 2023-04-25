FROM postgres:13.4

ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=mydatabase

COPY init.sql /docker-entrypoint-initdb.d/
