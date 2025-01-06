# mypkg
[![test](https://github.com/lemon528/robosys2024/actions/workflows/test.yml/badge.svg)](https://github.com/lemon528/robosys2024/actions/workflows/test.yml)  
このリポジトリは、センサー値をシミュレートするROS2のパッケージです。

## ノード
- ノード名:`sensor_simulator`
    - サイン波に基づいたセンサー値をシミュレートします。
    - 中心値5.0, 振幅2.0の範囲(3.0 ~ 7.0)で変動する値を`/sensor_data`に1秒ごと送信します。

## トピック
- トピック名:`/sensor_data`
    - シミュレーションされたセンサー値を送信します。　　　

## 実行方法と出力結果
- 端末1
```
$ ros2 run mypkg sensor_simulator
```

- 端末2
```
$ ros2 topic echo /sensor_data
data: 6.701807022094727
---
data: 6.9971818923950195
---
data: 6.803576469421387
---
data: 5.247146129608154
---
data: 4.265389442443848
---
data: 3.4634907245635986
---
data: 3.037783145904541
```

## 必要なソフトウェア
- Python

## テスト環境
- Ubuntu 22.04.5 LTS

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- このパッケージの一部のコードは、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。
    - https://ryuichiueda.github.io/slides_marp/robosys2024/lesson8.html#1
    - https://ryuichiueda.github.io/slides_marp/robosys2024/lesson9.html#1
    - https://ryuichiueda.github.io/slides_marp/robosys2024/lesson10.html#1
    - https://ryuichiueda.github.io/slides_marp/robosys2024/lesson11.html#1
- © 2025 Kouhei Kobayashi
