Install xcode
$ sudo xcode-select --install
Install brew
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
Don’t forget to update your brew
$ brew doctor
We then need to update our ~/.bash_profile file so that it searches the homebrew path for packages before searching on the system path.
Use the text editor you are most comfortable with here. In my case i went with sublime because, why not?
$ subl ~/.bash_profile
In the file insert the following line.
# Homebrew 
export PATH=/usr/local/bin:$PATH
The comment i added was just for you to know what the path is for later on, it is not compulsory but it is advisable as you are bound to forget this things soon enough.
Save your file and close it. At this point you now need to manually source your file. This is just to ensure the changes are loaded.
$ source ~/.bash_profile
Install python
Phew! Now let’s install python.
$ brew install python python3
I already have my python, why am I installing it again? Good question. Mac comes pre-installed with python. It is, however, advisable to install your own which leaves the system one to system routines and configurations.
Test your python installation by typing python on your terminal. If the python interpreter appears, you are good to go.
Be sure to check what python version you are using. You don’t want to use the system python.
$ which python2
/usr/local/bin/python2
$ which python3
/usr/local/bin/python3
If the result you are getting at this point is usr/bin/python, then that means you are using the system python.
Quick note:
Python — gives you the system python
Python2 — gives you the python2 you installed yourself.
python3 — gives you the python3 you installed.
Prepare for OpenCV installation
As you may have guessed already, our next thing will be installing OpenCV.
However, first things first. We will start with installing homebrew-science.
These formulæ provide software tailored to scientific endeavours. Need to store large amounts of data in a sparse matrix, solve a huge optimization problem or process the images from your space telescope? Maybe we can help!
$ brew install homebrew/science
Before installing OpenCV, we will add tools or rather prerequisites before installing it. There is nothing wrong with going straight to installing it, but we just want to make sure we have all we require first.
Let’s first install numpy. Numpy helps in scientific computations in python.
$ pip install numpy

$ brew install cmake pkg-config
$ brew install jpeg libpng libtiff openexr
$ brew install eigen tbb
We have just added tools to help in building and compile our OpenCV like CMAKE, Libraries used for operations on the images such as jpeg and ones for optimization.
This will aid in loading images of different formats and extensions such as JPEG and PNG.
CMAKE, on the other hand, is a family of tools used to build, test and package softwares.
Test your openCV installation by importing cv2 inside the python shell. It works? Great!
Install OpenCV
Let’s get the latest OpenCV from github.
$ cd ~
$ git clone https://github.com/opencv/opencv
We also need to clone the OpenCV contrib
$ git clone https://github.com/opencv/opencv_contrib
Don’t give up yet, we are almost there.
Configure OpenCV and Python
We need to setup our build. We will first need to create a build directory on the OpenCV directory we just cloned.
$ cd ~/opencv
$ mkdir build
$ cd build
To finish our build we will need the assistance of the CMAKE we downloaded earlier.
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
-D PYTHON2_LIBRARY= \
-D PYTHON2_INCLUDE_DIR= \
-D PYTHON3_LIBRARY=YYY \
-D PYTHON3_INCLUDE_DIR=ZZZ \
-D PYTHON3_EXECUTABLE=$VIRTUAL_ENV/bin/python \
-D BUILD_opencv_python2=ON \
-D BUILD_opencv_python3=ON \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D BUILD_EXAMPLES=ON ..
We need to configure our Python2 and Python3 libraries. We need to get to where libpython2.7*/3.*.dylib is located.
For python 2
/usr/local/Cellar/python/2.7.14/Frameworks/Python.framework/Versions/2.7/lib/python2.7/config/libpython2.7.dylib
For python 3
/usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/lib/python3.6/config-3.6m-darwin/libpython3.6.dylib
Always make sure you edit this according to the python versions installed on your system.
We will also need to add the Include_DIR for both python2 and python3. We will need to locate our python.h file(out python header file).
For python 2
/usr/local/Cellar/python/2.7.14/Frameworks/Python.framework/Versions/2.7/include/python2.7
For python 3
/usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/include/python3.6m
Fill in the blanks this time with our newly found information appended inside your build directory.
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
-D PYTHON2_LIBRARY=/usr/local/Cellar/python/2.7.14/Frameworks/Python.framework/Versions/2.7/lib/python2.7/config/libpython2.7.dylib \
-D PYTHON2_INCLUDE_DIR=/usr/local/Cellar/python/2.7.14/Frameworks/Python.framework/Versions/2.7/include/python2.7 \
-D PYTHON3_LIBRARY=/usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/lib/python3.6/config-3.6m-darwin/libpython3.6.dylib \
-D PYTHON3_INCLUDE_DIR=/usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/include/python3.6m \
-D PYTHON3_EXECUTABLE=$VIRTUAL_ENV/bin/python \
-D BUILD_opencv_python2=ON \
-D BUILD_opencv_python3=ON \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D BUILD_EXAMPLES=ON ..
The command will configure our OpenCV with both Python2 and Python3 for us.
We are now down to the last point.
Compiling our OpenCV
$ make -j4
The j value does not always have to be 4. Switch that up depending on the number of processors on your machine. If it is dual core use -j2 and so on.
The compiling might take a while, you can take a break at this point.
Use the code below to install OpenCV on your system.
$ sudo make install
