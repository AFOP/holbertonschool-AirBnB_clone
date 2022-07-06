# :scroll: AirBnB clone

![AirBnB clone image](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220705T224254Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7c4796d1496cfb8f767261f285ff02f6ef78cf6d1b5faf4f5c008d1337b4a889)

# :running: Description

The AirBnB project is a clone of AirBnB

This is the first step in creating our first full web application: the AirBnB clone. This first step is very important because what you build during this project will be used with all the other following projects: HTML/CSS templates, database storage, APIs, front-end integration...

## :running: how to start it: 

## step one: what can you with the command interpreter

In the command interpreter you can:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## :arrow_down: Installing and Using

Clone the repository into a new directory:

```
$ git clone https://github.com/alejolo311/AirBnB_clone
$ cd holbertonschool-AirBnB_clone
```

Run the command interpreter:

```
$ ./console.py
```

Into the command interpreter:

```
Welcome to the shell.   Type help or ? to list commands.

(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)

(hbnb) 
(hbnb) 
(hbnb) quit
guillaume@ubuntu:~/AirBnB$ 
```
## :wrench: Examples

* **all**
```
Welcome to the shell.   Type help or ? to list commands.

(hbnb) help all

Prints all string representation of all instances based or not on the class name

(hbnb) all
[BaseModel] (75f84d74-d908-4d70-8554-f072f3a1c4d0) {'id': '75f84d74-d908-4d70-8554-f072f3a1c4d0', 'created_at': datetime.datetime(2022, 7, 5, 21, 50, 7, 319976), 'updated_at': datetime.datetime(2022, 7, 5, 21, 50, 7, 319977), 'name': 'My_First_Model', 'my_number': 89}

(hbnb) 
(hbnb) quit
guillaume@ubuntu:~/AirBnB$ 
```

* **create**
```
Welcome to the shell.   Type help or ? to list commands.

(hbnb) help create
Creates a new instance of BaseModel and print its

(hbnb) create BaseModel
75f84d74-d908-4d70-8554-f072f3a1c4d0

(hbnb) 
(hbnb) quit
guillaume@ubuntu:~/AirBnB$ 
```

* **create**
```
(hbnb) help destroy
Deletes an instance based on the class name and id

(hbnb) destroy BaseModel 75f84d74-d908-4d70-8554-f072f3a1c4d0
(hbnb) 
(hbnb) quit
guillaume@ubuntu:~/AirBnB$ 
```

## AUTHORS
* **Andrés Ocaña** - *Documentación* - [AFOP](https://github.com/afop)  
