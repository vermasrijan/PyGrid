from ... import db


class Config(db.Model):
    """ Configs table.
        Columns:
            id (Integer, Primary Key): Config ID.
            config (String): Dictionary
            is_server_config (Boolean) : Boolean flag to indicate if it is a server config (True) or client config (False)
            fl_process_id (Integer, Foreign Key) : Reference to FL Process.
    """

    __tablename__ = "static__config__"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    config = db.Column(db.PickleType)
    is_server_config = db.Column(db.Boolean, default=False)
    fl_process_id = db.Column(db.BigInteger, db.ForeignKey("static__fl_process__.id"))

    def __str__(self):
        return f"<Config id: {self.id} , configs: {self.config}>"
