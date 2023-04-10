from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


engine = create_engine('sqlite:///ads.db', echo=True)
Base = declarative_base()

class Ad(Base):
    __tablename__ = 'ads'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
    owner = Column(String)

    def __repr__(self):
        return f"<Ad(title='{self.title}', description='{self.description}', date_created='{self.date_created}', owner='{self.owner}')>"

Base.metadata.create_all(engine)


app = Flask(__name__)


Session = sessionmaker(bind=engine)
session = Session()


@app.route('/ads', methods=['POST'])
def create_ad():
    ad_data = request.get_json()
    ad = Ad(title=ad_data['title'], description=ad_data['description'], owner=ad_data['owner'])
    session.add(ad)
    session.commit()
    return jsonify({'message': 'Ad created successfully!', 'data': ad.__repr__()})

@app.route('/ads/<int:id>', methods=['GET'])
def get_ad(id):
    ad = session.query(Ad).filter_by(id=id).first()
    return jsonify({'data': ad.__repr__()})

@app.route('/ads/<int:id>', methods=['DELETE'])
def delete_ad(id):
    ad = session.query(Ad).filter_by(id=id).first()
    session.delete(ad)
    session.commit()
    return jsonify({'message': 'Ad deleted successfully!'})

if __name__ == '__main__':
    app.run()
