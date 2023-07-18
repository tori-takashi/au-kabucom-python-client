# openapi_client.model.exchange_response.ExchangeResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Symbol** | str,  | str,  | 通貨 | [optional] 
**BidPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | BID | [optional] value must be a 64 bit float
**Spread** | decimal.Decimal, int, float,  | decimal.Decimal,  | SP | [optional] value must be a 64 bit float
**AskPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | ASK | [optional] value must be a 64 bit float
**Change** | decimal.Decimal, int, float,  | decimal.Decimal,  | 前日比 | [optional] value must be a 64 bit float
**Time** | str,  | str,  | 時刻 &lt;br&gt;※HH:mm:ss形式 | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

