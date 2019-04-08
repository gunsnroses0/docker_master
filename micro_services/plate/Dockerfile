FROM alpine/git
WORKDIR /app
RUN git clone https://github.com/gunsnroses0/ElMenus-Plates.git

FROM maven:3.6.0-jdk-11
WORKDIR /app
COPY --from=0 /app/ElMenus-Plates /app
RUN mvn install
