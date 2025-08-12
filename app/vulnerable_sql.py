def get_user_by_username(self, username: str):
    query = text("SELECT * FROM users WHERE username = :username")
    result = self.db.execute(query, {"username": username})
    return result.fetchone()