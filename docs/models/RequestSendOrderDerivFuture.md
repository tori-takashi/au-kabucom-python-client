# openapi_client.model.request_send_order_deriv_future.RequestSendOrderDerivFuture

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Exchange** | decimal.Decimal, int,  | decimal.Decimal,  | 市場コード &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;日通し&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;23&lt;/td&gt;           &lt;td&gt;日中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;24&lt;/td&gt;           &lt;td&gt;夜間&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | value must be a 32 bit integer
**Side** | str,  | str,  | 売買区分 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;売&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;買&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | 
**FrontOrderType** | decimal.Decimal, int,  | decimal.Decimal,  | 執行条件 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;           &lt;th&gt;”Price”の指定&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;18&lt;/td&gt;           &lt;td&gt;引成（派生）&lt;br&gt;※TimeInForceは、「FAK」のみ有効&lt;/td&gt;           &lt;td&gt;0&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;20&lt;/td&gt;           &lt;td&gt;指値&lt;/td&gt;           &lt;td&gt;発注したい金額&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;28&lt;/td&gt;           &lt;td&gt;引指（派生）&lt;br&gt;※TimeInForceは、「FAS」のみ有効&lt;/td&gt;           &lt;td&gt;発注したい金額&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;30&lt;/td&gt;           &lt;td&gt;逆指値&lt;/td&gt;           &lt;td&gt;指定なし&lt;br&gt;※AfterHitPriceで指定ください&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;120&lt;/td&gt;           &lt;td&gt;成行（マーケットオーダー）&lt;/td&gt;           &lt;td&gt;0&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | value must be a 32 bit integer
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 注文価格&lt;br&gt;※FrontOrderTypeで成行を指定した場合、0を指定する。&lt;br&gt;※詳細について、”FrontOrderType”をご確認ください。 | value must be a 64 bit float
**ExpireDay** | decimal.Decimal, int,  | decimal.Decimal,  | 注文有効期限&lt;br&gt; yyyyMMdd形式。&lt;br&gt; 「0」を指定すると、kabuステーション上の発注画面の「本日」に対応する日付として扱います。&lt;br&gt; 「本日」は直近の注文可能日となり、以下のように設定されます。&lt;br&gt; その市場の引けまでの間 : 当日&lt;br&gt; その市場の引け後       : 翌取引所営業日&lt;br&gt; その市場の休前日       : 休日明けの取引所営業日&lt;br&gt; ※ 日替わりはkabuステーションが日付変更通知を受信したタイミングです。&lt;br&gt; ※ 日通しの場合、夜間取引の引け後に日付が更新されます。 | value must be a 32 bit integer
**Symbol** | str,  | str,  | 銘柄コード&lt;br&gt;※取引最終日に「先物銘柄コード取得」でDerivMonthに0（直近限月）を指定した場合、日中・夜間の時間帯に関わらず、取引最終日を迎える限月の銘柄コードを返します。取引最終日を迎える銘柄の取引は日中取引をもって終了となりますので、ご注意ください。 | 
**Qty** | decimal.Decimal, int,  | decimal.Decimal,  | 注文数量 | value must be a 32 bit integer
**TimeInForce** | decimal.Decimal, int,  | decimal.Decimal,  | 有効期間条件 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;FAS&lt;br&gt;※逆指値注文以外の場合、FASを指定した場合、FrontOrderTypeは指値(20)のみ指定可能。&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;FAK&lt;br&gt;※逆指値注文以外の場合、FAKを指定した場合、Exchangeは日中(23)、夜間(24)のみ指定可能。&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;FOK&lt;br&gt;※逆指値注文以外の場合、FOKを指定した場合、Exchangeは日中(23)、夜間(24)のみ指定可能。&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | value must be a 32 bit integer
**TradeType** | decimal.Decimal, int,  | decimal.Decimal,  | 取引区分 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;新規&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;返済&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | value must be a 32 bit integer
**Password** | str,  | str,  | 注文パスワード | 
**ClosePositionOrder** | decimal.Decimal, int,  | decimal.Decimal,  | 決済順序&lt;br&gt;※ClosePositionOrderとClosePositionsはどちらか一方のみ指定可能。&lt;br&gt;※ClosePositionOrderとClosePositionsを両方指定した場合、エラー。 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;0&lt;/td&gt;           &lt;td&gt;日付（古い順）、損益（高い順）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;日付（古い順）、損益（低い順）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;日付（新しい順）、損益（高い順）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;日付（新しい順）、損益（低い順）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;損益（高い順）、日付（古い順）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;損益（高い順）、日付（新しい順）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;損益（低い順）、日付（古い順）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;7&lt;/td&gt;           &lt;td&gt;損益（低い順）、日付（新しい順）&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] value must be a 32 bit integer
**[ClosePositions](#ClosePositions)** | list, tuple,  | tuple,  | 返済建玉指定&lt;br&gt;※ClosePositionOrderとClosePositionsはどちらか一方のみ指定可能。&lt;br&gt;※ClosePositionOrderとClosePositionsを両方指定した場合、エラー。 | [optional] 
**[ReverseLimitOrder](#ReverseLimitOrder)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 逆指値条件&lt;br&gt; ※FrontOrderTypeで逆指値を指定した場合のみ必須。 | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ClosePositions

返済建玉指定<br>※ClosePositionOrderとClosePositionsはどちらか一方のみ指定可能。<br>※ClosePositionOrderとClosePositionsを両方指定した場合、エラー。

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | 返済建玉指定&lt;br&gt;※ClosePositionOrderとClosePositionsはどちらか一方のみ指定可能。&lt;br&gt;※ClosePositionOrderとClosePositionsを両方指定した場合、エラー。 | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PositionsDeriv**](PositionsDeriv.md) | [**PositionsDeriv**](PositionsDeriv.md) | [**PositionsDeriv**](PositionsDeriv.md) |  | 

# ReverseLimitOrder

逆指値条件<br> ※FrontOrderTypeで逆指値を指定した場合のみ必須。

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 逆指値条件&lt;br&gt; ※FrontOrderTypeで逆指値を指定した場合のみ必須。 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AfterHitPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | ヒット後注文価格&lt;br&gt; ※未設定の場合はエラーになります。&lt;br&gt; ※数字以外が設定された場合はエラーになります。&lt;br&gt;&lt;br&gt; ヒット後執行条件に従い、下記のようにヒット後注文価格を設定してください。  &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;ヒット後執行条件&lt;/th&gt;           &lt;th&gt;設定価格&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;成行&lt;/td&gt;       &lt;td&gt;0&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;指値&lt;/td&gt;       &lt;td&gt;指値の単価&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | value must be a 64 bit float
**UnderOver** | decimal.Decimal, int,  | decimal.Decimal,  | 以上／以下&lt;br&gt; ※未設定の場合はエラーになります。&lt;br&gt; ※1、2以外が指定された場合はエラーになります。 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;1&lt;/td&gt;       &lt;td&gt;以下&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;2&lt;/td&gt;       &lt;td&gt;以上&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | value must be a 32 bit integer
**AfterHitOrderType** | decimal.Decimal, int,  | decimal.Decimal,  | ヒット後執行条件&lt;br&gt; ※未設定の場合はエラーになります。&lt;br&gt; ※日通の注文で2以外が指定された場合はエラーになります。&lt;br&gt; ※日中、夜間の注文で1、2以外が指定された場合はエラーになります。&lt;br&gt; ※逆指値（成行）で有効期間条件(TimeInForce)にFAK以外を指定された場合はエラーになります。&lt;br&gt; ※逆指値（指値）で有効期間条件(TimeInForce)にFAS以外を指定された場合はエラーになります。 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;1&lt;/td&gt;       &lt;td&gt;成行&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;2&lt;/td&gt;       &lt;td&gt;指値&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | value must be a 32 bit integer
**TriggerPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | トリガ価格&lt;br&gt; ※未設定の場合はエラーになります。&lt;br&gt; ※数字以外が設定された場合はエラーになります。 | value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

