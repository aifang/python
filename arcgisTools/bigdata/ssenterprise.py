#coding=utf-8
import arcpy
from arcpy import env

# wkid=2362
# sr=arcpy.SpatialReference(wkid)
shp=r"D:\Sharp Map\sss.gdb"
env.workspace = shp

lyrEnterpriseInfos='ssqy'

fields=('isgq','iswz','iswm','isds','iswl','iszypf','zxlx')
arrCN=['高新技术企业','外资企业','外贸企业','电商企业','物流企业','专业批发市场']
with arcpy.da.UpdateCursor(lyrEnterpriseInfos, fields) as cursor:
    for row in cursor:  
        zxlx=""
        for idx in [0,1,2,3,4,5]:
            if row[idx].strip()!="":
                if idx!=5:
                    zxlx+=arrCN[idx]+',' 
        zxlx=zxlx[0:-1]
        print(zxlx)   
        row[6]=zxlx    
        cursor.updateRow(row)
print('xzlx over')

# fields=(r'zxlx')
# with arcpy.da.UpdateCursor(lyrEnterpriseInfos, fields) as cursor:
#     for row in cursor:     
#         row[0]=""
#         cursor.updateRow(row)
# print('Province over')
# fields=(r'zxlx')
# with arcpy.da.UpdateCursor(lyrEnterpriseInfos, fields) as cursor:
#     for row in cursor:     
#         print(row[0]) 
# print('zxlx over')


