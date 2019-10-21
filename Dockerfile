FROM python:3.6

ADD ./requirements.txt /project/requirements.txt
ADD ./setup.py /project/setup.py
WORKDIR /project
RUN mkdir example && \
    touch example/__init__.py
RUN pip install -r requirements.txt
ADD ./ /project