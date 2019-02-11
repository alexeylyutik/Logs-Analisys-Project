# Log Analysis Project

### Description
You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

Why this project?
In this project, you will stretch your SQL database skills. You will get practice interacting with a live database both from the command line and from your code. You will explore a large database with over a million rows. And you will build and refine complex queries and use them to draw business conclusions from data.

Report generation
Building an informative summary from logs is a real task that comes up very often in software engineering. For instance, at Udacity we collect logs to help us measure student progress and the success of our courses. The reporting tools we use to analyze those logs involve hundreds of lines of SQL.

Database as shared resource
In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

This shows one of the valuable roles of a database server in a real-world application: it's a point where different pieces of software (a web app and a reporting tool, for instance) can share data.

### Problems to Solve
**1. What are the most popular three articles of all time?** 
   Which articles have been accessed the most? 
   Present this information as a sorted list with the most popular article at the top.

**2. Who are the most popular article authors of all time?**
  That is, when you sum up all of the articles each author has written, which authors get the most page views?
  Present this as a sorted list with the most popular author at the top.

**3. On which days did more than 1% of requests lead to errors?**
  The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

## Environment
* Python  3.5.2
* Postgresql 9.5.12

## Setup

### Virtual Machine with Vagrant
***Requirements***

1. The VirtualBox VM environment
2. The Vagrant configuration program
3. Installing VirtualBox

**VirtualBox** 
VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org, [here](https://www.virtualbox.org/wiki/Downloads). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

**Installing Vagrant**
Vagrant is the program that will download a Linux operating system and run it inside the virtual machine. [Install it from this site](https://www.vagrantup.com/downloads.html).

Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

Bringing up the database server
Vagrant takes a configuration file called Vagrantfile that tells it how to start your Linux VM. All vagrant files for this project can be found in the vagrant folder of this repo [vagrant](vagrant). Once you have a copy of this in your machine go to that directory, and run the command ```$ vagrant up```. Once completed you should see something like this:

*Successful vagrant up results: "Done installing PostgreSQL database!"*

Now you have a PostgreSQL server running in a Linux virtual machine. This setup is independent of any other database or web services you might have running on your computer, for instance for other projects you might work on. The VM is linked to the directory where you ran vagrant up.

To log into the VM, use a terminal in that same directory and run the following command ```$ vagrant ssh```. You'll then see something like this:

*A shell prompt on the Vagrant-managed Linux VM.*

In this shell, if you change directory to /vagrant and run *ls* there, you will see the Vagrantfile you downloaded ... and any other files you put into that directory from your computer, that will be the shared folder between VM and your computer.

### Now you Logged in!
If you are now looking at a shell prompt that starts with the word vagrant ex ```vagrant@vagrant:/vagrant$```, congratulations — you've gotten logged into your Linux VM.


## How to execute program
1. Unzip the sql file.
```cmd
$ unzip archive.zip
```
2. Load the data onto the database
```sql
psql -d news -f newsdata.sql
```
2. Run Python file
```cmd 
$ python3 LogAnalysis.py 
```


                              
                              
                              
