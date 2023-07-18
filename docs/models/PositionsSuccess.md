# openapi_client.model.positions_success.PositionsSuccess

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ExecutionID** | str,  | str,  | 約定番号&lt;br&gt;※現物取引では、nullが返ります。 | [optional] 
**AccountType** | decimal.Decimal, int,  | decimal.Decimal,  | 口座種別 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;一般&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;特定&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;12&lt;/td&gt;           &lt;td&gt;法人&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] value must be a 32 bit integer
**Symbol** | str,  | str,  | 銘柄コード | [optional] 
**SymbolName** | str,  | str,  | 銘柄名 | [optional] 
**Exchange** | decimal.Decimal, int,  | decimal.Decimal,  | 市場コード &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;東証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;名証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;福証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;札証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;日通し&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;23&lt;/td&gt;           &lt;td&gt;日中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;24&lt;/td&gt;           &lt;td&gt;夜間&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] value must be a 32 bit integer
**ExchangeName** | str,  | str,  | 市場名 | [optional] 
**SecurityType** | decimal.Decimal, int,  | decimal.Decimal,  | 銘柄種別&lt;br&gt;※先物・オプション銘柄の場合のみ | [optional] value must be a 32 bit integer
**ExecutionDay** | decimal.Decimal, int,  | decimal.Decimal,  | 約定日（建玉日）&lt;br&gt;※信用・先物・オプションの場合のみ&lt;br&gt;※現物取引では、nullが返ります。 | [optional] value must be a 32 bit integer
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段 | [optional] value must be a 64 bit float
**LeavesQty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 残数量（保有数量） | [optional] value must be a 64 bit float
**HoldQty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 拘束数量（返済のために拘束されている数量） | [optional] value must be a 64 bit float
**Side** | str,  | str,  | 売買区分 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;売&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;買&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**Expenses** | decimal.Decimal, int, float,  | decimal.Decimal,  | 諸経費&lt;br&gt;※信用・先物・オプションの場合のみ | [optional] value must be a 64 bit float
**Commission** | decimal.Decimal, int, float,  | decimal.Decimal,  | 手数料&lt;br&gt;※信用・先物・オプションの場合のみ | [optional] value must be a 64 bit float
**CommissionTax** | decimal.Decimal, int, float,  | decimal.Decimal,  | 手数料消費税&lt;br&gt;※信用・先物・オプションの場合のみ | [optional] value must be a 64 bit float
**ExpireDay** | decimal.Decimal, int,  | decimal.Decimal,  | 返済期日&lt;br&gt;※信用・先物・オプションの場合のみ | [optional] value must be a 32 bit integer
**MarginTradeType** | decimal.Decimal, int,  | decimal.Decimal,  | 信用取引区分&lt;br&gt;※信用の場合のみ &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;制度信用&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;一般信用（長期）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;一般信用（デイトレ）&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] value must be a 32 bit integer
**CurrentPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | 現在値&lt;br&gt;追加情報出力フラグ：falseの場合、null | [optional] value must be a 64 bit float
**Valuation** | decimal.Decimal, int, float,  | decimal.Decimal,  | 評価金額&lt;br&gt;追加情報出力フラグ：falseの場合、null | [optional] value must be a 64 bit float
**ProfitLoss** | decimal.Decimal, int, float,  | decimal.Decimal,  | 評価損益額&lt;br&gt;追加情報出力フラグ：falseの場合、null | [optional] value must be a 64 bit float
**ProfitLossRate** | decimal.Decimal, int, float,  | decimal.Decimal,  | 評価損益率&lt;br&gt;追加情報出力フラグ：falseの場合、null | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

