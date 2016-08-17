import arcpy

workspace = r'd:\temp'
gdbName="test.gdb"
gdbPath=workspace+gdbName
featureclassName = "rivers"

print "Creating output FileGDB..."
arcpy.CreateFileGDB_management(workspace, gdbName)


spatial_ref = arcpy.SpatialReference(2362)

print "Creating output Featureclass..."
arcpy.CreateFeatureclass_management( gdbPath, featureclassName, "POLYGON", None, None, None, spatial_ref)

#  print "  Adding field(s)..."
# arcpy.AddField_management( Featureclass, "EventDate", "DATE", None, None, None, None, "NULLABLE", "NON_REQUIRED")
# arcpy.AddField_management( Featureclass, "Scale", "DOUBLE", 19, 2, None, None, "NULLABLE", "NON_REQUIRED")
# arcpy.AddField_management( Featureclass, "InvScale", "DOUBLE", 19, 12, None, None, "NULLABLE", "NON_REQUIRED")
# arcpy.AddField_management( Featureclass, "Width", "LONG", 9, None, None, None, "NULLABLE", "NON_REQUIRED")
# arcpy.AddField_management( Featureclass, "Height", "LONG", 9, None, None, None, "NULLABLE", "NON_REQUIRED")

