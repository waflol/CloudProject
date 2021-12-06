FROM ubuntu:18.04
RUN apt update -y & apt upgrade -y

RUN apt install -y build-essential wget zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libxrender-dev

RUN wget https://python.org/ftp/python/3.8.8/Python-3.8.8.tgz  \
    && tar -xf Python-3.8.8.tgz \
    && cd Python-3.8.8.tgz \
    && ./configure --enable-optimization \
    && make -j 8 \
    && make altinstall \
    && cd

RUN apt install python3-pip -y && python3.8 -m pip install --upgrade pip
WORKDIR /install
COPY . .
RUN chmod +x requirements.txt && ./requirements.txt -y
RUN pip install -r requirements.txt
RUN apt install libgl1-mesa-glx -y \
    && apt-get install libgtk2.0-0 -y \
    && apt install -y libsm6 -y

RUN apt install git -y \
    && cd \
    && git clone https://github.com/phonghongs/Unity-UIT_Car.git

CMD python3.8 ~/Unity-UIT_Car/Code