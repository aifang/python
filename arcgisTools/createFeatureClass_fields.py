#coding=utf-8
import arcpy
from arcpy import env

info = [
    {'layerName':'GIS_QXJXZQ','layeralias':'区县级行政区','geometry':'POLYGON','fields':[
        {'name':'QXMC','type':'TEXT','length':32,'alias':'区县名称'},
        {'name':'QXDM','type':'TEXT','length':16,'alias':'区县代码'}
    ]},
    {'layerName':'GIS_XZJXZQ','layeralias':'乡镇级（街道）行政区','geometry':'POLYGON','fields':[
        {'name':'XZMC','type':'TEXT','length':32,'alias':'乡镇名称'},
        {'name':'XZDM','type':'TEXT','length':16,'alias':'乡镇代码'}
    ]},
	{'layerName':'GIS_CJXZQ','layeralias':'村级（街坊）行政区','geometry':'POLYGON','fields':[
        {'name':'CJMC','type':'TEXT','length':32,'alias':'村级名称'},
        {'name':'CJDM','type':'TEXT','length':16,'alias':'村级代码'}
    ]},
	{'layerName':'GIS_SHUIXI','layeralias':'水系','geometry':'POLYGON','fields':[
        {'name':'SXMC','type':'TEXT','length':32,'alias':'水系名称'}
    ]},
	{'layerName':'GIS_SHANXI','layeralias':'山系','geometry':'POLYGON','fields':[
        {'name':'SXMC','type':'TEXT','length':32,'alias':'山系名称'}
    ]},
	{'layerName':'GIS_XZJT','layeralias':'性状交通','geometry':'POLYGON','fields':[
        {'name':'JTMC','type':'TEXT','length':32,'alias':'交通名称'}
    ]},
    {'layerName':'GIS_ZD','layeralias':'宗地','geometry':'POLYGON','fields':[
        {'name':'BSM','type':'LONG','alias':'标志码'},
		{'name':'YSDM','type':'TEXT','length':32,'alias':'要素代码'},
		{'name':'ZDDM','type':'TEXT','length':32,'alias':'宗地代码'},
		{'name':'BDCDYH','type':'TEXT','length':32,'alias':'不动产单元号'},
		{'name':'DJH','type':'TEXT','length':32,'alias':'地籍号'},
		{'name':'ZDSZD','type':'TEXT','length':128,'alias':'宗地四至-东'},
		{'name':'ZDSZN','type':'TEXT','length':128,'alias':'宗地四至-南'},
		{'name':'ZDSZX','type':'TEXT','length':128,'alias':'宗地四至-西'},
		{'name':'ZDSZB','type':'TEXT','length':128,'alias':'宗地四至-北'},
		{'name':'TXDZ','type':'TEXT','length':100,'alias':'通信地址'},
		{'name':'ZL','type':'TEXT','length':100,'alias':'坐落'},
		{'name':'QLLX','type':'TEXT','length':4,'alias':'权利类型'},
		{'name':'QLXZ','type':'TEXT','length':8,'alias':'权利性质'},
		{'name':'QLSDFS','type':'TEXT','length':4,'alias':'权利设定方式'},
		{'name':'YT','type':'TEXT','length':8,'alias':'用途'},
		{'name':'DJ','type':'TEXT','length':32,'alias':'土地等级'},
        {'name':'ZDMJ','type':'DOUBLE','precision':15,'scale':2,'alias':'宗地面积'},
		{'name':'MJDW','type':'TEXT','length':4,'alias':'面积单位'},
        {'name':'RJL','type':'DOUBLE','precision':4,'scale':2,'alias':'容积率'},
        {'name':'JZMD','type':'DOUBLE','precision':3,'scale':2,'alias':'建筑密度'},
        {'name':'JZXG','type':'DOUBLE','precision':5,'scale':2,'alias':'建筑限高'},
        {'name':'SBJG','type':'DOUBLE','precision':15,'scale':2,'alias':'申报价格'},
        {'name':'QDJG','type':'DOUBLE','precision':15,'scale':2,'alias':'取得价格'},
		{'name':'QXJXZQDM','type':'TEXT','length':16,'alias':'区县级行政区代码'},
		{'name':'XZJXZQDM','type':'TEXT','length':16,'alias':'乡镇级行政区代码'},
		{'name':'CJXZQDM','type':'TEXT','length':16,'alias':'村级行政区代码'},
		{'name':'ZDT','type':'TEXT','length':512,'alias':'宗地图'},
		{'name':'TFH','type':'TEXT','length':56,'alias':'图幅号'},
		{'name':'DAH','type':'TEXT','length':128,'alias':'档案号'},
		{'name':'BGBH','type':'TEXT','length':32,'alias':'变更编号'},
		{'name':'ZT','type':'TEXT','length':4,'alias':'状态'}
    ]},
	{'layerName':'GIS_LD','layeralias':'楼栋','geometry':'POLYGON','fields':[
        {'name':'BSM','type':'LONG','alias':'标志码'},
		{'name':'YSDM','type':'TEXT','length':10,'alias':'要素代码'},
		{'name':'ZDDM','type':'TEXT','length':32,'alias':'宗地代码'},
		{'name':'BDCDYH','type':'TEXT','length':32,'alias':'不动产单元号'},
		{'name':'ZRZH','type':'TEXT','length':32,'alias':'自然幢号'},
		{'name':'XMMC','type':'TEXT','length':32,'alias':'项目名称'},
		{'name':'JZWMC','type':'TEXT','length':100,'alias':'建筑物名称'},
		{'name':'JGRQ','type':'Date','alias':'竣工日期'},
		{'name':'JZWGD','type':'DOUBLE','precision':15,'scale':2,'alias':'建筑物高度'},
		{'name':'ZZDMJ','type':'DOUBLE','precision':15,'scale':3,'alias':'幢占地面积'},
		{'name':'YCJZMJ','type':'DOUBLE','precision':15,'scale':3,'alias':'预测建筑面积'},
		{'name':'SCJZMJ','type':'DOUBLE','precision':15,'scale':3,'alias':'实测建筑面积'},
		{'name':'ZCS','type':'SHORT','alias':'总层数'},
		{'name':'DSCS','type':'SHORT','alias':'地上层数'},
		{'name':'DXCS','type':'SHORT','alias':'地下层数'},
		{'name':'DXSD','type':'DOUBLE','precision':15,'scale':3,'alias':'地下深度'},
		{'name':'GHYT','type':'TEXT','length':4,'alias':'规划用途'},
		{'name':'FWJG','type':'TEXT','length':4,'alias':'房屋结构'},
		{'name':'ZTS','type':'SHORT','alias':'总套数'},
		{'name':'JZWJBYT','type':'TEXT','length':100,'alias':'建筑物基本用途'},
		{'name':'DAH','type':'TEXT','length':100,'alias':'档案号'},
		{'name':'QXJXZQDM','type':'TEXT','length':16,'alias':'区县级行政区代码'},
		{'name':'XZJXZQDM','type':'TEXT','length':16,'alias':'乡镇级行政区代码'},
		{'name':'CJXZQDM','type':'TEXT','length':16,'alias':'村级行政区代码'},
		{'name':'BGBH','type':'TEXT','length':32,'alias':'变更编号'},
		{'name':'ZT','type':'TEXT','length':4,'alias':'状态'}
    ]},
	{'layerName':'GIS_FW','layeralias':'房屋','geometry':'POLYGON','fields':[
        {'name':'BDCDYH','type':'TEXT','length':32,'alias':'不动产单元号'},
        {'name':'ZDDM','type':'TEXT','length':32,'alias':'宗地代码'},
        {'name':'FWBM','type':'TEXT','length':32,'alias':'房屋编号'},
        {'name':'FWMC','type':'TEXT','length':32,'alias':'房屋名称'},
        {'name':'YSDM','type':'TEXT','length':32,'alias':'要素代码'},
        {'name':'ZRZH','type':'TEXT','length':32,'alias':'自然幢号'},
        {'name':'LJZH','type':'TEXT','length':32,'alias':'逻辑幢号'},
        {'name':'CH','type':'TEXT','length':10,'alias':'层号'},
        {'name':'ZL','type':'TEXT','length':128,'alias':'坐落'},
        {'name':'MJDW','type':'TEXT','length':4,'alias':'面积单位'},
		{'name':'SJCS','type':'SHORT','alias':'实际层数'},
		{'name':'HH','type':'SHORT','alias':'户号'},
		{'name':'SHBW','type':'Text','length':4,'alias':'室号部位'},
		{'name':'HX','type':'Text','length':32,'alias':'户型'},
		{'name':'HXJG','type':'Text','length':4,'alias':'户型结构'},
		{'name':'FWYT','type':'Text','length':4,'alias':'房屋用途'},
		{'name':'YCJZMJ','type':'DOUBLE','precision':15,'scale':2,'alias':'预测建筑面积'},
		{'name':'YCTNJZMJ','type':'DOUBLE','precision':15,'scale':2,'alias':'预测套内建筑面积'},
		{'name':'YCFTJZMJ','type':'DOUBLE','precision':15,'scale':2,'alias':'预测分摊建筑面积'},
		{'name':'YCDXBFJZMJ','type':'DOUBLE','precision':15,'scale':2,'alias':'预测地下部分建筑面积'},
		{'name':'YCQTJZMJ','type':'DOUBLE','precision':15,'scale':2,'alias':'预测其它建筑面积'},
		{'name':'YCFTXS','type':'DOUBLE','precision':15,'scale':2,'alias':'预测分摊系数'},
		{'name':'SCJZMJ','type':'DOUBLE','precision':15,'scale':2,'alias':'实测建筑面积'},
		{'name':'SCTNJZMJ','type':'DOUBLE','precision':15,'scale':2,'alias':'实测套内建筑面积'},
		{'name':'SCFTJZMJ','type':'DOUBLE','precision':15,'scale':2,'alias':'实测分摊建筑面积'},
		{'name':'SCDXBFJZMJ','type':'DOUBLE','precision':15,'scale':2,'alias':'实测地下部分建筑面积'},
		{'name':'SCQTJZMJ','type':'DOUBLE','precision':15,'scale':2,'alias':'实测其它建筑面积'},
		{'name':'SCFTXS','type':'DOUBLE','precision':15,'scale':2,'alias':'实测分摊系数'},
		{'name':'GYTDMJ','type':'DOUBLE','precision':15,'scale':2,'alias':'共有土地面积'},
		{'name':'FTTDMJ','type':'DOUBLE','precision':15,'scale':2,'alias':'分摊土地面积'},
		{'name':'DYTDMJ','type':'DOUBLE','precision':15,'scale':2,'alias':'独用土地面积'},
		{'name':'FWLX','type':'TEXT','length':4,'alias':'房屋类型'},
		{'name':'FWXZ','type':'TEXT','length':4,'alias':'房屋性质'},
		{'name':'QXJXZQDM','type':'TEXT','length':16,'alias':'区县级行政区代码'},
		{'name':'XZJXZQDM','type':'TEXT','length':16,'alias':'乡镇级行政区代码'},
		{'name':'CJXZQDM','type':'TEXT','length':16,'alias':'村级行政区代码'},
		{'name':'BGBH','type':'TEXT','length':32,'alias':'变更编号'},
		{'name':'ZT','type':'TEXT','length':4,'alias':'状态'}
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

