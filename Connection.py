# -*- coding: utf-8 -*-
import base64
import numpy as np
import socketio # version 4.2.1
import eventlet # version 0.32.0
# import eventlet.wsgi
import cv2 # version 4.5.4-dev
from PIL import Image
from flask import Flask # version 1.1.2
from io import BytesIO
# ------------- Add library ------------#
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# --------------------------------------#
error_arr = np.zeros(5)
# initialize our server
sio = socketio.Server()
# our flask (web) app
app = Flask(__name__)


# registering event handler for the server
@sio.on('telemetry')
def telemetry(sid, data):
    if data:
        steering_angle = 0  # Góc lái hiện tại của xe
        speed_callback = 0  # Vận tốc hiện tại của xe
        image = 0  # Ảnh gốc
        # Original Image
        image = Image.open(BytesIO(base64.b64decode(data["image"])))
        imageRGB = np.asarray(image)
        cv2.imshow('',imageRGB)

        """
        - Chương trình đưa cho bạn 3 giá trị đầu vào:
            * steering_angle: góc lái hiện tại của xe
            * speed: Tốc độ hiện tại của xe
            * image: hình ảnh trả về từ xe

        - Bạn phải dựa vào 3 giá trị đầu vào này để tính toán và gửi lại góc lái và tốc độ xe cho phần mềm mô phỏng:
            * Lệnh điều khiển: send_control(sendBack_angle, sendBack_Speed)
            Trong đó:
                + sendBack_angle (góc điều khiển): [-25, 25]  NOTE: ( âm là góc trái, dương là góc phải)
                + sendBack_Speed (tốc độ điều khiển): [-150, 150] NOTE: (âm là lùi, dương là tiến)
        """
        sendBack_angle = 0
        sendBack_Speed = 50
        # ------------------------------------------  Work space  ----------------------------------------------#
        # ['car','pedestrian','road','roadcone','roadline','trafficsign']
        cv2.waitKey(1)


        print('toc do nap len {} : {}'.format(sendBack_angle, sendBack_Speed))
        print('van toc tra ve {} : {}'.format(steering_angle, speed_callback))
        send_control(sendBack_angle, sendBack_Speed)
        print(sendBack_Speed)

    else:
        sio.emit('manual', data={}, skip_sid=True)


@sio.on('connect')
def connect(sid, environ):
    print("connect ", sid)
    print('on connect')
    send_control(0, 0)


def send_control(steering_angle, throttle):
    sio.emit(
        "steer",
        data={
            'steering_angle': steering_angle.__str__(),
            'throttle': throttle.__str__(),
        },
        skip_sid=True)








if __name__ == '__main__':
    # -----------------------------------  Setup  ------------------------------------------#

    # --------------------------------------------------------------------------------------#
    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(sio, app)
    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)

