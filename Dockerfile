FROM alpine:latest
RUN apk update
RUN echo "hola nea" > hola.txt
