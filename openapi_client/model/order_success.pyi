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


class OrderSuccess(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            Result = schemas.Int32Schema
            OrderId = schemas.StrSchema
            __annotations__ = {
                "Result": Result,
                "OrderId": OrderId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Result"]) -> MetaOapg.properties.Result: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OrderId"]) -> MetaOapg.properties.OrderId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Result", "OrderId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Result"]) -> typing.Union[MetaOapg.properties.Result, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OrderId"]) -> typing.Union[MetaOapg.properties.OrderId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Result", "OrderId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Result: typing.Union[MetaOapg.properties.Result, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        OrderId: typing.Union[MetaOapg.properties.OrderId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrderSuccess':
        return super().__new__(
            cls,
            *_args,
            Result=Result,
            OrderId=OrderId,
            _configuration=_configuration,
            **kwargs,
        )
