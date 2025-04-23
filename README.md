# AirBnB Clone - The Console

## Project Overview

Welcome to our AirBnB Clone project! This is the first step towards building a full web application: the AirBnB clone. This initial phase is crucial as it establishes the foundation for all future projects: HTML/CSS templating, database storage, API development, and front-end integration.

The primary focus of this current project is to develop a command-line interpreter that manages the objects of our AirBnB clone application. This command interpreter will allow us to:

- Create new objects (ex: User, Place)
- Retrieve objects from files or databases
- Perform operations on objects (count, compute stats, etc.)
- Update object attributes
- Destroy objects

## About the Developers

Hello! We're Abigail Allman and Kelci Atkinson, software engineering students passionate about building scalable and modular applications. This project represents our deep dive into Python's object-oriented programming concepts and the development of complex command-line interfaces.

Connect with us:
- Abigail Allman: [LinkedIn](https://www.linkedin.com/in/abigailraleman/)
- Kelci Atkinson: [LinkedIn](https://www.linkedin.com/in/kelciatkinson/)

## The Journey of Building the AirBnB Clone

Our development process unfolded in several key stages:

1. **Understanding the Problem Space**: We began by researching AirBnB's architecture and identifying core entities like Users, Places, Reviews, etc.

2. **Designing the Base Architecture**: Our first major challenge was developing the BaseModel class - the foundation for all other models. This involved implementing serialization/deserialization mechanisms and unique ID generation.

3. **Developing the Storage Engine**: Creating the FileStorage class introduced us to JSON serialization/deserialization, file I/O in Python, and maintaining object persistence.

4. **Building the Command Interpreter**: Perhaps the most challenging part was developing the command-line interface using Python's cmd module, which required careful parsing of user inputs and thoughtful error handling.

5. **Implementing Unit Tests**: We adopted a test-driven development approach, writing comprehensive unit tests for all components to ensure robustness.

Each stage presented unique learning opportunities and challenges, from understanding object serialization to managing complex command parsing logic.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/kelciatkinson/atlas-AirBnB_clone.git
   cd atlas-AirBnb_clone
   ```
2. Make the console executable:
   ```sh
   chmod +x console.py
   ```

## Usage

### Command Interpreter
The command interpreter serves as a command-line interface facilitating user interaction with the AirBnB clone, allowing users to effectively manage the application's objects.

In order to launch the command interpreter, follow these instructions:

```
Clone the project repository from GitHub.
Check to see that Python 3 is installed on your system.
Open a terminal and arrive at the project directory.
Run the command ./console.py in order to launch the command interpreter.
```

### Commands for the Command Interpreter
```
all: Retrieve all objects/all objects of a specific class.
create: Create new instance of an object.
destroy: Delete an object from system.
help: Show available commands or describe specific command actions.
quit: Exit the command interpreter.
show: Display information about a specific object.
update: Update the attributes of an object.
```
In order to execute a command, type the command followed by the applicable arguments or options and push Enter.

### Examples
A few demonstrations of the usage of the command interpreter:

Create User:
```sh
Creating new user: 'create <class_name>'
```

Listing all objects:
```sh
'all'
```

Listing all objects of a class:
```sh
'all <class_name>
```

Quit the command interpreter:
```sh
quit
```

## Classes
```
Amenity
BaseModel
City
Place
Review
State
User
```

## Authors
+ Kelci Atkinson <kelci.atkinson@atlasschool.com>
+ Abigail Aleman <abigail.aleman@atlasschool.com>
