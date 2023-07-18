# openapi_client.model.wallet_margin_success.WalletMarginSuccess

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**MarginAccountWallet** | decimal.Decimal, int, float,  | decimal.Decimal,  | 信用新規可能額 | [optional] value must be a 64 bit float
**DepositkeepRate** | decimal.Decimal, int, float,  | decimal.Decimal,  | 保証金維持率&lt;br&gt;※銘柄指定の場合のみ&lt;br&gt;※銘柄が指定されなかった場合、0.0を返す。 | [optional] value must be a 64 bit float
**ConsignmentDepositRate** | decimal.Decimal, int, float,  | decimal.Decimal,  | 委託保証金率&lt;br&gt;※銘柄指定の場合のみ。&lt;br&gt;※銘柄が指定されなかった場合、Noneを返す。 | [optional] value must be a 64 bit float
**CashOfConsignmentDepositRate** | decimal.Decimal, int, float,  | decimal.Decimal,  | 現金委託保証金率&lt;br&gt;※銘柄指定の場合のみ。&lt;br&gt;※銘柄が指定されなかった場合、Noneを返す。 | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

