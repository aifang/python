# coding=utf-8

import xlrd
import arcpy
from arcpy import env

# 产税值写入地理企业点信息表
gdbPath = u"D:/Sharp Map/白云区地图/bigData/bigData20170401Update4upTaxAndOutput.gdb"
env.workspace = gdbPath

xlsPath = u"D:/Documents/Tencent Files/183714346/FileRecv/2012-2016年四上企业产值税收数据-热力图.xlsx"


lyrEnterpriseInfos = 'EnterpriseInfos'
#产值，区域税收，全库税收，企业税收
fields = ('OUTPUTVALUE' ,'DISTRICTTAX', 'NATIONALTAX', 'ENTERPRISENAME' ,'ZZJGCODE','REGISTERYEAR')


    
def updateHeatmapFieldsValue():
    workbook = xlrd.open_workbook(xlsPath,formatting_info=True)
    # table = data.sheets()[5]  # 通过索引顺序获取,----各年份汇总
    table = workbook.sheet_by_name('各年份汇总')  # 各年份汇总
    nrows = table.nrows        #sheet表内所有行数据
    for i in range(1, nrows):
        # ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
        strOrganizationCode = table.cell(i, 0).value   #组织机构代码 xlrd.xldate_as_tuple(sheet.cell_value(rows,3),book.datemode)xlrd.(table.cell_value(i, 0),1) #
        strEnterpriseName=table.cell(i, 1).value    #企业名称
        stroutPut=table.cell(i, 4).value            #产值
        strYear = table.cell(i, 5).value            #四上年份    
        strnationalTax=table.cell(i, 6).value       #税收全库
        strdistrictTax=table.cell(i, 7).value       #税收区库
        strWhere = "REGISTERYEAR = '" + strYear + "' AND ENTERPRISESSTYPE = '四上企业' and ZZJGCODE='" +strOrganizationCode+"' and ENTERPRISENAME ='"+strEnterpriseName+"'" 
        print(strWhere)
        with arcpy.da.UpdateCursor(lyrEnterpriseInfos, fields, where_clause=strWhere) as cursor:
            for row in cursor:
                row[0]=stroutPut
                row[1]=strdistrictTax
                row[2]=strnationalTax
                print("企业名称："+row[3]+ " 年份："+strYear+" 产值：" + stroutPut+" 税收全库："+strnationalTax+" 税收区库："+strdistrictTax)
                cursor.updateRow(row)
        # print('单行完成')
    print('所有行完成完成')   

updateHeatmapFieldsValue()