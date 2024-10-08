FROM python:3

# install dependencies
RUN apt-get update 
RUN apt-get upgrade -y 
RUN apt-get install curl libgconf-2-4 libatk1.0-0 libatk-bridge2.0-0 libgdk-pixbuf2.0-0 libgtk-3-0 libgbm-dev libnss3-dev libxss-dev libasound2 -y
RUN apt-get update
RUN rm -rf /var/lib/apt/lists/*

# create ctf user and directory
RUN mkdir /ctf
WORKDIR /ctf
RUN useradd -M -d /ctf ctf

# copy files
COPY server.py /ctf/server.py
COPY start.sh /ctf/start.sh
COPY secret_key.txt /ctf/secret_key.txt
COPY local.db /ctf/local.db
COPY templates /ctf/templates

# set permissions
RUN chown -R root:ctf /ctf 
RUN chmod -R 750 /ctf

# install flask and nodejs dependencies
RUN pip3 install flask

CMD ["bash", "/ctf/start.sh"]

EXPOSE 1234