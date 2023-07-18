# openapi_client.model.unregister_all_success.UnregisterAllSuccess

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[RegistList](#RegistList)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 現在登録されている銘柄のリスト&lt;br&gt;※銘柄登録解除が正常に行われれば、空リストを返します。&lt;br&gt;　登録解除でエラー等が発生した場合、現在登録されている銘柄のリストを返します | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# RegistList

現在登録されている銘柄のリスト<br>※銘柄登録解除が正常に行われれば、空リストを返します。<br>　登録解除でエラー等が発生した場合、現在登録されている銘柄のリストを返します

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 現在登録されている銘柄のリスト&lt;br&gt;※銘柄登録解除が正常に行われれば、空リストを返します。&lt;br&gt;　登録解除でエラー等が発生した場合、現在登録されている銘柄のリストを返します | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

