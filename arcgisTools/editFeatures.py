#coding=utf-8
import arcpy
from arcpy import env

fc=arcpy.UpdateCursor("E:/FHwork/时间演变开发/企业分布图point/bigData.gdb/EnterpriseData/EnterpriseInfos")
for row in fc:
    # print row.getValue("EnterpriseName")
    row.setValue("EnterpriseSSType","四上企业")
    fc.updateRow(row)
del row
del fc