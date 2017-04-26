#!/usr/bin/env python
# coding=utf-8
# 从新叠加2017年的行政区到企业所属街镇
import arcpy
from arcpy import env

# important 用arcmap编辑必须注册版本，用代码编辑必须取消版本注册
gdbPath = "D:/Sharp Map/白云区地图/bigData/bigData20170319updateXZQ.gdb"
env.workspace = gdbPath
lyrEnterpriseInfos = 'EnterpriseInfos'
lyrcustomExtents = ['bykgjjq', 'bymky', 'byxc', 'gzgjjkcyc', 'LXH']   #用于叠加的图层
lryOuts = [ 'EnterpriseInfosbykgjjq', 'EnterpriseInfosbymky', 'EnterpriseInfosbyxc', 'EnterpriseInfosgzgjjkcyc', 'EnterpriseInfosLXH']  #叠加输出的图层名
newFieldName = 'customExtent'


def startTask():
    addCustomExtentField(lyrEnterpriseInfos,newFieldName)
    addCustomExtentFieldAndSetValueForAllCustomLayer(lyrcustomExtents,newFieldName)
    intersectAnalysis()
    insertToCustomExtentField(lryOuts,lyrEnterpriseInfos,newFieldName)

# 1.先添加字段
def addCustomExtentField(lyrName, newFieldName):
    arcpy.AddField_management(lyrName, newFieldName, "TEXT", field_alias='自定义区域')
    print('添加customExtent(自定义区域) 字段成功')


# 2.添加字段并设置默认值到自定义区域的各个图层
def addCustomExtentFieldAndSetValueForAllCustomLayer(lyrs, newFieldName):
    defValues = ['白云空港经济区', '民科园', '白云新城', '广州国际健康产业城', '流溪河1公里缓冲']
    for index in range(len(lyrs)):
        arcpy.AddField_management(lyrs[index], newFieldName, "TEXT", field_alias='自定义区域')
        with arcpy.da.UpdateCursor(lyrs[index], newFieldName) as cursor:
            count = 0
            for row in cursor:
                row[0] = defValues[index]
                cursor.updateRow(row)
                count += 1
                print lyrs[index] + "=" + defValues[index] + ' ' + str(count)
    print('所有值写入自定义区域图层默认自写入完毕')


# 3.叠加自定义区域和企业点，输出新图层
def intersectAnalysis(outputType="POINT"):
    for lyr in lyrcustomExtents:
        lyrOut = lyrEnterpriseInfos + lyr
        arcpy.Intersect_analysis( [lyr, lyrEnterpriseInfos], lyrOut, output_type=outputType)
        print '已叠加 ' + lyrOut
    print lryOuts  # 方便直接使用
    print('叠加输出完成')


# 4.插入自定义区域字段
def insertToCustomExtentField(lryOuts, lyrWrite, sameField):
    count=0
    for lryRead in lryOuts:
        with arcpy.da.SearchCursor(lryRead, ['FID_EnterpriseInfos',sameField]) as cursor:
            for row in cursor:
                where = 'objectid' + "=" + str(row[0]) 
                with arcpy.da.UpdateCursor(lyrWrite, where_clause=where,field_names=sameField) as pcursor:
                    for prow in pcursor:
                        if prow[0]==None:
                            prow[0] = row[1]
                        else:
                            prow[0]+=","+row[1]
                        pcursor.updateRow(prow)
                        print prow[0]  +"  "+  str(row[0]) 
        count+=1
        print(lryRead + ' 插入数据完成  '+ str(count))
    print('完成所有插入数据')

# 开始执行
startTask()
