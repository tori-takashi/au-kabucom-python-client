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


class WalletMarginSuccess(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            MarginAccountWallet = schemas.Float64Schema
            DepositkeepRate = schemas.Float64Schema
            ConsignmentDepositRate = schemas.Float64Schema
            CashOfConsignmentDepositRate = schemas.Float64Schema
            __annotations__ = {
                "MarginAccountWallet": MarginAccountWallet,
                "DepositkeepRate": DepositkeepRate,
                "ConsignmentDepositRate": ConsignmentDepositRate,
                "CashOfConsignmentDepositRate": CashOfConsignmentDepositRate,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MarginAccountWallet"]) -> MetaOapg.properties.MarginAccountWallet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DepositkeepRate"]) -> MetaOapg.properties.DepositkeepRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ConsignmentDepositRate"]) -> MetaOapg.properties.ConsignmentDepositRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CashOfConsignmentDepositRate"]) -> MetaOapg.properties.CashOfConsignmentDepositRate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["MarginAccountWallet", "DepositkeepRate", "ConsignmentDepositRate", "CashOfConsignmentDepositRate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MarginAccountWallet"]) -> typing.Union[MetaOapg.properties.MarginAccountWallet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DepositkeepRate"]) -> typing.Union[MetaOapg.properties.DepositkeepRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ConsignmentDepositRate"]) -> typing.Union[MetaOapg.properties.ConsignmentDepositRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CashOfConsignmentDepositRate"]) -> typing.Union[MetaOapg.properties.CashOfConsignmentDepositRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["MarginAccountWallet", "DepositkeepRate", "ConsignmentDepositRate", "CashOfConsignmentDepositRate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        MarginAccountWallet: typing.Union[MetaOapg.properties.MarginAccountWallet, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        DepositkeepRate: typing.Union[MetaOapg.properties.DepositkeepRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        ConsignmentDepositRate: typing.Union[MetaOapg.properties.ConsignmentDepositRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        CashOfConsignmentDepositRate: typing.Union[MetaOapg.properties.CashOfConsignmentDepositRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WalletMarginSuccess':
        return super().__new__(
            cls,
            *_args,
            MarginAccountWallet=MarginAccountWallet,
            DepositkeepRate=DepositkeepRate,
            ConsignmentDepositRate=ConsignmentDepositRate,
            CashOfConsignmentDepositRate=CashOfConsignmentDepositRate,
            _configuration=_configuration,
            **kwargs,
        )
