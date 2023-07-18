# coding: utf-8

"""
    kabuステーションAPI

    # 定義情報   REST APIのコード一覧、エンドポイントは下記リンク参照     - [REST APIコード一覧](../ptal/error.html)  # noqa: E501

    The version of the OpenAPI document: 1.5
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.wallet_cash.get import WalletCashGet
from openapi_client.paths.wallet_cash_symbol.get import WalletCashSymbolGet
from openapi_client.paths.wallet_future.get import WalletFutureGet
from openapi_client.paths.wallet_future_symbol.get import WalletFutureSymbolGet
from openapi_client.paths.wallet_margin.get import WalletMarginGet
from openapi_client.paths.wallet_margin_symbol.get import WalletMarginSymbolGet
from openapi_client.paths.wallet_option.get import WalletOptionGet
from openapi_client.paths.wallet_option_symbol.get import WalletOptionSymbolGet


class WalletApi(
    WalletCashGet,
    WalletCashSymbolGet,
    WalletFutureGet,
    WalletFutureSymbolGet,
    WalletMarginGet,
    WalletMarginSymbolGet,
    WalletOptionGet,
    WalletOptionSymbolGet,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass