FROM alpine:latest
RUN apk update
RUN echo "hola" > hola.txt
