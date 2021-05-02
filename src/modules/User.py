import json
from modules.Role import getRoles


class User(object):
    """
    User class
    """

    def __init__(self, Id, Name, Role):
        self.Id = Id
        self.Name = Name
        self.Role = Role


def __userObjDecoder(obj):
    """
    User decoder
    :param obj: object
    """
    return User(obj['Id'], obj['Name'], obj['Role'])


def setUsers(usersData, loadDefault=False):
    """
    Set users data

    :param usersData: users json string
    :param loadDefault: True will read the data from Users.json in /data directory
    :return: list of user objects
    """
    users = []

    if loadDefault == True:
        with open('data/users.json') as user:
            users = json.loads(user.read(), object_hook=__userObjDecoder)
    else:
        users = json.loads(usersData, object_hook=__userObjDecoder)

    # get roles
    roles = getRoles()

    # check if roles are set
    if roles == None:
        raise ValueError(f"Please set roles before setting users")

    # validate if right role for the user
    for user in users:
        if(sum(r.Id == user.Role for r in roles) == 0):
            raise ValueError(
                f"Invalid roleId value for userId: {user.Id}")

    globals()["users"] = users

    return users


def getUser(id):
    if "users" not in globals():
        return None

    users = globals()["users"]

    return [u for u in users if u.Id == id]


def getUsersByRole(roleIds):
    result = []
    users = getUsers()

    for x in roleIds:
        response = [u for u in users if u.Role == int(x)]
        result.append(response)

    return result


def getUsers():
    if "users" not in globals():
        return None

    return globals()["users"]
