# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.model.api_soft_limit_response import ApiSoftLimitResponse
from openapi_client.model.board_success import BoardSuccess
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.exchange_response import ExchangeResponse
from openapi_client.model.margin_premium_response import MarginPremiumResponse
from openapi_client.model.order_success import OrderSuccess
from openapi_client.model.orders_success import OrdersSuccess
from openapi_client.model.positions import Positions
from openapi_client.model.positions_deriv import PositionsDeriv
from openapi_client.model.positions_success import PositionsSuccess
from openapi_client.model.primary_exchange_response import PrimaryExchangeResponse
from openapi_client.model.ranking_by_category_response import RankingByCategoryResponse
from openapi_client.model.ranking_by_margin_response import RankingByMarginResponse
from openapi_client.model.ranking_by_tick_count_response import RankingByTickCountResponse
from openapi_client.model.ranking_by_trade_value_response import RankingByTradeValueResponse
from openapi_client.model.ranking_by_trade_volume_response import RankingByTradeVolumeResponse
from openapi_client.model.ranking_default_response import RankingDefaultResponse
from openapi_client.model.regist_success import RegistSuccess
from openapi_client.model.regulations_response import RegulationsResponse
from openapi_client.model.request_cancel_order import RequestCancelOrder
from openapi_client.model.request_register import RequestRegister
from openapi_client.model.request_send_order import RequestSendOrder
from openapi_client.model.request_send_order_deriv_future import RequestSendOrderDerivFuture
from openapi_client.model.request_send_order_deriv_option import RequestSendOrderDerivOption
from openapi_client.model.request_token import RequestToken
from openapi_client.model.request_unregister import RequestUnregister
from openapi_client.model.symbol_name_success import SymbolNameSuccess
from openapi_client.model.symbol_success import SymbolSuccess
from openapi_client.model.token_success import TokenSuccess
from openapi_client.model.unregister_all_success import UnregisterAllSuccess
from openapi_client.model.wallet_cash_success import WalletCashSuccess
from openapi_client.model.wallet_future_success import WalletFutureSuccess
from openapi_client.model.wallet_margin_success import WalletMarginSuccess
from openapi_client.model.wallet_option_success import WalletOptionSuccess
