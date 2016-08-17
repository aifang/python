#coding=utf-8
import arcpy
from arcpy import env

info = [    
    {'layerName':'GIS_QXJXZQ','layeralias':'区县级行政区','geometry':'POLYGON','fields':[
        {'name':'qxmc','type':'TEXT','length':32,'alias':'区县名称'},
        {'name':'qxdm','type':'TEXT','length':16,'alias':'区县代码'}
    ]},
    {'layerName':'GIS_XZJXZQ','layeralias':'乡镇级（街道）行政区','geometry':'POLYGON','fields':[
        {'name':'xzmc','type':'TEXT','length':32,'alias':'乡镇名称'},
        {'name':'xzdm','type':'TEXT','length':16,'alias':'乡镇代码'}
    ]},
     {'layerName':'GIS_ZD','layeralias':'宗地','geometry':'POLYGON','fields':[
        {'name':'BSM','type':'LONG','alias':'标志码'},
        {'name':'BSM1','type':'SHORT','alias':'标志码1'},
        {'name':'ZDMJ','type':'DOUBLE','precision':15,'scale':2,'alias':'乡镇代码'}
    ]}
]


wkid=2362
sr=arcpy.SpatialReference(wkid)
gdbPath=r"d:\temp"
gdbName="test.gdb"
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

