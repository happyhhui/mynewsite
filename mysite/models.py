from django.db import models

# Create your models here.

class NewTable(models.Model):
    bigint_f = models.BigIntegerField()   #64位的大整数
    bool_f = models.BooleanField()      #布尔值，只有True/False两种
    date_f = models.DateField(auto_now=True)  #日期格式，auto_now每次对象被修改后自动加入，auto_now_add只有被创建时加入
    char_f = models.CharField(max_length=20,unique=True)  #拆除较短的字符串或数字
    datetime_f = models.DateField(auto_now_add=True)
    decimal_f = models.DecimalField(max_digits=10,decimal_places=2) #定点小数数值数据，max_digits接受的最大位数，decimal_places小数占用位数
    float_f = models.FloatField(null=True)       #浮点数字段
    int_f = models.IntegerField(default=2010)    #整数字段
    text_f = models.TextField()             #长文字格式

class Product(models.Model):
    SIZES = (
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        )
    sku = models.CharField(max_length=5,verbose_name='SKU值')
    name = models.CharField(max_length=20,verbose_name='品牌名')
    price = models.PositiveIntegerField(verbose_name='价格')     #正整数字段
    qty = models.PositiveIntegerField(default=0,verbose_name='库存')
    size = models.CharField(max_length=1,choices=SIZES,verbose_name='型号大小')    #choices上以选项的方式
    pub_date = models.DateTimeField(auto_now_add=True,verbose_name='上传时间')
    edit_date = models.DateTimeField(auto_now=True,verbose_name='修改时间')

    # 默认按sku降序排列
    class Meta:
        ordering = ('-sku',)
    def __str__(self):
        return self.name