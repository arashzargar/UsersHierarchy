import unittest
from modules.User import *
from modules.Role import *
from main import *
from unittest.mock import patch, Mock


class TestSum(unittest.TestCase):
    @patch('main.getRoles')
    def test_set_user_successful(self, MockRoles):
        """
        Test that it set valid set of users
        """

        # Arrange
        getRoles = MockRoles()
        roles = []

        roles.append(Role(1, 'Admin', 0))
        roles.append(Role(2, 'Manager', 1))
        roles.append(Role(3, 'Supervisor', 2))

        getRoles.return_value = roles

        data = '[{"Id":1,"Name":"Adam Admin","Role":1},{"Id":2,"Name":"Emily Employee","Role":2},{"Id":3,"Name":"Sam Supervisor","Role":3}]'

        # Act
        result = setUsers(data, loadDefault=False)

        # Assert
        self.assertEqual(len(result), 3)

    @patch('main.getRoles')
    def test_set_user_failed(self, MockRoles):
        """
        Test that it set valid set of users
        """

        # Arrange
        getRoles = MockRoles()
        roles = []

        roles.append(Role(1, 'Admin', 0))
        roles.append(Role(2, 'Manager', 1))
        roles.append(Role(3, 'Supervisor', 2))

        getRoles.return_value = roles

        data = '[{"Id":1,"Name":"Adam Admin","Role":1},{"Id":2,"Name":"Emily Employee","Role":2},{"Id":3,"Name":"Sam Supervisor","Role":3}]'

        # Act
        result = setUsers(data, loadDefault=False)

        # Assert
        self.assertIsNot(len(result), 6)

    def test_set_role_successful(self):
        """
        Test that it set valid set of roles
        """

        # Arrange
        data = '[{"Id":1,"Name":"System Administrator","Parent":0},{"Id":2,"Name":"Location Manager","Parent":1},{"Id":3,"Name":"Supervisor","Parent":2},{"Id":4,"Name":"Employee","Parent":3},{"Id":5,"Name":"Trainer","Parent":3}]'

        # Act
        result = setRoles(data, loadDefault=False)

        # Assert
        self.assertEqual(len(result), 5)

    def test_get_sub_ordinates_successful(self):
        """
        Test that it set valid set of users
        """

        # Arrange
        setRoles([], loadDefault=True)
        setUsers([], loadDefault=True)

        # Act
        result = getSubOrdinates(4, printResult=False)

        # Assert
        self.assertEqual(len(result), 3)


if __name__ == '__main__':
    unittest.main()
