# PMLogic
Easy multilayer perceptron that can turn celsius to farenheight.
*Requirement:
  - Cuda ver. 11.6
  - Cudnn ver. 8.3
  - Python ver. 3.9
  - Tensorflow ver. 2.8
  - Anaconda 3
*Install steps:
  1.- Check your GPU: https://developer.nvidia.com/cuda-gpus
  2.- Install Cuda\n
  3.- Copy from cudnn these files:\n
          "\cudnn-11.0-windows-x64-v8.0.4.30\cuda\bin\cudnn64_8.dll" to "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\bin".\n
          "\cudnn-11.0-windows-x64-v8.0.4.30\cuda\include\cudnn.h" to "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\include".\n
          "\cudnn-11.0-windows-x64-v8.0.4.30\cuda\lib\x64\cudnn.lib" to "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\lib\x64".\n
  4.- Install Anaconda 3 and execute anaconda prompt (anaconda3)\n
  5.- Create a new env: "conda create --name 'your name'"\n
  6.- Activate the env: "conda activate 'your name'"\n
  7.- Install tensorflow: "pip install tensorflow-gpu"\n
  8.- Run check.py for check if everything is correct\n
