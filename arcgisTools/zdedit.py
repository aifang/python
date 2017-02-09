# coding=utf-8
import arcpy
from arcpy import env
import random

# wkid=2362
# sr=arcpy.SpatialReference(wkid)
gdbPath = "D:/Sharp Map/白云区地图/bigData/bigData.gdb"
sdePath = r"C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\192.168.12.25.sde"
env.workspace = sdePath

lyrEnterpriseInfos = 'EnterpriseInfos'
fields = ('LANDNO')
# fieldsIntersect=()
# with arcpy.da.UpdateCursor(lyrEnterpriseInfos, fields) as cursor:
#     for row in cursor:
#         row[0]="";
#         cursor.updateRow(row)
with arcpy.da.UpdateCursor(lyrEnterpriseInfos, fields) as cursor:
    for row in cursor:
        if row[0] != None:
            row[0] = row[0].split(',')[0]
            print(row[0])
        # row[0]="";
        # cursor.updateRow(row)
print('宗地 over')
