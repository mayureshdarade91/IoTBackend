from sqlalchemy.orm import relationship
from .. import db

class Device(db.Model):
    """ Device Model for storing device related details """
    __tablename__ = "device"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    org_id = db.Column(db.Integer)
    device_code = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    last_active = db.Column(db.DateTime, nullable=True)
    sensor = relationship("Sensor", backref='Device', lazy=True)

    def __init__(self,org_id,device_code,name,registered_on,last_active = None,sensor = []):
        self.org_id = org_id
        self.name = name
        self.device_code = device_code
        self.registered_on = registered_on
        self.last_active = last_active
        self.sensor = sensor   

    def __repr__(self):
        return "<Device '{}'>".format(self.name)