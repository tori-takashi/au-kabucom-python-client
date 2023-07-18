# openapi_client.model.ranking_by_trade_volume_response.RankingByTradeVolumeResponse

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
**Trend** | str,  | str,  | トレンド &lt;table&gt;     &lt;thead&gt;         &lt;tr&gt;             &lt;th&gt;定義値&lt;/th&gt;             &lt;th&gt;内容&lt;/th&gt;         &lt;/tr&gt;     &lt;/thead&gt;     &lt;tbody&gt;         &lt;tr&gt;             &lt;td&gt;0&lt;/td&gt;             &lt;td&gt;対象データ無し&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;1&lt;/td&gt;             &lt;td&gt;過去10営業日より20位以上上昇&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;2&lt;/td&gt;             &lt;td&gt;過去10営業日より1～19位上昇&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;3&lt;/td&gt;             &lt;td&gt;過去10営業日と変わらず&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;4&lt;/td&gt;             &lt;td&gt;過去10営業日より1～19位下落&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;5&lt;/td&gt;             &lt;td&gt;過去10営業日より20位以上下落&lt;/td&gt;         &lt;/tr&gt;     &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**AverageRanking** | decimal.Decimal, int, float,  | decimal.Decimal,  | 平均順位&lt;br&gt;※100位以下は「999」となります | [optional] value must be a 64 bit float
**Symbol** | str,  | str,  | 銘柄コード | [optional] 
**SymbolName** | str,  | str,  | 銘柄名称 | [optional] 
**CurrentPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | 現在値 | [optional] value must be a 64 bit float
**ChangeRatio** | decimal.Decimal, int, float,  | decimal.Decimal,  | 前日比 | [optional] value must be a 64 bit float
**RapidTradePercentage** | decimal.Decimal, int, float,  | decimal.Decimal,  | 売買高急増（％） | [optional] value must be a 64 bit float
**TradingVolume** | decimal.Decimal, int, float,  | decimal.Decimal,  | 売買高&lt;br&gt;売買高を千株単位で表示する&lt;br&gt;※百株の位を四捨五入 | [optional] value must be a 64 bit float
**CurrentPriceTime** | str,  | str,  | 時刻&lt;br&gt;HH:mm&lt;br&gt;※日付は返しません | [optional] 
**ChangePercentage** | decimal.Decimal, int, float,  | decimal.Decimal,  | 騰落率（%） | [optional] value must be a 64 bit float
**ExchangeName** | str,  | str,  | 市場名 | [optional] 
**CategoryName** | str,  | str,  | 業種名 | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

