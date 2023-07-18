# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)  # noqa: E501

    The version of the OpenAPI document: 1.5
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class PositionsSuccess(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            ExecutionID = schemas.StrSchema
            AccountType = schemas.Int32Schema
            Symbol = schemas.StrSchema
            SymbolName = schemas.StrSchema
            Exchange = schemas.Int32Schema
            ExchangeName = schemas.StrSchema
            SecurityType = schemas.Int32Schema
            ExecutionDay = schemas.Int32Schema
            Price = schemas.Float64Schema
            LeavesQty = schemas.Float64Schema
            HoldQty = schemas.Float64Schema
            Side = schemas.StrSchema
            Expenses = schemas.Float64Schema
            Commission = schemas.Float64Schema
            CommissionTax = schemas.Float64Schema
            ExpireDay = schemas.Int32Schema
            MarginTradeType = schemas.Int32Schema
            CurrentPrice = schemas.Float64Schema
            Valuation = schemas.Float64Schema
            ProfitLoss = schemas.Float64Schema
            ProfitLossRate = schemas.Float64Schema
            __annotations__ = {
                "ExecutionID": ExecutionID,
                "AccountType": AccountType,
                "Symbol": Symbol,
                "SymbolName": SymbolName,
                "Exchange": Exchange,
                "ExchangeName": ExchangeName,
                "SecurityType": SecurityType,
                "ExecutionDay": ExecutionDay,
                "Price": Price,
                "LeavesQty": LeavesQty,
                "HoldQty": HoldQty,
                "Side": Side,
                "Expenses": Expenses,
                "Commission": Commission,
                "CommissionTax": CommissionTax,
                "ExpireDay": ExpireDay,
                "MarginTradeType": MarginTradeType,
                "CurrentPrice": CurrentPrice,
                "Valuation": Valuation,
                "ProfitLoss": ProfitLoss,
                "ProfitLossRate": ProfitLossRate,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ExecutionID"]) -> MetaOapg.properties.ExecutionID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccountType"]) -> MetaOapg.properties.AccountType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Symbol"]) -> MetaOapg.properties.Symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SymbolName"]) -> MetaOapg.properties.SymbolName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Exchange"]) -> MetaOapg.properties.Exchange: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ExchangeName"]) -> MetaOapg.properties.ExchangeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SecurityType"]) -> MetaOapg.properties.SecurityType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ExecutionDay"]) -> MetaOapg.properties.ExecutionDay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Price"]) -> MetaOapg.properties.Price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LeavesQty"]) -> MetaOapg.properties.LeavesQty: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["HoldQty"]) -> MetaOapg.properties.HoldQty: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Side"]) -> MetaOapg.properties.Side: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Expenses"]) -> MetaOapg.properties.Expenses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Commission"]) -> MetaOapg.properties.Commission: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CommissionTax"]) -> MetaOapg.properties.CommissionTax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ExpireDay"]) -> MetaOapg.properties.ExpireDay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MarginTradeType"]) -> MetaOapg.properties.MarginTradeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CurrentPrice"]) -> MetaOapg.properties.CurrentPrice: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Valuation"]) -> MetaOapg.properties.Valuation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProfitLoss"]) -> MetaOapg.properties.ProfitLoss: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProfitLossRate"]) -> MetaOapg.properties.ProfitLossRate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ExecutionID", "AccountType", "Symbol", "SymbolName", "Exchange", "ExchangeName", "SecurityType", "ExecutionDay", "Price", "LeavesQty", "HoldQty", "Side", "Expenses", "Commission", "CommissionTax", "ExpireDay", "MarginTradeType", "CurrentPrice", "Valuation", "ProfitLoss", "ProfitLossRate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ExecutionID"]) -> typing.Union[MetaOapg.properties.ExecutionID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccountType"]) -> typing.Union[MetaOapg.properties.AccountType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Symbol"]) -> typing.Union[MetaOapg.properties.Symbol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SymbolName"]) -> typing.Union[MetaOapg.properties.SymbolName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Exchange"]) -> typing.Union[MetaOapg.properties.Exchange, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ExchangeName"]) -> typing.Union[MetaOapg.properties.ExchangeName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SecurityType"]) -> typing.Union[MetaOapg.properties.SecurityType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ExecutionDay"]) -> typing.Union[MetaOapg.properties.ExecutionDay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Price"]) -> typing.Union[MetaOapg.properties.Price, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LeavesQty"]) -> typing.Union[MetaOapg.properties.LeavesQty, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["HoldQty"]) -> typing.Union[MetaOapg.properties.HoldQty, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Side"]) -> typing.Union[MetaOapg.properties.Side, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Expenses"]) -> typing.Union[MetaOapg.properties.Expenses, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Commission"]) -> typing.Union[MetaOapg.properties.Commission, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CommissionTax"]) -> typing.Union[MetaOapg.properties.CommissionTax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ExpireDay"]) -> typing.Union[MetaOapg.properties.ExpireDay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MarginTradeType"]) -> typing.Union[MetaOapg.properties.MarginTradeType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CurrentPrice"]) -> typing.Union[MetaOapg.properties.CurrentPrice, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Valuation"]) -> typing.Union[MetaOapg.properties.Valuation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProfitLoss"]) -> typing.Union[MetaOapg.properties.ProfitLoss, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProfitLossRate"]) -> typing.Union[MetaOapg.properties.ProfitLossRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ExecutionID", "AccountType", "Symbol", "SymbolName", "Exchange", "ExchangeName", "SecurityType", "ExecutionDay", "Price", "LeavesQty", "HoldQty", "Side", "Expenses", "Commission", "CommissionTax", "ExpireDay", "MarginTradeType", "CurrentPrice", "Valuation", "ProfitLoss", "ProfitLossRate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        ExecutionID: typing.Union[MetaOapg.properties.ExecutionID, str, schemas.Unset] = schemas.unset,
        AccountType: typing.Union[MetaOapg.properties.AccountType, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Symbol: typing.Union[MetaOapg.properties.Symbol, str, schemas.Unset] = schemas.unset,
        SymbolName: typing.Union[MetaOapg.properties.SymbolName, str, schemas.Unset] = schemas.unset,
        Exchange: typing.Union[MetaOapg.properties.Exchange, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ExchangeName: typing.Union[MetaOapg.properties.ExchangeName, str, schemas.Unset] = schemas.unset,
        SecurityType: typing.Union[MetaOapg.properties.SecurityType, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ExecutionDay: typing.Union[MetaOapg.properties.ExecutionDay, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Price: typing.Union[MetaOapg.properties.Price, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        LeavesQty: typing.Union[MetaOapg.properties.LeavesQty, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        HoldQty: typing.Union[MetaOapg.properties.HoldQty, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        Side: typing.Union[MetaOapg.properties.Side, str, schemas.Unset] = schemas.unset,
        Expenses: typing.Union[MetaOapg.properties.Expenses, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        Commission: typing.Union[MetaOapg.properties.Commission, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        CommissionTax: typing.Union[MetaOapg.properties.CommissionTax, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        ExpireDay: typing.Union[MetaOapg.properties.ExpireDay, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        MarginTradeType: typing.Union[MetaOapg.properties.MarginTradeType, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        CurrentPrice: typing.Union[MetaOapg.properties.CurrentPrice, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        Valuation: typing.Union[MetaOapg.properties.Valuation, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        ProfitLoss: typing.Union[MetaOapg.properties.ProfitLoss, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        ProfitLossRate: typing.Union[MetaOapg.properties.ProfitLossRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PositionsSuccess':
        return super().__new__(
            cls,
            *_args,
            ExecutionID=ExecutionID,
            AccountType=AccountType,
            Symbol=Symbol,
            SymbolName=SymbolName,
            Exchange=Exchange,
            ExchangeName=ExchangeName,
            SecurityType=SecurityType,
            ExecutionDay=ExecutionDay,
            Price=Price,
            LeavesQty=LeavesQty,
            HoldQty=HoldQty,
            Side=Side,
            Expenses=Expenses,
            Commission=Commission,
            CommissionTax=CommissionTax,
            ExpireDay=ExpireDay,
            MarginTradeType=MarginTradeType,
            CurrentPrice=CurrentPrice,
            Valuation=Valuation,
            ProfitLoss=ProfitLoss,
            ProfitLossRate=ProfitLossRate,
            _configuration=_configuration,
            **kwargs,
        )
