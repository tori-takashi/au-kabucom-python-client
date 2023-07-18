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


class WalletOptionSuccess(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            OptionBuyTradeLimit = schemas.Float64Schema
            OptionSellTradeLimit = schemas.Float64Schema
            MarginRequirement = schemas.Float64Schema
            __annotations__ = {
                "OptionBuyTradeLimit": OptionBuyTradeLimit,
                "OptionSellTradeLimit": OptionSellTradeLimit,
                "MarginRequirement": MarginRequirement,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OptionBuyTradeLimit"]) -> MetaOapg.properties.OptionBuyTradeLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OptionSellTradeLimit"]) -> MetaOapg.properties.OptionSellTradeLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MarginRequirement"]) -> MetaOapg.properties.MarginRequirement: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["OptionBuyTradeLimit", "OptionSellTradeLimit", "MarginRequirement", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OptionBuyTradeLimit"]) -> typing.Union[MetaOapg.properties.OptionBuyTradeLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OptionSellTradeLimit"]) -> typing.Union[MetaOapg.properties.OptionSellTradeLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MarginRequirement"]) -> typing.Union[MetaOapg.properties.MarginRequirement, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["OptionBuyTradeLimit", "OptionSellTradeLimit", "MarginRequirement", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        OptionBuyTradeLimit: typing.Union[MetaOapg.properties.OptionBuyTradeLimit, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        OptionSellTradeLimit: typing.Union[MetaOapg.properties.OptionSellTradeLimit, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        MarginRequirement: typing.Union[MetaOapg.properties.MarginRequirement, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WalletOptionSuccess':
        return super().__new__(
            cls,
            *_args,
            OptionBuyTradeLimit=OptionBuyTradeLimit,
            OptionSellTradeLimit=OptionSellTradeLimit,
            MarginRequirement=MarginRequirement,
            _configuration=_configuration,
            **kwargs,
        )