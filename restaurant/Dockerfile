FROM alpine/git
WORKDIR /app
RUN git clone https://github.com/gunsnroses0/ElMenus-Restaurants.git

FROM maven:3.6.0-jdk-11
WORKDIR /app
COPY --from=0 /app/ElMenus-Restaurants /app
RUN pwd
RUN mvn install
