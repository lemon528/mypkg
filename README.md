# mypkg
[![test](https://github.com/lemon528/robosys2024/actions/workflows/test.yml/badge.svg)](https://github.com/lemon528/robosys2024/actions/workflows/test.yml)  
このリポジトリは、ROS2パッケージ`mypkg`を提供します。

## sensor_simulator
ノイズ付きセンサー値をシミュレートし、それをトピックに配信します。

## 実行方法と出力結果
- sensor_simulator
```
$ ros2 run mypkg sensor_simulator
[INFO] [1735812505.849612880] [noisy_sensor_simulator]: Noisy Sensor value: 6.71
[INFO] [1735812506.849660507] [noisy_sensor_simulator]: Noisy Sensor value: 5.41
[INFO] [1735812507.849832367] [noisy_sensor_simulator]: Noisy Sensor value: 3.67
```

- sensor_simulator.launch.py
```
$ ros2 launch mypkg sensor_simulator.launch.py
[sensor_simulator-1] [INFO] [1735812559.734612598] [noisy_sensor_simulator]: Noisy Sensor value: 6.71
[sensor_simulator-1] [INFO] [1735812560.734613589] [noisy_sensor_simulator]: Noisy Sensor value: 5.41
[sensor_simulator-1] [INFO] [1735812561.735071482] [noisy_sensor_simulator]: Noisy Sensor value: 3.67
```

## 必要ソフトウェア
- Python version 3.10 以上
- Ubuntu version 22.04 LTS 以上
- ROS2 Humble

## テスト環境
- Python 3.10.12
- Ubuntu 22.04.5 LTS
- ROS2 Humble

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- このパッケージの一部のコードは、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。
    - https://ryuichiueda.github.io/slides_marp/robosys2024/lesson8.html#1
    - https://ryuichiueda.github.io/slides_marp/robosys2024/lesson9.html#1
    - https://ryuichiueda.github.io/slides_marp/robosys2024/lesson10.html#1
    - https://ryuichiueda.github.io/slides_marp/robosys2024/lesson11.html#1
- © 2025 Kouhei Kobayashi
