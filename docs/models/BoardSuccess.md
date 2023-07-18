# openapi_client.model.board_success.BoardSuccess

下記にあるBIDとASKとは、トレーダー目線から見た場合の値であるため、BidPrice=Sell1のPrice、AskPrice=Buy1のPriceという数値となります。

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 下記にあるBIDとASKとは、トレーダー目線から見た場合の値であるため、BidPrice&#x3D;Sell1のPrice、AskPrice&#x3D;Buy1のPriceという数値となります。 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Symbol** | str,  | str,  | 銘柄コード | [optional] 
**SymbolName** | str,  | str,  | 銘柄名 | [optional] 
**Exchange** | decimal.Decimal, int,  | decimal.Decimal,  | 市場コード&lt;br&gt;※株式・先物・オプション銘柄の場合のみ &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;東証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;名証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;福証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;札証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;日通し&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;23&lt;/td&gt;           &lt;td&gt;日中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;24&lt;/td&gt;           &lt;td&gt;夜間&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] value must be a 32 bit integer
**ExchangeName** | str,  | str,  | 市場名称&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] 
**CurrentPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | 現値 | [optional] value must be a 64 bit float
**CurrentPriceTime** | str, datetime,  | str,  | 現値時刻 | [optional] value must conform to RFC-3339 date-time
**CurrentPriceChangeStatus** | str,  | str,  | 現値前値比較 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;0000&lt;/td&gt;           &lt;td&gt;事象なし&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0056&lt;/td&gt;           &lt;td&gt;変わらず&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0057&lt;/td&gt;           &lt;td&gt;UP&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0058&lt;/td&gt;           &lt;td&gt;DOWN&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0059&lt;/td&gt;           &lt;td&gt;中断板寄り後の初値&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0060&lt;/td&gt;           &lt;td&gt;ザラバ引け&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0061&lt;/td&gt;           &lt;td&gt;板寄り引け&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0062&lt;/td&gt;           &lt;td&gt;中断引け&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0063&lt;/td&gt;           &lt;td&gt;ダウン引け&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0064&lt;/td&gt;           &lt;td&gt;逆転終値&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0066&lt;/td&gt;           &lt;td&gt;特別気配引け&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0067&lt;/td&gt;           &lt;td&gt;一時留保引け&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0068&lt;/td&gt;           &lt;td&gt;売買停止引け&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0069&lt;/td&gt;           &lt;td&gt;サーキットブレーカ引け&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0431&lt;/td&gt;           &lt;td&gt;ダイナミックサーキットブレーカ引け&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**CurrentPriceStatus** | decimal.Decimal, int,  | decimal.Decimal,  | 現値ステータス &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;現値&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;不連続歩み&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;板寄せ&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;システム障害&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;中断&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;売買停止&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;7&lt;/td&gt;           &lt;td&gt;売買停止・システム停止解除&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;8&lt;/td&gt;           &lt;td&gt;終値&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;9&lt;/td&gt;           &lt;td&gt;システム停止&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;10&lt;/td&gt;           &lt;td&gt;概算値&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;11&lt;/td&gt;           &lt;td&gt;参考値&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;12&lt;/td&gt;           &lt;td&gt;サーキットブレイク実施中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;13&lt;/td&gt;           &lt;td&gt;システム障害解除&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;14&lt;/td&gt;           &lt;td&gt;サーキットブレイク解除&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;15&lt;/td&gt;           &lt;td&gt;中断解除&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;16&lt;/td&gt;           &lt;td&gt;一時留保中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;17&lt;/td&gt;           &lt;td&gt;一時留保解除&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;18&lt;/td&gt;           &lt;td&gt;ファイル障害&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;19&lt;/td&gt;           &lt;td&gt;ファイル障害解除&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;20&lt;/td&gt;           &lt;td&gt;Spread/Strategy&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;21&lt;/td&gt;           &lt;td&gt;ダイナミックサーキットブレイク発動&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;22&lt;/td&gt;           &lt;td&gt;ダイナミックサーキットブレイク解除&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;23&lt;/td&gt;           &lt;td&gt;板寄せ約定&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] value must be a 32 bit integer
**CalcPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | 計算用現値 | [optional] value must be a 64 bit float
**PreviousClose** | decimal.Decimal, int, float,  | decimal.Decimal,  | 前日終値 | [optional] value must be a 64 bit float
**PreviousCloseTime** | str, datetime,  | str,  | 前日終値日付 | [optional] value must conform to RFC-3339 date-time
**ChangePreviousClose** | decimal.Decimal, int, float,  | decimal.Decimal,  | 前日比 | [optional] value must be a 64 bit float
**ChangePreviousClosePer** | decimal.Decimal, int, float,  | decimal.Decimal,  | 騰落率 | [optional] value must be a 64 bit float
**OpeningPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | 始値 | [optional] value must be a 64 bit float
**OpeningPriceTime** | str, datetime,  | str,  | 始値時刻 | [optional] value must conform to RFC-3339 date-time
**HighPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | 高値 | [optional] value must be a 64 bit float
**HighPriceTime** | str, datetime,  | str,  | 高値時刻 | [optional] value must conform to RFC-3339 date-time
**LowPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | 安値 | [optional] value must be a 64 bit float
**LowPriceTime** | str, datetime,  | str,  | 安値時刻 | [optional] value must conform to RFC-3339 date-time
**TradingVolume** | decimal.Decimal, int, float,  | decimal.Decimal,  | 売買高&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**TradingVolumeTime** | str, datetime,  | str,  | 売買高時刻&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must conform to RFC-3339 date-time
**VWAP** | decimal.Decimal, int, float,  | decimal.Decimal,  | 売買高加重平均価格（VWAP）&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**TradingValue** | decimal.Decimal, int, float,  | decimal.Decimal,  | 売買代金&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**BidQty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 最良売気配数量 ※①&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**BidPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | 最良売気配値段 ※①&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**BidTime** | str, datetime,  | str,  | 最良売気配時刻 ※①&lt;br&gt;※株式銘柄の場合のみ | [optional] value must conform to RFC-3339 date-time
**BidSign** | str,  | str,  | 最良売気配フラグ ※①&lt;br&gt;※株式・先物・オプション銘柄の場合のみ &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;0000&lt;/td&gt;           &lt;td&gt;事象なし&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0101&lt;/td&gt;           &lt;td&gt;一般気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0102&lt;/td&gt;           &lt;td&gt;特別気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0103&lt;/td&gt;           &lt;td&gt;注意気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0107&lt;/td&gt;           &lt;td&gt;寄前気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0108&lt;/td&gt;           &lt;td&gt;停止前特別気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0109&lt;/td&gt;           &lt;td&gt;引け後気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0116&lt;/td&gt;           &lt;td&gt;寄前気配約定成立ポイントなし&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0117&lt;/td&gt;           &lt;td&gt;寄前気配約定成立ポイントあり&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0118&lt;/td&gt;           &lt;td&gt;連続約定気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0119&lt;/td&gt;           &lt;td&gt;停止前の連続約定気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0120&lt;/td&gt;           &lt;td&gt;買い上がり売り下がり中&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**MarketOrderSellQty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 売成行数量&lt;br&gt;※株式銘柄の場合のみ | [optional] value must be a 64 bit float
**[Sell1](#Sell1)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量1本目 | [optional] 
**[Sell2](#Sell2)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量2本目 | [optional] 
**[Sell3](#Sell3)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量3本目 | [optional] 
**[Sell4](#Sell4)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量4本目 | [optional] 
**[Sell5](#Sell5)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量5本目 | [optional] 
**[Sell6](#Sell6)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量6本目 | [optional] 
**[Sell7](#Sell7)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量7本目 | [optional] 
**[Sell8](#Sell8)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量8本目 | [optional] 
**[Sell9](#Sell9)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量9本目 | [optional] 
**[Sell10](#Sell10)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量10本目 | [optional] 
**AskQty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 最良買気配数量 ※①&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**AskPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | 最良買気配値段 ※①&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**AskTime** | str, datetime,  | str,  | 最良買気配時刻 ※①&lt;br&gt;※株式銘柄の場合のみ | [optional] value must conform to RFC-3339 date-time
**AskSign** | str,  | str,  | 最良買気配フラグ ※①&lt;br&gt;※株式・先物・オプション銘柄の場合のみ &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;0000&lt;/td&gt;           &lt;td&gt;事象なし&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0101&lt;/td&gt;           &lt;td&gt;一般気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0102&lt;/td&gt;           &lt;td&gt;特別気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0103&lt;/td&gt;           &lt;td&gt;注意気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0107&lt;/td&gt;           &lt;td&gt;寄前気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0108&lt;/td&gt;           &lt;td&gt;停止前特別気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0109&lt;/td&gt;           &lt;td&gt;引け後気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0116&lt;/td&gt;           &lt;td&gt;寄前気配約定成立ポイントなし&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0117&lt;/td&gt;           &lt;td&gt;寄前気配約定成立ポイントあり&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0118&lt;/td&gt;           &lt;td&gt;連続約定気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0119&lt;/td&gt;           &lt;td&gt;停止前の連続約定気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0120&lt;/td&gt;           &lt;td&gt;買い上がり売り下がり中&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**MarketOrderBuyQty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 買成行数量&lt;br&gt;※株式銘柄の場合のみ | [optional] value must be a 64 bit float
**[Buy1](#Buy1)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量1本目 | [optional] 
**[Buy2](#Buy2)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量2本目 | [optional] 
**[Buy3](#Buy3)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量3本目 | [optional] 
**[Buy4](#Buy4)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量4本目 | [optional] 
**[Buy5](#Buy5)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量5本目 | [optional] 
**[Buy6](#Buy6)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量6本目 | [optional] 
**[Buy7](#Buy7)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量7本目 | [optional] 
**[Buy8](#Buy8)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量8本目 | [optional] 
**[Buy9](#Buy9)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量9本目 | [optional] 
**[Buy10](#Buy10)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量10本目 | [optional] 
**OverSellQty** | decimal.Decimal, int, float,  | decimal.Decimal,  | OVER気配数量&lt;br&gt;※株式銘柄の場合のみ | [optional] value must be a 64 bit float
**UnderBuyQty** | decimal.Decimal, int, float,  | decimal.Decimal,  | UNDER気配数量&lt;br&gt;※株式銘柄の場合のみ | [optional] value must be a 64 bit float
**TotalMarketValue** | decimal.Decimal, int, float,  | decimal.Decimal,  | 時価総額&lt;br&gt;※株式銘柄の場合のみ | [optional] value must be a 64 bit float
**ClearingPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | 清算値&lt;br&gt;※先物銘柄の場合のみ | [optional] value must be a 64 bit float
**IV** | decimal.Decimal, int, float,  | decimal.Decimal,  | インプライド・ボラティリティ&lt;br&gt;※オプション銘柄かつ日通しの場合のみ | [optional] value must be a 64 bit float
**Gamma** | decimal.Decimal, int, float,  | decimal.Decimal,  | ガンマ&lt;br&gt;※オプション銘柄かつ日通しの場合のみ | [optional] value must be a 64 bit float
**Theta** | decimal.Decimal, int, float,  | decimal.Decimal,  | セータ&lt;br&gt;※オプション銘柄かつ日通しの場合のみ | [optional] value must be a 64 bit float
**Vega** | decimal.Decimal, int, float,  | decimal.Decimal,  | ベガ&lt;br&gt;※オプション銘柄かつ日通しの場合のみ | [optional] value must be a 64 bit float
**Delta** | decimal.Decimal, int, float,  | decimal.Decimal,  | デルタ&lt;br&gt;※オプション銘柄かつ日通しの場合のみ | [optional] value must be a 64 bit float
**SecurityType** | decimal.Decimal, int,  | decimal.Decimal,  | 銘柄種別 &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;定義値&lt;/th&gt;       &lt;th&gt;説明&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;0&lt;/td&gt;       &lt;td&gt;指数&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;1&lt;/td&gt;       &lt;td&gt;現物&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;101&lt;/td&gt;       &lt;td&gt;日経225先物&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;103&lt;/td&gt;       &lt;td&gt;日経225OP&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;107&lt;/td&gt;       &lt;td&gt;TOPIX先物&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;121&lt;/td&gt;       &lt;td&gt;JPX400先物&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;144&lt;/td&gt;       &lt;td&gt;NYダウ&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;145&lt;/td&gt;       &lt;td&gt;日経平均VI&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;154&lt;/td&gt;       &lt;td&gt;東証マザーズ指数先物&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;155&lt;/td&gt;       &lt;td&gt;TOPIX_REIT&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;171&lt;/td&gt;       &lt;td&gt;TOPIX CORE30&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;901&lt;/td&gt;       &lt;td&gt;日経平均225ミニ先物&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;907&lt;/td&gt;       &lt;td&gt;TOPIXミニ先物&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Sell1

売気配数量1本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量1本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Time** | str, datetime,  | str,  | 時刻&lt;br&gt;※株式銘柄の場合のみ | [optional] value must conform to RFC-3339 date-time
**Sign** | str,  | str,  | 気配フラグ&lt;br&gt;※株式・先物・オプション銘柄の場合のみ &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;0000&lt;/td&gt;           &lt;td&gt;事象なし&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0101&lt;/td&gt;           &lt;td&gt;一般気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0102&lt;/td&gt;           &lt;td&gt;特別気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0103&lt;/td&gt;           &lt;td&gt;注意気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0107&lt;/td&gt;           &lt;td&gt;寄前気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0108&lt;/td&gt;           &lt;td&gt;停止前特別気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0109&lt;/td&gt;           &lt;td&gt;引け後気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0116&lt;/td&gt;           &lt;td&gt;寄前気配約定成立ポイントなし&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0117&lt;/td&gt;           &lt;td&gt;寄前気配約定成立ポイントあり&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0118&lt;/td&gt;           &lt;td&gt;連続約定気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0119&lt;/td&gt;           &lt;td&gt;停止前の連続約定気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0120&lt;/td&gt;           &lt;td&gt;買い上がり売り下がり中&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Sell2

売気配数量2本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量2本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Sell3

売気配数量3本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量3本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Sell4

売気配数量4本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量4本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Sell5

売気配数量5本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量5本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Sell6

売気配数量6本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量6本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Sell7

売気配数量7本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量7本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Sell8

売気配数量8本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量8本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Sell9

売気配数量9本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量9本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Sell10

売気配数量10本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 売気配数量10本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Buy1

買気配数量1本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量1本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Time** | str, datetime,  | str,  | 時刻&lt;br&gt;※株式銘柄の場合のみ | [optional] value must conform to RFC-3339 date-time
**Sign** | str,  | str,  | 気配フラグ&lt;br&gt;※株式・先物・オプション銘柄の場合のみ &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;0000&lt;/td&gt;           &lt;td&gt;事象なし&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0101&lt;/td&gt;           &lt;td&gt;一般気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0102&lt;/td&gt;           &lt;td&gt;特別気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0103&lt;/td&gt;           &lt;td&gt;注意気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0107&lt;/td&gt;           &lt;td&gt;寄前気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0108&lt;/td&gt;           &lt;td&gt;停止前特別気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0109&lt;/td&gt;           &lt;td&gt;引け後気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0116&lt;/td&gt;           &lt;td&gt;寄前気配約定成立ポイントなし&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0117&lt;/td&gt;           &lt;td&gt;寄前気配約定成立ポイントあり&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0118&lt;/td&gt;           &lt;td&gt;連続約定気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0119&lt;/td&gt;           &lt;td&gt;停止前の連続約定気配&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0120&lt;/td&gt;           &lt;td&gt;買い上がり売り下がり中&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] 
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Buy2

買気配数量2本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量2本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Buy3

買気配数量3本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量3本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Buy4

買気配数量4本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量4本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Buy5

買気配数量5本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量5本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Buy6

買気配数量6本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量6本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Buy7

買気配数量7本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量7本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Buy8

買気配数量8本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量8本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Buy9

買気配数量9本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量9本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Buy10

買気配数量10本目

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 買気配数量10本目 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | 値段&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**Qty** | decimal.Decimal, int, float,  | decimal.Decimal,  | 数量&lt;br&gt;※株式・先物・オプション銘柄の場合のみ | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

