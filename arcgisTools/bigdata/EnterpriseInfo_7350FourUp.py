# coding=utf-8
import arcpy
from arcpy import env
# important 用arcmap编辑必须注册版本，用代码编辑必须取消版本注册
gdbPath = "D:/Sharp Map/白云区地图/bigData/bigData_1.gdb"
# sdePath = r"C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\10.128.117.252.sde"
env.workspace = gdbPath
# ----------本脚本所做的事情---------------
# 1.行政区叠加，得到真实地理位置街镇
# 2.写入真实地理位置街镇
# 3.叠加宗地数据，获取关联宗地
# 4.写入landNo宗地字段
# 5.人工手动导入到服务器中，注意备份

# lyrXZQ='BYXZQ'
# lyrEnterpriseInfos='correctPosition7350'

# fields=('Province','ProvinceCode')
# with arcpy.da.UpdateCursor(lyrEnterpriseInfos, fields) as cursor:
#     for row in cursor:     
#         row[0]='广东省'
#         row[1]='440000'
#         cursor.updateRow(row)
# print('Province over')

# fields=('City','CityCode')
# with arcpy.da.UpdateCursor(lyrEnterpriseInfos, fields) as cursor:
#     for row in cursor:     
#         row[0]='广州市'
#         row[1]='440100'
#         cursor.updateRow(row)
# print('City over')

# fields=('District','DistrictCode')
# with arcpy.da.UpdateCursor(lyrEnterpriseInfos, fields) as cursor:
#     for row in cursor:     
#         row[0]='白云区'
#         row[1]='440111'
#         cursor.updateRow(row)
# print('District over')

