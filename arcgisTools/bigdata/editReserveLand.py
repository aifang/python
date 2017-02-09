# coding=utf-8

import arcpy
from arcpy import env
# important 用arcmap编辑必须注册版本，用代码编辑必须取消版本注册
sdePath = r"C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\192.168.12.25.sde"
env.workspace = sdePath

lyrReserveLand = 'ReserveLand'
fields = ['PROJECTNAME', 'OBJECTID']

# 储备用地数据处理

def trimProjectName():
    where = "1=1"
    with arcpy.da.UpdateCursor(lyrReserveLand, where_clause=where, field_names=fields) as pcursor:
        for prow in pcursor:
            if prow[0] != None:
                prow[0] = prow[0].strip()
            print(prow[0])
            pcursor.updateRow(prow)
    print('宗地 over')

trimProjectName();