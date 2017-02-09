# coding=utf-8
# 随机生成企业税收产值，提供村社热力图使用
import arcpy
from arcpy import env
import random

# important 用arcmap编辑必须注册版本，用代码编辑必须取消版本注册
sdePath = r"C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\10.128.117.252.sde"
env.workspace = sdePath

lyrEnterpriseInfos = 'EnterpriseInfos'
fields = ['TAXVALUE', 'OUTPUTVALUE','OBJECTID']

# lyrXZQ='XZQ/BYXZQ'
# lyrEnterpriseInfos='EnterpriseData/EnterpriseInfos'

with arcpy.da.UpdateCursor(lyrEnterpriseInfos, where_clause="ENTERPRISESSTYPE='四上企业'", field_names=fields) as cursor:
    for row in cursor:     
        row[0]=random.randint(200,600);
        row[1]=random.randint(500,1000);
        cursor.updateRow(row)
        print(row[0])
        print(row[1])
print('Province over')


# fields=('RegisterYear')
# with arcpy.da.UpdateCursor(lyrEnterpriseInfos, fields) as cursor:
#     for row in cursor:     
#         row[0]=random.randint(2010,2015);
#         cursor.updateRow(row)
# print('RegisterYear over')

# fields=('ZXLX')
# with arcpy.da.UpdateCursor(lyrEnterpriseInfos, fields) as cursor:
#     for row in cursor:     
#         row[0]=random.choice(['专业批发市场','高新技术企业','物流企业','电商企业','外资企业','外贸企业']);
#         cursor.updateRow(row)
# print('over')