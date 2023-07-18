import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.auth_api import AuthApi
from openapi_client.apis.tags.order_api import OrderApi
from openapi_client.apis.tags.wallet_api import WalletApi
from openapi_client.apis.tags.info_api import InfoApi
from openapi_client.apis.tags.register_api import RegisterApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTH: AuthApi,
        TagValues.ORDER: OrderApi,
        TagValues.WALLET: WalletApi,
        TagValues.INFO: InfoApi,
        TagValues.REGISTER: RegisterApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTH: AuthApi,
        TagValues.ORDER: OrderApi,
        TagValues.WALLET: WalletApi,
        TagValues.INFO: InfoApi,
        TagValues.REGISTER: RegisterApi,
    }
)
