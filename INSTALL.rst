Installing PyMultiNest and PyAPEMoST
=================================================

.. contents::

To use PyMultiNest or PyAPEMoST, follow these installation steps.
If you only want to use one of them, skip steps according.

Installing the python library
------------------------------------

Just run ::
   
     $ python setup.py install

or if you only want to install locally::

     $ python setup.py install --user

Installing the bridge to MultiNest
------------------------------------

1. build MultiNest in some directory $MULTINEST::

     $ export MULTINEST=/my/multinest/directory

     $ cd $MULTINEST && make libnest3.so

libnest3.so should be a dynamic library (compiled with -fPIC, linked with -shared -llapack -lpthread).

2. build the multinest_bridge::

     $ make -C multinest_bridge libcnest.so

Installing the bridge to APEMoST
------------------------------------

3. build APEMoST in some directory $APEMOST::
  
     $ export APEMOST=/my/apemost/directory

     $ cd $APEMOST && make libapemost.so

Running some code
--------------------------

PyMultiNest / PyAPEMoST have to be able to find the corresponding 
libraries. So put the three directories in the dynamic library load path::

     $ export LD_LIBRARY_PATH=$MULTINEST:$PWD/multinest_bridge:$APEMOST

Test importing the libraries::

     $ python -c 'import pymultinest'
     $ python -c 'import pyapemost'

5. Try out the demo programs distributed in the package. They produce a lot of output, so lets create a temporary directory::

     $ mkdir /tmp/demo_output
     $ cd /tmp/demo_output
     
     $ mkdir chains/
     $ python $OLDPWD/pymultinest_demo.py
     
     $ python $OLDPWD/pyapemost_demo.py

Congratulations! You are now ready to run your own code.

Generating the documentation
----------------------------

Go into doc and run make::

     $ cd doc && make html


