FROM alpine/git
WORKDIR /db
RUN git clone https://github.com/AliWaleed97/psql-configuration.git

FROM postgres:latest
WORKDIR /db
COPY --from=0 /db/psql-configuration /db
# RUN cat tables.sql
RUN mv tables.sql /docker-entrypoint-initdb.d/
RUN mv procedures.sql /docker-entrypoint-initdb.d/