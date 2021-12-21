.. raw:: html

Table of Contents
~~~~~~~~~~~~~~~~~
 - `Set up environments`_
 - `Simple training`_
 - `Simple training on unity editor`_
 - `Test on unity editor`_
 - `Build custom track and export it for training on cloud`_
 - `Documentation`_
Set up environments
~~~~~~~~~~~~~
Yêu cầu: Python 3

- B1: clone project mlagents

.. code:: bash

    $ git clone --branch release_18 https://github.com/Unity-Technologies/ml-agents.git

-B2: cài đặt mlagents và mlagents-envs

.. code:: bash

    $ cd <path-root>/ml-agents/ml-agents
    
    $ pip install e .
    
    $ cd <path-root>/ml-agents/ml-agents-envs
    
    $ pip install e .
Có thể sử dụng pip show ml-agents/ml-agents-envs để kiểm tra đã cài đặt chưa
-B3: clone map để training

.. code:: bash

   $ git clone https://github.com/waflol/Map_Demo.git
   
Simple training
~~~~~~~~~~~~~
- B1: tạo file config.yaml. `Exmaple <https://github.com/waflol/Map_Demo/blob/main/config.yaml>`__
- B2: cung cấp quyển cho các file *.x86_64 và UnityPlayer.so trong Map_Demo
- B3: Tạo biến env_path dẫn tới file *.x86_64
- B5: Training

.. code:: bash
  $ mlagents-learn config.yaml --run-id="test" --env=$env_path --no-graphics



Documentation
~~~~~~~~~~~~~
Latest **documentation** is avaliable on `Read the
Docs <https://github.com/Unity-Technologies/ml-agents/tree/release_18>`__
