# openapi_client.model.wallet_option_success.WalletOptionSuccess

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**OptionBuyTradeLimit** | decimal.Decimal, int, float,  | decimal.Decimal,  | 買新規建玉可能額 | [optional] value must be a 64 bit float
**OptionSellTradeLimit** | decimal.Decimal, int, float,  | decimal.Decimal,  | 売新規建玉可能額 | [optional] value must be a 64 bit float
**MarginRequirement** | decimal.Decimal, int, float,  | decimal.Decimal,  | 必要証拠金額&lt;br&gt;※銘柄指定の場合のみ。&lt;br&gt;※銘柄が指定されなかった場合、空を返す。 | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

