## Zyzzfit App


## Dependency
<p>Please make sure that you have the following dependencies installed:</p>

+ msvc-runtime==14.29.30133
+ python-dateutil==2.8.2
+ Python Version: 3.10.0
+ Download MySQL following the instructions here: https://www.mysql.com/de/downloads/



## Running the App:
+ run main.py make sure all dependencies are installed
+ All configurable variables are defined in main.py
+ This means if you need to change the SQL configuration, this is where you do it



## Configuring the MySQL server:
+ configurations are made in main.py in set_env_variables()
+ The MySQL password should be set to the users password that they set up when downloading MySQL for their machine.
+ By default the MySQL user is root and the MySQL host is localhost.
+ You may also change the database name in the same location