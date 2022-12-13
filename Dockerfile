FROM python:latest
LABEL Maintainer="roushan.me17"
WORKDIR /usr/app/src
COPY ./ ./
RUN pip install -r ./requirement.txt
CMD [ "python", "./kubebot.py"]