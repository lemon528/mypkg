# robosys2024_ROS2
[![test](https://github.com/lemon528/robosys2024/actions/workflows/test.yml/badge.svg)](https://github.com/lemon528/robosys2024/actions/workflows/test.yml)

## sensor_simulator
ノイズ付きセンサー値をシミュレートし、それをトピックに配信します。

## 使用方法
- リポジトリをクローン
- cdでディレクトリに移動
- ワークスペースのビルド

```
$ git clone https://github.com/lemon528/robosys2024_ROS2.git

$ cd ros2_ws

$ colcon build

$ source ~/.bashrc
```

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

## テスト環境
- Ubuntu 22.04.5 LTS

## ライセンス
- このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布および使用が許可されます。
- 
