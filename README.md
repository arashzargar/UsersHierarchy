# Coding Challenge - Users Hierarchy

Users hierarchy: In our system each user belongs to a user-group with a defined set of permissions. We name such a group "Role". A certain role (unless it is the root) must have a parent role to whom it reports to. 

Notice how the System Administrator has no parent role and how Employee has as parent role the Supervisor. Naturally this cascading parent-child relationship means that Location Manager, Supervisor, Employee, Trainer are all children roles to System Administrator. 


## Task
Come up with a function, for an arbitrary collection of roles and users, given a user Id returns a list of ALL their subordinates (i.e: including their subordinate's subordinates). For example if you were given user #3 in the above example (Sam Supervisor), you should output objUser2 (Emily Employee) and objUser5 (Steve Trainer) Another example is if you were give user #1 in the above example (Adam Admin), you should output a list containing [objUser2, objUser3, objUser4, objUser5] in no particular order. 

### Tips
- Any role with parent 0 is a top level role. i.e: has no parents.
- A form of Object Oriented design might help in this case!

## Tech stack
- Python 3

### Installation
##### How to Install Python on Windows
There are three installation methods on Windows:
- The Microsoft Store
- The full installer
- Windows Subsystem for Linux
 
You can also use cmd.exe or Windows Terminal.

With the command line open, type in the following command and press Enter:
```
C:\> python --version
Python 3.8.4
```

##### How to Install Python on macOS
Python 2 comes preinstalled on older versions of macOS. This is no longer the case for current versions of macOS, starting with macOS Catalina.

There are two installation methods on macOS:
- The official installer
- The Homebrew package manager

With the command line open, type in the following commands:
```
# Check the Python 3 version
$ python3 --version
```
- Resources: https://www.python.org/downloads/

## Development

In this project I've focused on three main methods:
- setRoles
- setUsers
- getSubOrdinates


##### setRoles:
located in Role.py file, includes logics to:
- set roles
- validate roles
- get data either from default data (stores under /data/roles.json) or get as string 

##### setUsers:
located in User.py file, includes logics to:
- set users
- validate associated role for each user
- loadDefault (Boolean): to get data either from default data (stores under /data/users.json) or get as string 

##### getSubOrdinates:
located in main.py file, includes logics to:
- find all sub-ordinates for selected user
- validate user and roles
- loadDefault (Boolean): to 


#### Building form source

##### required Python packages
```python
pip install json
pip install collections
pip install unittest
```

### To run
Check `getSubOrdinates` function in ``main.py`` line 66, uncomment and set the right userId to look for sub-ordinated of selected user, the run following command
```sh
python3 main.py
```

##### To run Unit test

```sh
python3 -m unittest test.py
```

### Examples

``` python
# default role
roleObj = setRoles([], loadDefault=True)
#printObject(roleObj)

# string role
rolesData = '[{"Id":1,"Name":"System Administrator","Parent":0},{"Id":2,"Name":"Location Manager","Parent":1},{"Id":3,"Name":"Supervisor","Parent":2},{"Id":4,"Name":"Employee","Parent":3},{"Id":5,"Name":"Trainer","Parent":3}]'
roleObj = setRoles(rolesData, loadDefault=False)
#printObject(roleObj)

# default user
userObj = setUsers([], loadDefault=True)
#printObject(userObj)

# string user
userData = '[{"Id":1,"Name":"Adam Admin","Role":1},{"Id":2,"Name":"Emily Employee","Role":4},{"Id":3,"Name":"Sam Supervisor","Role":3},{"Id":4,"Name":"Mary Manager","Role":2},{"Id":5,"Name":"Steve Trainer","Role":5}]'
userObj = setUsers(userData, loadDefault=False)
printObject(userObj)
```


### Approach
I've used graph theory's Breadth-first search to search roles graph. It starts at the root and explores all of the neighbour nodes at the present depth prior to moving on to the nodes at the next depth level.
- Reference: https://en.wikipedia.org/wiki/Breadth-first_search

### Assumptions
- Target organizations do not have thousands of complex roles (BFS is not scalable for complex use cases such as map route or social network platforms etc.)

### Improvement Area

- The data layer at the moment is stored in json and accordingly loaded in memeory, to improve this app it's required to store the data in DataBase of any sort (SQL or NoSQL), depends on future requirements and scalability of the system.
- Increase code coverage by adding more unit test and integration tests
