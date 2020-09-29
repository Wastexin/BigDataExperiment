from pyspark import SparkConf, SparkContext
# from visualize import visualize
import jieba

SRCPATH = '/src/'

# conf = SparkConf().setAppName("ex2").setMaster("spark://master:7077")
conf = SparkConf().setAppName("ex2").setMaster("local")
sc = SparkContext(conf=conf)

answers_filePath = 'src/answers.txt'
answersRdd = sc.textFile(answers_filePath)
# print(answersRdd.take(10))  # 展示前10行数据验证
str = answersRdd.reduce(lambda a,b:a+b)

# jieba分词
words_list = jieba.lcut(str)
print(words_list)