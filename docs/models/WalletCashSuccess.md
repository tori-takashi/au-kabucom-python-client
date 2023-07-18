# openapi_client.model.wallet_cash_success.WalletCashSuccess

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**StockAccountWallet** | decimal.Decimal, int, float,  | decimal.Decimal,  | 現物買付可能額&lt;br&gt; ※auマネーコネクトが有効の場合、auじぶん銀行の残高を含めた合計可能額を表示する&lt;br&gt; ※auマネーコネクトが無効の場合、auカブコム証券の可能額のみを表示する | [optional] value must be a 64 bit float
**AuKCStockAccountWallet** | decimal.Decimal, int, float,  | decimal.Decimal,  | うち、auカブコム証券可能額 | [optional] value must be a 64 bit float
**AuJbnStockAccountWallet** | decimal.Decimal, int, float,  | decimal.Decimal,  | うち、auじぶん銀行残高&lt;br&gt;※auマネーコネクトが無効の場合、「0」を表示する | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

