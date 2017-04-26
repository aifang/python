# coding=utf-8

import arcpy
from arcpy import env

# 产税值写入地理企业点信息表
gdbPath = u"D:/Sharp Map/白云区地图/bigData/bigData20170401Update4upTaxAndOutput.gdb"
env.workspace = gdbPath
lyrEnterpriseInfos = 'EnterpriseInfos'
#产值，区域税收，全库税收，企业税收
# fields = ('OUTPUTVALUE' ,'DISTRICTTAX', 'NATIONALTAX', 'ENTERPRISENAME' ,'ZZJGCODE','REGISTERYEAR')
fields = ('OUTPUTVALUE' ,'DISTRICTTAX', 'NATIONALTAX')
fieldsXLSX = ('组织机构代码' ,'企业名称', '最大产值（元）', '年份' ,'税收全库（元）','税收区库（元）')

def noneToNull(value):
    if value==None:
        return None
    else:
        return value

def noneToString(value):
    if value==None:
        return ''
    else:
        return value

def updateHeatmapFieldsValue():
    count=0
    # with arcpy.da.SearchCursor('TaxAndOutputxlsx', fieldsXLSX,where_clause="年份<>'2012'") as cursor:
    with arcpy.da.SearchCursor('TaxAndOutputxlsx', fieldsXLSX) as cursor:
        for row in cursor:
            strOrganizationCode = row[0]   #组织机构代码
            strEnterpriseName=row[1]    #企业名称
            stroutPut=row[2]            #产值
            strYear = row[3]            #四上年份    
            strnationalTax=row[4]       #税收全库
            strdistrictTax=row[5]       #税收区库
            strWhere = "REGISTERYEAR = '" + strYear + "' AND ENTERPRISESSTYPE = '四上企业' and ZZJGCODE='" +strOrganizationCode+"' and ENTERPRISENAME ='"+strEnterpriseName+"'" 
            # strWhere = "REGISTERYEAR = '" + strYear + "' AND ENTERPRISESSTYPE = '四上企业' and ZZJGCODE='" +noneToString(strOrganizationCode)+"' and ENTERPRISENAME ='"+noneToString(strEnterpriseName)+"'" 
            # print(strWhere)
            with arcpy.da.UpdateCursor(lyrEnterpriseInfos, fields, where_clause=strWhere) as pcursor:
                for prow in pcursor:
                    # prow[0]=noneToNull(stroutPut)
                    # prow[1]=noneToNull(strdistrictTax) 
                    # prow[2]=noneToNull(strnationalTax) 
                    if stroutPut!=None and stroutPut!='':
                        prow[0]=stroutPut
                    if strdistrictTax!=None and strdistrictTax!='':
                        prow[1]=strdistrictTax
                    if strnationalTax!=None and strnationalTax!='':
                        prow[2]=strnationalTax
                    # print("企业名称："+strEnterpriseName+ " 年份："+strYear+" 产值：" + noneToString(prow[0])+" 税收全库："+noneToString(prow[1])+" 税收区库："+noneToString(prow[2]))
                    count+=1
                    print("企业名称："+strEnterpriseName+ " 年份："+strYear+" 产值：" + str(prow[0])+" 税收全库："+str(prow[1])+" 税收区库："+str(prow[2])+"总数："+ str(count))
                    pcursor.updateRow(prow)
            # print('单行完成')
    print('所有行完成完成')   


updateHeatmapFieldsValue()