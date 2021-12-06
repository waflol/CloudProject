FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y redis-server && \
    apt-get clean

# RUN apt-get install -y wget zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libxrender-dev

RUN apt-get install -y libglib2.0-0 build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev

RUN wget https://python.org/ftp/python/3.8.8/Python-3.8.8.tgz  \
    && tar -xf Python-3.8.8.tgz \
    && cd Python-3.8.8 \
    && ./configure --enable-optimizations \
    && make altinstall \
    && make -j 8 \
    && cd

RUN apt install python3-pip -y && python3.8 -m pip install --upgrade pip
RUN cd /home
WORKDIR /working
COPY . .
RUN chmod +x requirements.txt
RUN pip install -r requirements.txt
RUN apt install git -y
RUN apt install libgl1-mesa-glx -y \
    && apt install -y libsm6 -y
    
# RUN chmod +x requirements.txt && ./requirements.txt -y
# RUN pip install -r requirements.txt
# RUN apt install libgl1-mesa-glx -y \
#     && apt-get install libgtk2.0-0 -y \
#     && apt install -y libsm6 -y

# RUN apt install git -y \
#     && cd \
#     && git clone https://github.com/phonghongs/Unity-UIT_Car.git

# CMD python3.8 ~/Unity-UIT_Car/Code\ test\ Simulation/Raw\ code/raw_code.py