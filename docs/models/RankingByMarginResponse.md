# openapi_client.model.ranking_by_margin_response.RankingByMarginResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Type** | str,  | str,  | 種別 | [optional] 
**ExchangeDivision** | str,  | str,  | 市場 | [optional] 
**[Ranking](#Ranking)** | list, tuple,  | tuple,  | ランキング | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Ranking

ランキング

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | ランキング | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**false** | decimal.Decimal, int,  | decimal.Decimal,  | 順位&lt;br&gt;※ランキング内で同じ順位が返却される場合があります（10位が2件など） | [optional] value must be a 32 bit integer
**Symbol** | str,  | str,  | 銘柄コード | [optional] 
**SymbolName** | str,  | str,  | 銘柄名称 | [optional] 
**SellRapidPaymentPercentage** | decimal.Decimal, int, float,  | decimal.Decimal,  | 売残（千株） | [optional] value must be a 64 bit float
**SellLastWeekRatio** | decimal.Decimal, int, float,  | decimal.Decimal,  | 売残前週比 | [optional] value must be a 64 bit float
**BuyRapidPaymentPercentage** | decimal.Decimal, int, float,  | decimal.Decimal,  | 買残（千株） | [optional] value must be a 64 bit float
**BuyLastWeekRatio** | decimal.Decimal, int, float,  | decimal.Decimal,  | 買残前週比 | [optional] value must be a 64 bit float
**Ratio** | decimal.Decimal, int, float,  | decimal.Decimal,  | 倍率 | [optional] value must be a 64 bit float
**ExchangeName** | str,  | str,  | 市場名 | [optional] 
**CategoryName** | str,  | str,  | 業種名 | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

