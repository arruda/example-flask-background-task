FROM python:3.6

ADD ./requirements.txt /project/requirements.txt
WORKDIR /project
RUN pip install -r requirements.txt
ADD ./ /project