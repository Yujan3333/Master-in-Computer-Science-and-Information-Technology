Assignment # 2
Deadline- 30 April 2026

1. Define visual image interpretation. Describe basic elements of visual image
interpretation in remote sensing with illustrations.
- [Visual Image Interpretation](RGIS-assignment-notes/Visual%20Image%20Interpretation.md)

2. Explain the importance of scale in satellite image interpretation and discuss how
changes in scale influence the identification and classification of geographic features.
Define image interpretation keys and describe the major elements used in visual image
interpretation, such as tone/color, texture, shape, size, pattern, shadow, site, and
association. Give examples.
- [Scale in satellite  image Interpretation](RGIS-assignment-notes/Scale%20in%20satellite%20%20image%20Interpretation.md)

3. Describe the various types of image preprocessing techniques. What would be the
advantage of geometrically correcting an image to geographic coordinates prior to
further analysis and interpretation?
- [Image preprocessing Techniques](RGIS-assignment-notes/Image%20preprocessing%20Techniques.md)

4. Discuss various image enhancement techniques used in digital image processing.
Explain the importance of spatial filtering in image enhancement and describe how
different filters can be applied to modify the spatial frequency characteristics of an
image, with suitable examples.
- [Image Enhancement Techniques in Digital Image Processing](RGIS-assignment-notes/Image%20Enhancement%20Techniques%20in%20Digital%20Image%20Processing.md)

4. Explain the commonly used digital image processing functions with appropriate
illustrations. Furthermore, differentiate between supervised classification and
unsupervised classification in image analysis, highlighting their principles, workflow,
advantages, and limitations
- [Digital Image Processing Functions](RGIS-assignment-notes/Digital%20Image%20Processing%20Functions.md)

6. Export the location of School data of Kathmandu Valley from openstreetmap to QGIS.
	(i) Identify all schools located within a 2 km radius of the Department of Chemistry, Tribhuvan University. 
	ii. Create a map layer and a corresponding database table for schools located within the boundaries of Kathmandu Metropolitan City. 
	iii. Determine the number of schools situated within a 1 km buffer of the Ring Road. Develop a separate map layer and database table for these schools.

(Hint: To Download OSM Data Go to
https://www.overpass-turbo.eu/
Click on Wizard
Search (if don't know search name, go https://wiki.openstreetmap.org/ to know tag
name)
amenity=school in Kathmandu
Build and run queryExport in required format
Add school data in QGIS
Two theme display (point and poly).
Convert poly to point using geometry tool - Centroid (will get center point of each poly)
Merge intial point feature and new point from poly using merge tool
To solve above questions, please use municipal boundary map and road network map.)
- [RGIS-Lab-2](RGIS-assignment-notes/RGIS-Lab-2.md)


![](../../../../../Images/Third_Sem_Images/RGIS%20Assignment-2.pdf)
