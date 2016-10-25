#coding=utf-8
import arcpy
from arcpy import env
# important 用arcmap编辑必须注册版本，用代码编辑必须取消版本注册
gdbPath="D:/Sharp Map/白云区地图/bigData/bigData.gdb"
sdePath=r"C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\192.168.12.25.sde"
env.workspace = sdePath
#0.5米叠加，出现效果
lyrEnterpriseInfos='EnterpriseInfos'
lyrZDIntersect='EnterpriseInfosZD_Intersect'
fields=['LANDNO','OBJECTID'] #['LANDNO']  #
fieldsIntersect=['DJH','FID_ENTERPRISEINFOS']

with arcpy.da.SearchCursor(lyrZDIntersect, fieldsIntersect) as cursor:
    for row in cursor: 
        where=fields[1]+"='"+str(row[1]) +"'"
        with arcpy.da.UpdateCursor(lyrEnterpriseInfos,where_clause=where, field_names=fields) as pcursor:
            for prow in pcursor: 
                if prow[0]!=None and prow[0].strip()!="":
                    prow[0]+=','+row[0]
                else:
                    prow[0]=row[0]
                print(prow[0])
                pcursor.updateRow(prow)
print('宗地 over')
        
#0.0米叠加，出现效果
#清除多个叠加zd
# count=0;
# wer="LANDNO LIKE '%,%'"
# with arcpy.da.UpdateCursor(lyrEnterpriseInfos,where_clause=wer, field_names=fields) as pcursor:
#     for prow in pcursor:
#         count+=1
#         print(prow[0]) 
#         prow[0]=prow[0].split(',')[0]
#         print(prow[0])
#         print(count)
#         pcursor.updateRow(prow)
# print('宗地 over')

#清空LANDNO字段
# with arcpy.da.UpdateCursor(lyrEnterpriseInfos, field_names=fields) as pcursor:
#     for prow in pcursor: 
#         prow[0]=None
#         pcursor.updateRow(prow)
# print('宗地 over')

