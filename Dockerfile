FROM  alpine
RUN apk add --no-cache python3
CMD [ "pip install python3" ]
