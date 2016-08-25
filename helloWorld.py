import  arcpy

polygon = "c:/base/data.gdb/roads"
point = "c:/base/data.gdb/roads_point"
arcpy.FeatureVerticesToPoints_management(polygon,point,"All")


arcpy.SearchCursor(dataset, {where_clause}, {spatial_reference}, {fields}, {sort_fields})
arcpy.UpdateCursor(dataset, {where_clause}, {spatial_reference}, {fields}, {sort_fields})

cursor = arcpy.da.SearchCursor(fc, ['fieldA', 'fieldB'])
for row in cursor:
    print(row)

with arcpy.da.SearchCursor(fc, ['fieldA', 'fieldB']) as cursor:
    for row in cursor:   
        print(row)

with arcpy.da.UpdateCursor("c:/base/data.gdb/roads",
                           ["roadtype", "distance"]) as cursor:
    for row in cursor:
        # Update the values in the distance field by multiplying 
        #   the roadtype by 100. Road type is either 1, 2, 3 or 4.
        #
        row[1] = row[0] * 100
        cursor.updateRow(row)
        
# Create update cursor for feature class
lyrPolygons = arcpy.UpdateCursor("c:/data/base.gdb/polygon")
lyrPoint = "c:/data/base.gdb/point"
for rowPoly in rowsPolygons:    
    xyCol=[]
    sql="ORIG_FID='"+rowPoly.getValue("OBJECTID")+"'"
    with arcpy.da.SearchCursor(lyrPoint, ['SHAPE@XY'],sql) as cursor:
    for rowPoint in cursor:   
        xy=rowPoint.getValue('SHAPE')
        xyCol.append(xy);
    rowPoly.setValue("xyField",xyCol)
    rowsPolygons.updateRow(rowPoly)


del rowPoly
del lyrPolygons
