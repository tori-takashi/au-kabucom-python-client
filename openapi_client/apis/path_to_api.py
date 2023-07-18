import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.token import Token
from openapi_client.apis.paths.sendorder import Sendorder
from openapi_client.apis.paths.sendorder_future import SendorderFuture
from openapi_client.apis.paths.sendorder_option import SendorderOption
from openapi_client.apis.paths.cancelorder import Cancelorder
from openapi_client.apis.paths.wallet_cash import WalletCash
from openapi_client.apis.paths.wallet_cash_symbol import WalletCashSymbol
from openapi_client.apis.paths.wallet_margin import WalletMargin
from openapi_client.apis.paths.wallet_margin_symbol import WalletMarginSymbol
from openapi_client.apis.paths.wallet_future import WalletFuture
from openapi_client.apis.paths.wallet_future_symbol import WalletFutureSymbol
from openapi_client.apis.paths.wallet_option import WalletOption
from openapi_client.apis.paths.wallet_option_symbol import WalletOptionSymbol
from openapi_client.apis.paths.board_symbol import BoardSymbol
from openapi_client.apis.paths.symbol_symbol import SymbolSymbol
from openapi_client.apis.paths.orders import Orders
from openapi_client.apis.paths.positions import Positions
from openapi_client.apis.paths.register import Register
from openapi_client.apis.paths.unregister import Unregister
from openapi_client.apis.paths.unregister_all import UnregisterAll
from openapi_client.apis.paths.symbolname_future import SymbolnameFuture
from openapi_client.apis.paths.symbolname_option import SymbolnameOption
from openapi_client.apis.paths.ranking import Ranking
from openapi_client.apis.paths.exchange_symbol import ExchangeSymbol
from openapi_client.apis.paths.regulations_symbol import RegulationsSymbol
from openapi_client.apis.paths.primaryexchange_symbol import PrimaryexchangeSymbol
from openapi_client.apis.paths.apisoftlimit import Apisoftlimit
from openapi_client.apis.paths.margin_marginpremium_symbol import MarginMarginpremiumSymbol

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.TOKEN: Token,
        PathValues.SENDORDER: Sendorder,
        PathValues.SENDORDER_FUTURE: SendorderFuture,
        PathValues.SENDORDER_OPTION: SendorderOption,
        PathValues.CANCELORDER: Cancelorder,
        PathValues.WALLET_CASH: WalletCash,
        PathValues.WALLET_CASH_SYMBOL: WalletCashSymbol,
        PathValues.WALLET_MARGIN: WalletMargin,
        PathValues.WALLET_MARGIN_SYMBOL: WalletMarginSymbol,
        PathValues.WALLET_FUTURE: WalletFuture,
        PathValues.WALLET_FUTURE_SYMBOL: WalletFutureSymbol,
        PathValues.WALLET_OPTION: WalletOption,
        PathValues.WALLET_OPTION_SYMBOL: WalletOptionSymbol,
        PathValues.BOARD_SYMBOL: BoardSymbol,
        PathValues.SYMBOL_SYMBOL: SymbolSymbol,
        PathValues.ORDERS: Orders,
        PathValues.POSITIONS: Positions,
        PathValues.REGISTER: Register,
        PathValues.UNREGISTER: Unregister,
        PathValues.UNREGISTER_ALL: UnregisterAll,
        PathValues.SYMBOLNAME_FUTURE: SymbolnameFuture,
        PathValues.SYMBOLNAME_OPTION: SymbolnameOption,
        PathValues.RANKING: Ranking,
        PathValues.EXCHANGE_SYMBOL: ExchangeSymbol,
        PathValues.REGULATIONS_SYMBOL: RegulationsSymbol,
        PathValues.PRIMARYEXCHANGE_SYMBOL: PrimaryexchangeSymbol,
        PathValues.APISOFTLIMIT: Apisoftlimit,
        PathValues.MARGIN_MARGINPREMIUM_SYMBOL: MarginMarginpremiumSymbol,
    }
)

path_to_api = PathToApi(
    {
        PathValues.TOKEN: Token,
        PathValues.SENDORDER: Sendorder,
        PathValues.SENDORDER_FUTURE: SendorderFuture,
        PathValues.SENDORDER_OPTION: SendorderOption,
        PathValues.CANCELORDER: Cancelorder,
        PathValues.WALLET_CASH: WalletCash,
        PathValues.WALLET_CASH_SYMBOL: WalletCashSymbol,
        PathValues.WALLET_MARGIN: WalletMargin,
        PathValues.WALLET_MARGIN_SYMBOL: WalletMarginSymbol,
        PathValues.WALLET_FUTURE: WalletFuture,
        PathValues.WALLET_FUTURE_SYMBOL: WalletFutureSymbol,
        PathValues.WALLET_OPTION: WalletOption,
        PathValues.WALLET_OPTION_SYMBOL: WalletOptionSymbol,
        PathValues.BOARD_SYMBOL: BoardSymbol,
        PathValues.SYMBOL_SYMBOL: SymbolSymbol,
        PathValues.ORDERS: Orders,
        PathValues.POSITIONS: Positions,
        PathValues.REGISTER: Register,
        PathValues.UNREGISTER: Unregister,
        PathValues.UNREGISTER_ALL: UnregisterAll,
        PathValues.SYMBOLNAME_FUTURE: SymbolnameFuture,
        PathValues.SYMBOLNAME_OPTION: SymbolnameOption,
        PathValues.RANKING: Ranking,
        PathValues.EXCHANGE_SYMBOL: ExchangeSymbol,
        PathValues.REGULATIONS_SYMBOL: RegulationsSymbol,
        PathValues.PRIMARYEXCHANGE_SYMBOL: PrimaryexchangeSymbol,
        PathValues.APISOFTLIMIT: Apisoftlimit,
        PathValues.MARGIN_MARGINPREMIUM_SYMBOL: MarginMarginpremiumSymbol,
    }
)
