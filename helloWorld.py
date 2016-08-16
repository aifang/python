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
rows = arcpy.UpdateCursor("c:/data/base.gdb/roads")

# Update the field used in buffer so the distance is based on the
# road type. Road type is either 1, 2, 3 or 4. Distance is in meters.
for row in rows:
    # Fields from the table can be dynamically accessed from the
    # row object. Here fields named BUFFER_DISTANCE and ROAD_TYPE
    # are used
    row.setValue("valueA", row.getValue("ROAD_TYPE") * 100)
    rows.updateRow(row)

# Delete cursor and row objects to remove locks on the data
del row
del rows
