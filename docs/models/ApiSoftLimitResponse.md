# openapi_client.model.api_soft_limit_response.ApiSoftLimitResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Stock** | decimal.Decimal, int, float,  | decimal.Decimal,  | 現物のワンショット上限&lt;br&gt;※単位は万円 | [optional] value must be a 64 bit float
**Margin** | decimal.Decimal, int, float,  | decimal.Decimal,  | 信用のワンショット上限&lt;br&gt;※単位は万円 | [optional] value must be a 64 bit float
**Future** | decimal.Decimal, int, float,  | decimal.Decimal,  | 先物のワンショット上限&lt;br&gt;※単位は枚 | [optional] value must be a 64 bit float
**FutureMini** | decimal.Decimal, int, float,  | decimal.Decimal,  | 先物ミニのワンショット上限&lt;br&gt;※単位は枚 | [optional] value must be a 64 bit float
**Option** | decimal.Decimal, int, float,  | decimal.Decimal,  | オプションのワンショット上限&lt;br&gt;※単位は枚 | [optional] value must be a 64 bit float
**KabuSVersion** | str,  | str,  | kabuステーションのバージョン | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

