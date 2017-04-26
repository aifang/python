# coding=utf-8
# 随机生成企业税收、产值，年份，门类
import arcpy
from arcpy import env
import random

# important 用arcmap编辑必须注册版本，用代码编辑必须取消版本注册
env.workspace = r"C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\192.168.12.25.sde"

lyrEnterpriseInfos = 'outputAndTax'
fields = ['PRODUCTTYPE','DOORCALSS','OBJECTID']

# lyrXZQ='XZQ/BYXZQ'
# lyrEnterpriseInfos='EnterpriseData/EnterpriseInfos'

with arcpy.da.UpdateCursor(lyrEnterpriseInfos, where_clause="ENTERPRISESSTYPE='四上企业'", field_names=fields) as cursor:
    for row in cursor:     
        row[0]=random.choice(('皮具',None,'化妆品',None,'汽车产业'));
        row[1]=random.choice(('工业','商业','营利性服务业','农、林、牧、渔业','建筑、房地产业','金融业','科学研究和技术服务业','水利、环境和公共设施管理业','教育','卫生和社会工作','公共管理、社会保障和社会组织','国际组织'));
        cursor.updateRow(row)
        print(row[0])
        print(row[1])
print('Province over')
