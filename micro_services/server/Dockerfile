# FROM alpine/git
# WORKDIR /app
# RUN git clone https://github.com/gunsnroses0/ElMenus-Server.git

# FROM maven:3.6.0-jdk-11 AS build 
# WORKDIR /app
# COPY --from=0 /app/ElMenus-Server /app 
# RUN mvn -f /app/pom.xml clean package



# FROM gcr.io/distroless/java  
# COPY --from=build /app/target/Server-2.0.1-SNAPSHOT-jar-with-dependencies.jar /app/Server-2.0.1-SNAPSHOT-jar-with-dependencies.jar  
# EXPOSE 8080  
# ENTRYPOINT ["java","-jar","/app/Server-2.0.1-SNAPSHOT-jar-with-dependencies.jar"]
FROM alpine/git
WORKDIR /app
RUN git clone https://github.com/gunsnroses0/ElMenus-Server.git

FROM maven:3.5-jdk-8-alpine
WORKDIR /app
COPY --from=0 /app/ElMenus-Server /app
RUN mvn install