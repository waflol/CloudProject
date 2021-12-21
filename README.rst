.. raw:: html
**Important note**

    Các thư mục com.unity.learn.iet-framework-master và ml-agents-release_18 là các thư mục kèm theo bắt buộc phải cài đặt (các gói phụ thuộc như hình dưới)
 
.. image:: https://github.com/waflol/CloudProject/blob/main/images/1.png

Table of Contents
~~~~~~~~~~~~~~~~~
 - `Set up environments`_
 - `Simple training`_
 - `Simple training on unity editor`_
 - `Test on unity editor`_
 - `Documentation`_
Set up environments
~~~~~~~~~~~~~
Yêu cầu: Python 3, pip và git

- B1: clone project mlagents

.. code:: bash

    $ git clone --branch release_18 https://github.com/Unity-Technologies/ml-agents.git

- B2: cài đặt mlagents và mlagents-envs

.. code:: bash

    $ cd <path-root>/ml-agents/ml-agents
    $ pip install e .
    
    $ cd <path-root>/ml-agents/ml-agents-envs
    $ pip install e .
Có thể sử dụng pip show ml-agents/ml-agents-envs để kiểm tra đã cài đặt chưa

- B3: clone map để training

.. code:: bash

   $ git clone https://github.com/waflol/Map_Demo.git
   
Simple training
~~~~~~~~~~~~~
- B1: tạo file config.yaml. `Exmaple <https://github.com/waflol/Map_Demo/blob/main/config.yaml>`__
- B2: cung cấp quyển cho các file *.x86_64 và UnityPlayer.so trong Map_Demo
.. code:: bash

   $ chmod -R 755 <path-to-Map_Demo>/Map_Demo/TrainingA/linux/TrainingA.x86_64
   $ chmod -R 755 <path-to-Map_Demo>/Map_Demo/TrainingA/linux/UnityPlayer.so
   
- B3: Tạo biến env_path dẫn tới file *.x86_64
- B5: Training
.. code:: bash

   $ mlagents-learn <path-to-config>/config.yaml --run-id="test" --env=$env_path --no-graphics

Simple training on unity editor
~~~~~~~~~~~~~
- B1: Cài unity hub, unity editor và git clone project này về
- B2: Vào unity hub, chọn add chọn thư mục CarAIUnityV1 trong project và cái các gói phụ thuộc nếu có yêu cầu ( có sẵn mlagents và iet-framework-master trong project)
- (Optional-nếu làm B2 rồi thì bỏ qua): Tạo new project, xong vào Assets > Import Package > Custom Package, xong chọn file Map_projectDEV.unitypackage và cài đặt các gói phụ thuộc
- B3: cài đặt mlagents và mlagents-envs

.. code:: bash

    $ cd <path-root>/ml-agents/ml-agents
    $ pip install e .
    
    $ cd <path-root>/ml-agents/ml-agents-envs
    $ pip install e .
    
- B3: tạo file config.yaml
- B4: Chạy đoạn code dưới để training
.. code:: bash

   $ mlagents-learn <path-to-config>/config.yaml --run-id="test" --env=$env_path --no-graphics
- B5: Nhấn nút play trên unity editor và quan sát

Test on unity editor
~~~~~~~~~~~~~
- B1: Tại working space đang training có thư mục result, ta vào results > <run-id> > ArcadeDriver.onnx.
- B2: Trong giao diện unity editor, ta điều hướng tới Assets > Karting > Prefabs > AI, rồi kéo file ArcadeDriver.onnx vào thư mục AI đó
- B3: Trong unity editor, ta vào Assets > Scenes > MLTraining > Test_map, sau đó mở scene Testing lên.
- B4: Chọn game object KartClassic_MLAgent trên thanh Hierarchy, trên thanh Inspector (bên phải), ta mở Behavior Parameters xong kéo model mời thêm trước đó vào phần model.
- B5: Nhấn nút play để xem kết quả

Documentation
~~~~~~~~~~~~~
Latest **documentation** is avaliable on `Read the
Docs <https://github.com/Unity-Technologies/ml-agents/tree/release_18>`__
