# TNTの爆発に巻き込まれたときに盾を構えていてもダメージを喰らう
-   2023-09-19 03:31:31
-   準備中


# 目次
- [TNTの爆発に巻き込まれたときに盾を構えていてもダメージを喰らう](#tntの爆発に巻き込まれたときに盾を構えていてもダメージを喰らう)
- [目次](#目次)
- [ソース](#ソース)
- [報告状況](#報告状況)
    - [最新の確認済みバージョン](#最新の確認済みバージョン)
    - [ステータス](#ステータス)
    - [内容](#内容)
        - [ダメージの方向](#ダメージの方向)
        - [盾がTNTの爆発が守れない](#盾がtntの爆発が守れない)


# ソース
-   [MC-261433](https://bugs.mojang.com/browse/MC-261433)(``Shield doesn't block TNT explosion``)
-   [MC-92017](https://bugs.mojang.com/browse/MC-92017)(``Shield damage direction is incorrect``)

# 報告状況
## 最新の確認済みバージョン
-   1.19.4

## ステータス
-   修正済み(1.20 Pre-release_2)

## 内容
この報告は一度直った後別のバグが発生したっぽい
### ダメージの方向
id:92017の報告  
ダメージが間接的に与えられた時に、ダメージの方向が正しくなかった。  
EntityA EntityB TNT  
この並び方で立っている時、AがTNTを起爆しBにダメージを与えると本来TNTの方向からダメージを喰らうべきなのにAの方向から喰らってしまう。  

→``22w43a``(1.19.3)で修正された

### 盾がTNTの爆発が守れない
id:261433の報告  
1.19.3で盾から正しくダメージが防げるようになった。しかし、**1.19.4ではそもそも盾がTNTダメージを守れなくなった**

→``1.20 PreRelease_2``で修正された




