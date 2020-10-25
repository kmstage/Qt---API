import  pandas as pd
from FilterAPI import db
from FilterAPI.models import Data

df = pd.read_excel('MarketWatch.xlsx', 0)


for index, (Symbol,Name,Number,Volume,Value,Yesterday,
        First,LastPriceValue,LastPriceChange,LastPricePercent,
        FinalPriceValue,FinalPriceChange,FinalPricePercent,
        TheLeast,TheMost,EPS,PE,BuyCount,BuyVolume,
        BuyPrice,SaleCount,SaleVolume,SalePrice) in df.iterrows():
    if index>0:
        data = Data()
        data.Symbol = Symbol
        data.Name = Name
        data.Number = Number
        data.Volume = Volume
        data.Value = Value
        data.Yesterday = Yesterday
        data.First = First
        data.LastPriceValue = LastPriceValue
        data.LastPriceChange = LastPriceChange
        data.LastPricePercent = LastPricePercent
        data.FinalPriceValue = FinalPriceValue
        data.FinalPriceChange = FinalPriceChange
        data.FinalPricePercent = FinalPricePercent
        data.TheLeast = TheLeast
        data.TheMost = TheMost
        data.EPS = EPS
        data.PE = PE
        data.BuyCount = BuyCount
        data.BuyVolume = BuyVolume
        data.BuyPrice = BuyPrice
        data.SaleCount = SaleCount
        data.SaleVolume = SaleVolume
        data.SalePrice = SalePrice
        db.session.add(data)

db.session.commit()
