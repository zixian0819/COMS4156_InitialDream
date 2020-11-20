"""Import required packages."""
from flaskr.db import get_db

DATABASE = get_db()


class Task(DATABASE.Model):  # pylint: disable=too-few-public-methods
    """Task class."""
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    title = DATABASE.Column(DATABASE.String(255), nullable=False)
    date = DATABASE.Column(DATABASE.Date, nullable=False)

    def __repr__(self):
        return f'{self.title}'
