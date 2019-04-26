FROM alpine/git
WORKDIR /app
RUN git clone https://github.com/gunsnroses0/ElMenus-Favorites.git

FROM maven:3.5-jdk-8-alpine
WORKDIR /app
COPY --from=0 /app/ElMenus-Favorites /app
RUN mvn install
