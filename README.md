# AirBnB Clone - The Console

## Project Overview

The primary focus of this current project is to develop a command-line interpreter that manages the objects of our AirBnB clone application. This command interpreter will allow us to:

- Create new objects (ex: User, Place)
- Retrieve objects from files or databases
- Perform operations on objects (count, compute stats, etc.)
- Update object attributes
- Destroy objects

Created by:

- Abigail Allman: [LinkedIn](https://www.linkedin.com/in/abigailraleman/)
- Kelci Atkinson: [LinkedIn](https://www.linkedin.com/in/kelciatkinson/)

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
