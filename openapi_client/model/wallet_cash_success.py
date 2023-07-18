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


class WalletCashSuccess(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            StockAccountWallet = schemas.Float64Schema
            AuKCStockAccountWallet = schemas.Float64Schema
            AuJbnStockAccountWallet = schemas.Float64Schema
            __annotations__ = {
                "StockAccountWallet": StockAccountWallet,
                "AuKCStockAccountWallet": AuKCStockAccountWallet,
                "AuJbnStockAccountWallet": AuJbnStockAccountWallet,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StockAccountWallet"]) -> MetaOapg.properties.StockAccountWallet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AuKCStockAccountWallet"]) -> MetaOapg.properties.AuKCStockAccountWallet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AuJbnStockAccountWallet"]) -> MetaOapg.properties.AuJbnStockAccountWallet: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["StockAccountWallet", "AuKCStockAccountWallet", "AuJbnStockAccountWallet", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StockAccountWallet"]) -> typing.Union[MetaOapg.properties.StockAccountWallet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AuKCStockAccountWallet"]) -> typing.Union[MetaOapg.properties.AuKCStockAccountWallet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AuJbnStockAccountWallet"]) -> typing.Union[MetaOapg.properties.AuJbnStockAccountWallet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["StockAccountWallet", "AuKCStockAccountWallet", "AuJbnStockAccountWallet", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        StockAccountWallet: typing.Union[MetaOapg.properties.StockAccountWallet, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        AuKCStockAccountWallet: typing.Union[MetaOapg.properties.AuKCStockAccountWallet, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        AuJbnStockAccountWallet: typing.Union[MetaOapg.properties.AuJbnStockAccountWallet, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WalletCashSuccess':
        return super().__new__(
            cls,
            *_args,
            StockAccountWallet=StockAccountWallet,
            AuKCStockAccountWallet=AuKCStockAccountWallet,
            AuJbnStockAccountWallet=AuJbnStockAccountWallet,
            _configuration=_configuration,
            **kwargs,
        )
