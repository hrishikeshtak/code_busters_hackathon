FROM ubuntu:22.04

# Install Python 3.10
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y python3.10 python3-pip

# Update symlink to point to latest
RUN rm /usr/bin/python3 && ln -s /usr/bin/python3.10 /usr/bin/python3
RUN python3 --version
RUN pip3 --version

ENV PROJECT_DIR=/opt/code_busters_hackathon
RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR


COPY main.py $PROJECT_DIR/
COPY run-api.py $PROJECT_DIR/
COPY routes.py $PROJECT_DIR/
COPY src $PROJECT_DIR/src
COPY requirements.txt $PROJECT_DIR/
COPY entrypoint.sh $PROJECT_DIR/

RUN pip install --upgrade pip \
 && pip install wheel \
 && pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["./entrypoint.sh"]
