from FilterAPI import db
from flask import jsonify


class Data(db.Model):
    # create models here
    id = db.Column(db.Integer, primary_key=True)
    Symbol = db.Column(db.String)
    Name = db.Column(db.String)
    Number = db.Column(db.String)
    Volume = db.Column(db.String)
    Value = db.Column(db.String)
    Yesterday = db.Column(db.String)
    First = db.Column(db.String)
    LastPriceValue = db.Column(db.String)
    LastPriceChange = db.Column(db.String)
    LastPricePercent = db.Column(db.String)
    FinalPriceValue = db.Column(db.String)
    FinalPriceChange = db.Column(db.String)
    FinalPricePercent = db.Column(db.String)
    TheLeast = db.Column(db.String)
    TheMost = db.Column(db.String)
    EPS = db.Column(db.String)
    PE = db.Column(db.String)
    BuyCount = db.Column(db.String)
    BuyVolume = db.Column(db.String)
    BuyPrice = db.Column(db.String)
    SaleCount = db.Column(db.String)
    SaleVolume = db.Column(db.String)
    SalePrice = db.Column(db.String)

    #create methods here
    def __repr__(self):
        return f"{self.id} {self.Symbol}"

    @staticmethod
    def getAll():
        result = []
        data = Data.query.all()
        for i in data:
            sample = {'id':i.id, 'Symbol':i.Symbol, 'Name':i.Name, 'Number':i.Number, 'Volume': i.Volume,'Value':i.Value,'Yesterday':i.Yesterday,
                'First':i.First,'LastPriceValue':i.LastPriceValue, 'LastPriceChange':i.LastPriceChange, 'LastPricePercent':i.LastPricePercent,
                'FinalPriceValue':i.FinalPriceValue, 'FinalPriceChange':i.FinalPriceChange, 'FinalPricePercent':i.FinalPricePercent,
                'TheLeast':i.TheLeast,'TheMost':i.TheMost,'EPS':i.EPS,'PE':i.PE,'BuyCount':i.BuyCount,'BuyVolume':i.BuyVolume,
                'BuyPrice':i.BuyPrice,'SaleCount':i.SaleCount, 'SaleVolume':i.SaleVolume,'SalePrice':i.SalePrice}
            result.append(sample)
        return jsonify(result)

    @staticmethod
    def shoppingLine():
        result = []
        data = Data.query.filter(
            Data.BuyPrice == Data.TheMost, Data.BuyVolume>0).all()
        for i in data:
            sample = {'id':i.id, 'Symbol':i.Symbol, 'Name':i.Name, 'Number':i.Number, 'Volume': i.Volume,'Value':i.Value,'Yesterday':i.Yesterday,
                'First':i.First,'LastPriceValue':i.LastPriceValue, 'LastPriceChange':i.LastPriceChange, 'LastPricePercent':i.LastPricePercent,
                'FinalPriceValue':i.FinalPriceValue, 'FinalPriceChange':i.FinalPriceChange, 'FinalPricePercent':i.FinalPricePercent,
                'TheLeast':i.TheLeast,'TheMost':i.TheMost,'EPS':i.EPS,'PE':i.PE,'BuyCount':i.BuyCount,'BuyVolume':i.BuyVolume,
                'BuyPrice':i.BuyPrice,'SaleCount':i.SaleCount, 'SaleVolume':i.SaleVolume,'SalePrice':i.SalePrice}
            result.append(sample)
        return jsonify(result)

    @staticmethod
    def salesLine():
        result = []
        data = Data.query.filter(
            Data.SalePrice == Data.TheLeast, Data.SaleVolume>0).all()
        for i in data:
            sample = {'id':i.id, 'Symbol':i.Symbol, 'Name':i.Name, 'Number':i.Number, 'Volume': i.Volume,'Value':i.Value,'Yesterday':i.Yesterday,
                'First':i.First,'LastPriceValue':i.LastPriceValue, 'LastPriceChange':i.LastPriceChange, 'LastPricePercent':i.LastPricePercent,
                'FinalPriceValue':i.FinalPriceValue, 'FinalPriceChange':i.FinalPriceChange, 'FinalPricePercent':i.FinalPricePercent,
                'TheLeast':i.TheLeast,'TheMost':i.TheMost,'EPS':i.EPS,'PE':i.PE,'BuyCount':i.BuyCount,'BuyVolume':i.BuyVolume,
                'BuyPrice':i.BuyPrice,'SaleCount':i.SaleCount, 'SaleVolume':i.SaleVolume,'SalePrice':i.SalePrice}
            result.append(sample)
        return jsonify(result)