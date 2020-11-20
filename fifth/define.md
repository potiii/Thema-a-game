#character
###構成
Characterクラス(親)  
→Princeクラス(子)  
→Stinkerクラス(子) 

###定義
hp,hpの上限,攻撃力(共通パラメーター)  
攻撃を受けたときの処理(共通処理)  

武器の装備の有無(Prince)
武器を装備する処理(Prince)  
ポーションを使う処理(Prince)
攻撃を受けたときの処理の継承(Prince)  

攻撃を受けたときの処理の継承(stinker)  

####error
line31 and 44

#room
###構成
roomクラス

###定義
####パラメータ
sword,訪問済,ポーション,stinker,lock,prince,x,y
####処理
roomオブジェクトのパラメータで持っているオブジェクトの始末  
訪問済パラメータをTrueにする処理  
ロックを解除する処理  
princeオブジェクトをsetする処理

#Map
###構成
mapクラス
###定義
Roomの二次元配列を初期化時に生成する。
#####パラメータ
Roomの二次元配列,Mapの最大サイズ(x,y)
#####処理
X,Yを指定してRoomオブジェクトを取り出す処理  
Mapを描画するときのドアを判定する処理  
Mapを描画するときのスメルを判定する処理  
Mapをプリントする処理  

#Game
###構成
Gameクラス
###定義
####初期化時
Mapオブジェクトを持たせる  
Princeの座標を持つX,Y  
開始地点のRoomオブジェクトを参照する  
####処理
Princeを移動する処理  
ゲームデータを更新する処理  
ユーザー入力を受け付ける処理

