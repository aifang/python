#coding=utf-8
import arcpy
from arcpy import env

info = [
    {'layerName':'EnterpriseInfos','layeralias':'企业信息','geometry':'POINT','fields':[
        {'name':'ZZJGCode','type':'TEXT','length':32,'alias':'组织机构代码'},
        {'name':'EnterpriseName','type':'TEXT','length':128,'alias':'企业名称'},
        {'name':'Address','type':'TEXT','length':128,'alias':'企业地址'},
        {'name':'Province','type':'TEXT','length':32,'alias':'省份'},
        {'name':'ProvinceCode','type':'TEXT','length':32,'alias':'省份代码'},
        {'name':'City','type':'TEXT','length':32,'alias':'城市'},
        {'name':'CityCode','type':'TEXT','length':32,'alias':'城市代码'}, 
        {'name':'Area','type':'TEXT','length':32,'alias':'区县'},
        {'name':'AreaCoderea','type':'TEXT','length':32,'alias':'区县代码'},
        {'name':'StreetTown','type':'TEXT','length':32,'alias':'街镇'},
        {'name':'StreetTownCode','type':'TEXT','length':32,'alias':'街镇代码'},
        {'name':'Village','type':'TEXT','length':32,'alias':'村舍'},
        {'name':'VillageCode','type':'TEXT','length':32,'alias':'村舍代码'},
        {'name':'HYName','type':'TEXT','length':32,'alias':'行业'},
        {'name':'HYCode','type':'TEXT','length':32,'alias':'行业代码'},
        {'name':'ZXLX','type':'TEXT','length':32,'alias':'专项类型'},
        {'name':'SSLX','type':'TEXT','length':32,'alias':'四上类型'},
        {'name':'RegisterYear','type':'TEXT','length':16,'alias':'注册年份'},
        {'name':'TransferYear','type':'TEXT','length':16,'alias':'迁移年份'},
        {'name':'TransferType','type':'TEXT','length':16,'alias':'迁入迁出状态'}  
    ]} 
]


wkid=2362
sr=arcpy.SpatialReference(wkid)
gdbPath=r"d:\temp"
gdbName="bigData.gdb"
ws=gdbPath + '\\'+  gdbName

print '......CreateFileGDB.......'
print ws
arcpy.CreateFileGDB_management(gdbPath,gdbName)
print '......CreateFileGDB Success......\n'
# Set environment settings
env.workspace = ws

for lyr in info:
    layerName=lyr['layerName']
    layeralias=lyr['layeralias']
    geometry=lyr['geometry']
    
    print '......CreateLayer......' 
    print layerName+":"+layeralias
    arcpy.CreateFeatureclass_management(ws,layerName,geometry,spatial_reference=sr)
    print '......CreateLayer Success......\n'

    print "......"+layerName+":"+layeralias+' Add fields......'
    for field in lyr['fields']:
        fieldname=field['name']
        fieldtype=field['type']
        fieldalias=field['alias']
        if fieldtype=='TEXT':
            fieldlength=field['length']
            arcpy.AddField_management(layerName,fieldname,fieldtype,field_length=fieldlength,field_alias=fieldalias)
        if fieldtype=='LONG' or fieldtype=='SHORT':
             arcpy.AddField_management(layerName,fieldname,fieldtype,field_alias=fieldalias)
        if fieldtype=='DOUBLE':
            fieldprecision=field['precision']
            fieldscale=field['scale']
            arcpy.AddField_management(layerName,fieldname,fieldtype,field_precision=fieldprecision,field_scale=fieldscale,field_alias=fieldalias)   
        print fieldname+":"+fieldalias  
    print "......"+layerName+":"+layeralias+' Add fields Success\n' 

print '......task had done!'

