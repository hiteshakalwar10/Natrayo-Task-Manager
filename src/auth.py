import bcrypt

from .database import get_connection


class AuthManager:

    def __init__(self):
        self.connection = get_connection()

    def signup(self, username, password):
        username = username.strip()

        if not username:
            raise ValueError("Username cannot be empty.")

        if not password:
            raise ValueError("Password cannot be empty.")

        cursor = self.connection.cursor()

        query = """
            SELECT id
            FROM users
            WHERE username = %s
        """

        cursor.execute(query, (username,))
        existing_user = cursor.fetchone()

        if existing_user is not None:
            cursor.close()
            raise ValueError("Username already exists.")

        password_hash = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )

        query = """
            INSERT INTO users (username, password)
            VALUES (%s, %s)
        """

        cursor.execute(
            query,
            (username, password_hash.decode("utf-8"))
        )

        self.connection.commit()

        user_id = cursor.lastrowid

        cursor.close()

        return user_id

    def login(self, username, password):
        username = username.strip()

        cursor = self.connection.cursor()

        query = """
            SELECT id, username, password, role
            FROM users
            WHERE username = %s
        """

        cursor.execute(query, (username,))

        user = cursor.fetchone()

        cursor.close()

        if user is None:
            return None

        stored_password = user[2]

        if bcrypt.checkpw(
            password.encode("utf-8"),
            stored_password.encode("utf-8")
        ):
            return {
                "id": user[0],
                "username": user[1],
                "role": user[3]
            }

        return None