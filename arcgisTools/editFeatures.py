#coding=utf-8
# import arcpy
# from arcpy import env

# fc=arcpy.UpdateCursor("E:/FHwork/时间演变开发/企业分布图point/bigData.gdb/EnterpriseData/EnterpriseInfos")
# for row in fc:
#     # print row.getValue("EnterpriseName")
#     row.setValue("EnterpriseSSType","四上企业")
#     fc.updateRow(row)
# del row
# del fc


import arcpy
import xlrd  
import xlwt    
  
xlsPath = r"D:\地图\地图底图\duobianxing.xls"  
data = xlrd.open_workbook(xlsPath)  
  
table = data.sheets()[0]#通过索引顺序获取  
cols = table.col_values(7)#该数值需要调整  
nrows = table.nrows  
point = arcpy.Point()  
array = arcpy.Array()  
  
polygonGeometryList = []  
for i in range(1,nrows):  
    str = table.cell(i,7).value#该处i后的数值应该是需要调整的  
    points = str.split(u' ')  
    for j in points:  
        xy = j.split(',')  
        print xy[0]  
        print xy[1]  
        print '\n'  
        point.X = float(xy[0]);point.Y = float(xy[1])  
        array.add(point)  
    polygon = arcpy.Polygon(array)  
    polygonGeometryList.append(polygon)  
    array.removeAll()  
arcpy.CopyFeatures_management(polygonGeometryList, "D:\\地图\地图底图\heshimian.shp")
  
print 'over'  
