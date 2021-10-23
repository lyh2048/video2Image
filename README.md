# Video2Image

## 使用说明

1、安装依赖，需要安装`opencv-python`

> `numpy==1.21.3`
> `opencv-python==4.5.4.58`

```bash
pip install -r .\requirements.txt
```



2、运行程序

```bash
python .\main.py -i ./input/test.mp4 -m 2 -n 2 -o ./output/test22.png
```



## 示例

```bash
python .\main.py -i ./input/test.mp4 -m 2 -n 2 -o ./output/test22.png
```

>参数说明
>
>-i  	指定输入视频的路径
>
>-o 	指定输出图片的路径
>
>-m	指定行数
>
>-n	 指定列数

![test22](README.assets/test22.png)

