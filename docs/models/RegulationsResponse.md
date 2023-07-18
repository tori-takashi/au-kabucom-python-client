# openapi_client.model.regulations_response.RegulationsResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Symbol** | str,  | str,  | 銘柄コード&lt;br&gt; ※対象商品は、株式のみ | [optional] 
**[RegulationsInfo](#RegulationsInfo)** | list, tuple,  | tuple,  | 規制情報 | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# RegulationsInfo

規制情報

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | 規制情報 | 

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
**Exchange** | decimal.Decimal, int,  | decimal.Decimal,  | 規制市場 &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;定義値&lt;/th&gt;       &lt;th&gt;内容&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;0&lt;/td&gt;       &lt;td&gt;全対象&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;1&lt;/td&gt;       &lt;td&gt;東証&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;3&lt;/td&gt;       &lt;td&gt;名証&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;5&lt;/td&gt;       &lt;td&gt;福証&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;6&lt;/td&gt;       &lt;td&gt;札証&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;9&lt;/td&gt;       &lt;td&gt;SOR&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;10&lt;/td&gt;       &lt;td&gt;CXJ&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;21&lt;/td&gt;       &lt;td&gt;JNX&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] value must be a 32 bit integer
**Product** | decimal.Decimal, int,  | decimal.Decimal,  | 規制取引区分&lt;br&gt; ※空売り規制の場合、「4：新規」 &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;定義値&lt;/th&gt;       &lt;th&gt;内容&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;0&lt;/td&gt;       &lt;td&gt;全対象&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;1&lt;/td&gt;       &lt;td&gt;現物&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;2&lt;/td&gt;       &lt;td&gt;信用新規（制度）&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;3&lt;/td&gt;       &lt;td&gt;信用新規（一般）&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;4&lt;/td&gt;       &lt;td&gt;新規&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;5&lt;/td&gt;       &lt;td&gt;信用返済（制度）&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;6&lt;/td&gt;       &lt;td&gt;信用返済（一般）&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;7&lt;/td&gt;       &lt;td&gt;返済&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;8&lt;/td&gt;       &lt;td&gt;品受&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;9&lt;/td&gt;       &lt;td&gt;品渡&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] value must be a 32 bit integer
**Side** | str,  | str,  | 規制売買&lt;br&gt; ※空売り規制の場合、「1：売」 &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;定義値&lt;/th&gt;       &lt;th&gt;内容&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;0&lt;/td&gt;       &lt;td&gt;全対象&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;1&lt;/td&gt;       &lt;td&gt;売&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;2&lt;/td&gt;       &lt;td&gt;買&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**Reason** | str,  | str,  | 理由&lt;br&gt;※空売り規制の場合、「空売り規制」 | [optional] 
**LimitStartDay** | str,  | str,  | 制限開始日&lt;br&gt;yyyy/MM/dd HH:mm形式  &lt;br&gt;※空売り規制の場合、null | [optional] 
**LimitEndDay** | str,  | str,  | 制限終了日&lt;br&gt;yyyy/MM/dd HH:mm形式  &lt;br&gt;※空売り規制の場合、null | [optional] 
**Level** | decimal.Decimal, int,  | decimal.Decimal,  | コンプライアンスレベル&lt;br&gt; ※空売り規制の場合、null &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;定義値&lt;/th&gt;       &lt;th&gt;内容&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;０&lt;/td&gt;       &lt;td&gt;規制無し&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;１&lt;/td&gt;       &lt;td&gt;ワーニング&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;２&lt;/td&gt;       &lt;td&gt;エラー&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

