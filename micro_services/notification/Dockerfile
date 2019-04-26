FROM alpine/git
WORKDIR /app
RUN git clone https://github.com/gunsnroses0/ElMenus-Notifications.git

FROM maven:3.5-jdk-8-alpine
WORKDIR /app
COPY --from=0 /app/ElMenus-Notifications /app
RUN mvn install
