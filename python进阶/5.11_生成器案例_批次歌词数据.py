"""
案例：基于传入的数值（每批次的歌词条数），创建生成器，生成批次歌词
"""

# 需求：基于文件中的歌词，创建生成器，传入每批次歌词条数，生成批次歌词
import math

# 1. 定义函数，接收每批次的歌词条数，返回生成器
def dataset_loader(batch_size):
    """
    自定义 歌词批量 生成器
    :param batch_size:没批次的歌词条数
    :return:生成器，每个元素都是一批次的歌词，例如：（批次1歌词， 批次2歌词， 。。。）
    """

    # 1.1 打开读取文件
    with open('./data/5.11_生成器案例_批次歌词数据.txt', 'r', encoding = 'utf-8') as src_f:
        # 1.1.1 一次读取所有行
        lines = [line.strip() for line in src_f.readlines()]
        # print(lines)

        # 1.1.2 计算批次总数
        total_batch = math.ceil(len(lines) / batch_size)

        # 1.1.3 or循环的方式，创建生成器,获取每批次的数据，存储到生成器中，最后返回生成器
        for i in range(total_batch):
            # 思考我要获取什么数据呢？
            # 第1批 批次索引（i=0）     lines歌词列表里面第1~3行 索引（0~2）
            # 第2批 批次索引（i=1）     lines歌词列表里面第4~6行 索引（3~5）
            # 第3批 批次索引（i=2）     lines歌词列表里面第7~9行 索引（6~8）
            # ......
            yield lines[i * batch_size : i * batch_size + batch_size]

# 2. 测试
dl = dataset_loader(4)
print(next(dl))
print(next(dl))

for line in dl:
    print(line)
