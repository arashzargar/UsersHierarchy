import json
from collections import defaultdict


class Role(object):
    """
    Role class
    """

    def __init__(self, Id, Name, Parent):
        self.Id = Id
        self.Name = Name
        self.Parent = Parent


def __roleObjDecoder(obj):
    """
    Role decoder
    :param obj: object
    """
    return Role(obj['Id'], obj['Name'], obj['Parent'])


def setRoles(rolesData, loadDefault=False):
    """
    Set roles data

    :param rolesData: roles json string
    :param loadDefault: True will read the data from Roles.json in /data directory
    :return: list of role objects
    """
    roles = []

    if loadDefault == True:
        with open('data/roles.json') as role:
            roles = json.loads(role.read(), object_hook=__roleObjDecoder)
    else:
        roles = json.loads(rolesData, object_hook=__roleObjDecoder)

    # validate if no more than 1 Admin role entered
    if(sum(u.Parent == 0 for u in roles) > 1):
        raise ValueError(
            "Invalid value, there should not be more than one Admin role in the system")

    # validate if every role has valid parent [except Admin]
    for role in roles:
        if role.Parent == 0:
            continue

        if(sum(x.Id == role.Parent for x in roles) == 0):
            raise ValueError(
                f"Invalid value, role_Id: {role.Id} has invalid parent")

    # convert roles to graph
    __covertRolesToGraph(roles)

    # set global roles variable
    globals()["roles"] = roles

    return roles


# local variables
graph = defaultdict(list)   # graph dictionary


def __covertRolesToGraph(roles):
    lastNodes = []

    for role in roles:
        if role.Parent == 0:
            continue

        graph[str(role.Parent)].append(str(role.Id))

        lastNodes.append(role.Id)
        if role.Parent in lastNodes:
            lastNodes.remove(role.Parent)

    for item in lastNodes:
        graph[str(item)] = []

    globals()["graph"] = graph


def getRoles():
    if "roles" not in globals():
        return None

    return globals()["roles"]
