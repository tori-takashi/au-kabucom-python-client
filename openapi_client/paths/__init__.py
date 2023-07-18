# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    TOKEN = "/token"
    SENDORDER = "/sendorder"
    SENDORDER_FUTURE = "/sendorder/future"
    SENDORDER_OPTION = "/sendorder/option"
    CANCELORDER = "/cancelorder"
    WALLET_CASH = "/wallet/cash"
    WALLET_CASH_SYMBOL = "/wallet/cash/{symbol}"
    WALLET_MARGIN = "/wallet/margin"
    WALLET_MARGIN_SYMBOL = "/wallet/margin/{symbol}"
    WALLET_FUTURE = "/wallet/future"
    WALLET_FUTURE_SYMBOL = "/wallet/future/{symbol}"
    WALLET_OPTION = "/wallet/option"
    WALLET_OPTION_SYMBOL = "/wallet/option/{symbol}"
    BOARD_SYMBOL = "/board/{symbol}"
    SYMBOL_SYMBOL = "/symbol/{symbol}"
    ORDERS = "/orders"
    POSITIONS = "/positions"
    REGISTER = "/register"
    UNREGISTER = "/unregister"
    UNREGISTER_ALL = "/unregister/all"
    SYMBOLNAME_FUTURE = "/symbolname/future"
    SYMBOLNAME_OPTION = "/symbolname/option"
    RANKING = "/ranking"
    EXCHANGE_SYMBOL = "/exchange/{symbol}"
    REGULATIONS_SYMBOL = "/regulations/{symbol}"
    PRIMARYEXCHANGE_SYMBOL = "/primaryexchange/{symbol}"
    APISOFTLIMIT = "/apisoftlimit"
    MARGIN_MARGINPREMIUM_SYMBOL = "/margin/marginpremium/{symbol}"
