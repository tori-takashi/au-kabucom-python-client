# openapi_client.model.margin_premium_response.MarginPremiumResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Symbol** | str,  | str,  | 銘柄コード | [optional] 
**[GeneralMargin](#GeneralMargin)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 一般信用（長期） | [optional] 
**[DayTrade](#DayTrade)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 一般信用（デイトレ） | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# GeneralMargin

一般信用（長期）

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 一般信用（長期） | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**MarginPremiumType** | decimal.Decimal, int,  | decimal.Decimal,  | プレミアム料入力区分 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;null&lt;/td&gt;           &lt;td&gt;一般信用（長期）非対応銘柄&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0&lt;/td&gt;           &lt;td&gt;プレミアム料がない銘柄&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;プレミアム料が固定の銘柄&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;プレミアム料が入札で決定する銘柄&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] value must be a 32 bit integer
**MarginPremium** | decimal.Decimal, int, float,  | decimal.Decimal,  | 確定プレミアム料&lt;br&gt; ※入札銘柄の場合、入札受付中は随時更新します。受付時間外は、確定したプレミアム料を返します。&lt;br&gt; ※非入札銘柄の場合、常に固定値を返します。&lt;br&gt; ※信用取引不可の場合、nullを返します。&lt;br&gt; ※19:30~翌営業日のプレミアム料になります。 | [optional] value must be a 64 bit float
**UpperMarginPremium** | decimal.Decimal, int, float,  | decimal.Decimal,  | 上限プレミアム料&lt;br&gt; ※プレミアム料がない場合は、nullを返します。 | [optional] value must be a 64 bit float
**LowerMarginPremium** | decimal.Decimal, int, float,  | decimal.Decimal,  | 下限プレミアム料&lt;br&gt; ※プレミアム料がない場合は、nullを返します。 | [optional] value must be a 64 bit float
**TickMarginPremium** | decimal.Decimal, int, float,  | decimal.Decimal,  | プレミアム料刻値&lt;br&gt; ※入札可能銘柄以外は、nullを返します。 | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# DayTrade

一般信用（デイトレ）

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 一般信用（デイトレ） | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**MarginPremiumType** | decimal.Decimal, int,  | decimal.Decimal,  | プレミアム料入力区分 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;null&lt;/td&gt;           &lt;td&gt;一般信用（デイトレ）非対応銘柄&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0&lt;/td&gt;           &lt;td&gt;プレミアム料がない銘柄&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;プレミアム料が固定の銘柄&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;プレミアム料が入札で決定する銘柄&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] value must be a 32 bit integer
**MarginPremium** | decimal.Decimal, int, float,  | decimal.Decimal,  | 確定プレミアム料&lt;br&gt; ※入札銘柄の場合、入札受付中は随時更新します。受付時間外は、確定したプレミアム料を返します。&lt;br&gt; ※非入札銘柄の場合、常に固定値を返します。&lt;br&gt; ※信用取引不可の場合、nullを返します。&lt;br&gt; ※19:30~翌営業日のプレミアム料になります。 | [optional] value must be a 64 bit float
**UpperMarginPremium** | decimal.Decimal, int, float,  | decimal.Decimal,  | 上限プレミアム料&lt;br&gt; ※プレミアム料がない場合は、nullを返します。 | [optional] value must be a 64 bit float
**LowerMarginPremium** | decimal.Decimal, int, float,  | decimal.Decimal,  | 下限プレミアム料&lt;br&gt; ※プレミアム料がない場合は、nullを返します。 | [optional] value must be a 64 bit float
**TickMarginPremium** | decimal.Decimal, int, float,  | decimal.Decimal,  | プレミアム料刻値&lt;br&gt; ※入札可能銘柄以外は、nullを返します。 | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

