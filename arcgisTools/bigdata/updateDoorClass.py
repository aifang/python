# coding=utf-8
# 随机生成企业税收、产值，年份，门类
import arcpy
from arcpy import env

# important 用arcmap编辑必须注册版本，用代码编辑必须取消版本注册
env.workspace = "D:/Sharp Map/白云区地图/bigData/bigData.gdb"


lyrEnterpriseInfos = 'outputAndTax'
# lyrEnterpriseInfos = '化妆品产业分布'

fields = ['DOORCALSS', 'KXCLASS', 'OBJECTID']  # 产业，行业代码

car1 = ['采矿业', '制造业', '电力、热力、燃气及水生产和供应']  #工业
car2 = ['批发和零售业', '住宿和餐饮业']  #商业
car3 = ['交通运输、仓储和邮政业', '信息传输、软件和信息技术服务业', '租赁和商务服务业', '居民服务、修理和其他服务业', '文化、体育和娱乐业']  #营利性服务业
car4 = ['农、林、牧、渔业']  #农、林、牧、渔业
car5 = ['建筑、房地产业']  #建筑、房地产业
car6 = ['货币金融服务', '资本市场服务', '保险业', '其他金融业']  #金融业
car7 = ['研究和试验发展', '专业技术服务业', '科技推广和应用服务业']  # 科学研究和技术服务业
car8 = ['水利、环境和公共设施管理业']  #水利、环境和公共设施管理业
car9 = ['教育']  #教育
car10 = ['卫生和社会工作']  #卫生和社会工作
car11 = ['公共管理、社会保障和社会组织']  #公共管理、社会保障和社会组织
car12 = ['国际组织']  #国际组织
car13 = ['新业态行业']  #新业态行业

def getProductType(hycode):
    productType = None
    if hycode==None or hycode.strip() == "":
        return productType
    hycode = hycode.strip()
    if hycode in car1:
        productType = '工业'
    if hycode in car2:
        productType = '商业'
    if hycode in car3:
        productType = '营利性服务业'
    if hycode in car4:
        productType = '农、林、牧、渔业'
    if hycode in car5:
        productType = '建筑、房地产业'
    if hycode in car6:
        productType = '金融业'
    if hycode in car7:
        productType = '科学研究和技术服务业'
    if hycode in car8:
        productType = '水利、环境和公共设施管理业'
    if hycode in car9:
        productType = '教育'
    if hycode in car10:
        productType = '卫生和社会工作'
    if hycode in car11:
        productType = '公共管理、社会保障和社会组织'
    if hycode in car12:
        productType = '国际组织'
    if hycode in car13:
        productType = '新业态行业'
    return productType

def doABC():
    count=0
    count1=0
    with arcpy.da.UpdateCursor(lyrEnterpriseInfos, field_names=fields) as cursor:
        for row in cursor:
            count=count+1
            productType = getProductType(row[0])
            if productType == None:
                continue
            row[1] = productType
            # print(row[0]+" : "+row[1])
            cursor.updateRow(row)
            count1=count1+1
    print (count)
    print (count1)
    print('Province over')


doABC()


