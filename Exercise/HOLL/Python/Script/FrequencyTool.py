import arcpy #import arcgis library

#Dynamic Parameters
arcpy.env.workspace = r'%s' % arcpy.GetParameterAsText(0)  #accept gdb workspace parameter
Polygon = r'%s' % arcpy.GetParameterAsText(1)  #polygon layer parameter
Point = r'%s' % arcpy.GetParameterAsText(2) #point layer parameter
FrequencyField = r'%s' % arcpy.GetParameterAsText(3)  #

#Manually assign parameter values
IntersectLayer = "IntersectLayer" #default intersect layer
PointFrequency = "PointFrequency" #default point frequecy table

#Show message in console of parameters
arcpy.AddMessage(arcpy.env.workspace)
arcpy.AddMessage(Polygon)
arcpy.AddMessage(Point)
arcpy.AddMessage(IntersectLayer)
arcpy.AddMessage(PointFrequency)
arcpy.AddMessage(FrequencyField)

#utilize geoprocessing tools
arcpy.SpatialJoin_analysis(Polygon, Point, IntersectLayer,"JOIN_ONE_TO_MANY", "KEEP_ALL","", "INTERSECT" )
arcpy.Frequency_analysis(IntersectLayer, PointFrequency, FrequencyField)