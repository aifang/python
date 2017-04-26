#coding=utf-8
import arcpy
from arcpy import env
import random

# wkid=2362
# sr=arcpy.SpatialReference(wkid)
gdbPath="D:/Sharp Map/白云区地图/bigData"
gdbName="bigData.gdb"
ws=gdbPath + '/'+  gdbName
env.workspace = ws

# lyrXZQ='XZQ/BYXZQ'
# lyrEnterpriseInfos='EnterpriseData/EnterpriseInfos'
lyrXZQ='BYXZQ'
lyrEnterpriseInfos='EnterpriseInfos'

fields=('Province','ProvinceCode')
with arcpy.da.UpdateCursor(lyrEnterpriseInfos, fields) as cursor:
    for row in cursor:     
        row[0]='广东省'
        row[1]='440000'
        cursor.updateRow(row)
print('Province over')

fields=('City','CityCode')
with arcpy.da.UpdateCursor(lyrEnterpriseInfos, fields) as cursor:
    for row in cursor:     
        row[0]='广州市'
        row[1]='440100'
        cursor.updateRow(row)
print('City over')

fields=('District','DistrictCode')
with arcpy.da.UpdateCursor(lyrEnterpriseInfos, fields) as cursor:
    for row in cursor:     
        row[0]='白云区'
        row[1]='440111'
        cursor.updateRow(row)
print('District over')
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
