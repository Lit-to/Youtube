# 寝ている村人に食べ物を投げると動く、起きてしまう
-   2023-07-19 13:01:23
-   準備中
# 目次
- [寝ている村人に食べ物を投げると動く、起きてしまう](#寝ている村人に食べ物を投げると動く起きてしまう)
- [目次](#目次)
- [概要](#概要)
- [バグレポート情報](#バグレポート情報)
    - [確認済みバージョン](#確認済みバージョン)
    - [確認・修正状況](#確認修正状況)
- [wikiチェック](#wikiチェック)
- [検証](#検証)
- [結果](#結果)

# 概要
~~夜這いしているような動きを見せるのでなんかキモい。~~
[``Villagers move around in bed or even leave the bed when food is thrown at them``](https://bugs.mojang.com/browse/MC-157464)の紹介
Duplication(同じバグ報告)が32件存在している

寝ている村人に食べ物を投げると起きてしまう？
-   バグレポではパンのみ

# バグレポート情報
## 確認済みバージョン
(SSは除く)

-   1.14.4
-   1.15
-   1.15.2
-   1.16.1
-   1.16.4

要素:モブのふるまい(村人)


## 確認・修正状況
-   [x] 確認済み
-   [ ] 未解決

-   Duplication(被り):32件

# wikiチェック
wikiの村人のページ(https://minecraft.fandom.com/wiki/Villager#Sleeping )には<br>
![](2023-07-19-13-01-23.png) <br />
と既に記載あり、バグではなく限りなく仕様？

# 検証
1.  村人を並べる
2.  夜にする(見づらいので暗視)
![](2023-07-19_12.36.12.png)
-   村人が寝るはず
3.  食べ物を投げる  

# 結果
※レポジトリには動画付き

-   パン
→言う通りパンに寄せられる

-   それ以外の食べ物
→人参、ジャガイモには反応ありそう




