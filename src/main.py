import json
from modules.Role import *
from modules.User import *

# local variables
visited = []                # List to keep track of visited nodes.
queue = []                  # Initialize a queue


def __obj_dict(obj):
    return obj.__dict__


def printObject(obj):
    """
    Pretty print list of objects
    """
    json_string = json.dumps(obj, default=__obj_dict, indent=2)
    print(json_string)


def getSubOrdinates(userId, printResult=True):
    user = getUser(userId)

    if len(user) == 0:
        raise ValueError("User not found.")

    roleId = str(user[0].Role)

    if "graph" not in globals():
        raise ValueError(
            "Please setup roles & users before getting sub ordinates for this user_id")

    graph = globals()["graph"]

    roleIds = breathFirstSearch(visited, graph, roleId)

    result = getUsersByRole(roleIds[1:])

    if printResult == True:
        printObject(result)

    return result


def breathFirstSearch(visited, graph, node):
    visited.append(node)
    queue.append(node)

    result = []
    while queue:
        s = queue.pop(0)
        result.append(s)

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return result


try:
    setRoles([], loadDefault=True)
    setUsers([], loadDefault=True)
    # getSubOrdinates(4)

except Exception as e:
    print(str(e) + " | Refer to documentation for correct data structure and schema.")
