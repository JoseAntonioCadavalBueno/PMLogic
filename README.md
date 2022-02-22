# PMLogic
Easy multilayer perceptron, it will try turn celsius to farenheight.
- Requirement:
  - Cuda ver. 11.6
  - Cudnn ver. 8.3
  - Python ver. 3.9
  - Tensorflow ver. 2.8
  - Anaconda 3
- Install steps:
  - 1.- Check your GPU: https://developer.nvidia.com/cuda-gpus
  - 2.- Install Cuda
  - 3.- Copy from cudnn these files:
    - "\cudnn-11.0-windows-x64-v8.0.4.30\cuda\bin\cudnn64_8.dll" to "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\bin".
    - "\cudnn-11.0-windows-x64-v8.0.4.30\cuda\include\cudnn.h" to "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\include".
    - "\cudnn-11.0-windows-x64-v8.0.4.30\cuda\lib\x64\cudnn.lib" to "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\lib\x64".
  - 4.- Install Anaconda 3 and execute anaconda prompt (anaconda3)
  - 5.- Create a new env: "conda create --name 'your name'"
  - 6.- Activate the env: "conda activate 'your name'"
  - 7.- Install tensorflow: "pip install tensorflow-gpu"
  - 8.- Run check.py for check if everything is correct
