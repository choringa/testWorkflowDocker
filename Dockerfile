FROM alpine:latest
RUN apk update
RUN echo "hola2" > hola.txt
