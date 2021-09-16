FROM python:3.7-alpine3.9
COPY . /opt/
EXPOSE 8008
RUN apk add tzdata \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && cd /opt/ \
    && pip install -U setuptools \
    && pip install -r requirements.txt 

WORKDIR /opt/
CMD [ "python3", "-u", "run.py" ]
