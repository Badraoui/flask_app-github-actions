FROM datamechanics/spark:3.1-latest
ENV PYSPARK_MAJOR_PYTHON_VERSION=3
WORKDIR /opt/application/
COPY requirements.txt .
RUN pip3 install -r requirements.txt 

COPY *.py ./
COPY *.yml ./
COPY *.md ./
COPY src/rest_api.py ./


RUN cd src
RUN python rest_api.py
