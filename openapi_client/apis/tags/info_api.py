# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)  # noqa: E501

    The version of the OpenAPI document: 1.5
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.apisoftlimit.get import ApisoftlimitGet
from openapi_client.paths.board_symbol.get import BoardGet
from openapi_client.paths.exchange_symbol.get import ExchangeGet
from openapi_client.paths.margin_marginpremium_symbol.get import MarginpremiumGet
from openapi_client.paths.orders.get import OrdersGet
from openapi_client.paths.positions.get import PositionsGet
from openapi_client.paths.primaryexchange_symbol.get import PrimaryExchangeGet
from openapi_client.paths.ranking.get import RankingGet
from openapi_client.paths.regulations_symbol.get import RegulationsGet
from openapi_client.paths.symbol_symbol.get import SymbolGet
from openapi_client.paths.symbolname_future.get import SymbolnameFutureGet
from openapi_client.paths.symbolname_option.get import SymbolnameOptionGet


class InfoApi(
    ApisoftlimitGet,
    BoardGet,
    ExchangeGet,
    MarginpremiumGet,
    OrdersGet,
    PositionsGet,
    PrimaryExchangeGet,
    RankingGet,
    RegulationsGet,
    SymbolGet,
    SymbolnameFutureGet,
    SymbolnameOptionGet,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
