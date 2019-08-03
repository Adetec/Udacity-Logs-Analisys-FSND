# Logs Analysis
### My 1st project - Udacity FSND Program

## Project overview:
This project is an internal reporting tool that will use information from the database named `newsdata.sql` to discover what kind of articles the site's readers like.
The program will generate plain text reports on the data and store it into a text file.

## Requirements:
1. [Virtual box](https://www.virtualbox.org): is the software that actually runs the virtual machine. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.
**Ubuntu users**: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.
2. [Vagrant](https://www.vagrantup.com/): Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Install the version for your operating system.
**Windows users**: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.
3. [Python3](https://www.python.org/download/releases/3.0/)
4. [PostgreSQL](https://www.postgresql.org/docs/9.4/app-psql.html):is an open source relational database management system ( DBMS ) developed by a worldwide team of volunteers.
5. [News database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip): Contains the data to be analysed

### So what are we reporting, anyway?
Here are the questions the reporting tool should answer:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### How it works:
1. After installing requirements, clone the Udacity [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)
2. Open `vagrant` folder, clone this project inside, and copy the extracted database file `newsdata.sql` from dowloading [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) inside this project directory as well,
3. `cd` into this project directory in your terminal. Inside, you will find another directory called **vagrant**. Change directory to the **vagrant** subdirectory.
4. Run `vagrant up` to start running Virtual machine, please note that it might take some time to download the OS system and apply the settings
5. After seeing the prompt come back, run `vagrant ssh` to log in
6. cd into the `vagrant` directory and use the command `psql -d news -f newsdata.sql`.
Here's what this command does:
    * `psql ` — the PostgreSQL command line program
    * `-d news ` — connect to the database named news which has been set up for you
    * `-f newsdata.sql ` — run the SQL statements in the file newsdata.sql
    
    Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
7. Move to this project directory and make sure you are in by run `ls` command
8. Finally run `python logs_analysis.py`
9. Result should be printed and `output.txt` will be updated or created if it doesn't exist