#rgis #third-semester 

# Remote Sensing and GIS (CSC-624) — Lecture Notes Summary
---

## Unit 1: Concept of Remote Sensing (4 hrs)

**Basics**: RS is defined as acquiring information about an object/area without physical contact, viewed as both an art and a science. Types by scope include satellite RS, photography/photogrammetry, thermal RS, radar RS, and LiDAR.

**RS Process**: energy source → interaction with atmosphere → interaction with target → recording by sensor → transmission/reception/processing → interpretation and analysis → applications.

**Electromagnetic (EM) Spectrum**: the range of wavelengths (gamma to radio) that sensors detect and that interacts with targets — foundational to understanding what any sensor can "see."

**Passive vs Active RS**:
- *Passive* sensors detect naturally available energy (e.g., reflected sunlight).
- *Active* sensors supply their own energy source (e.g., radar, police speed guns). A camera can act as either.

**Image vs Photograph**: an *image* is any pictorial representation of recorded EM energy; a *photograph* specifically uses photographic film (0.3–0.9 µm range). Digital images subdivide into pixels, each holding a brightness value. All photographs are images, not all images are photographs.

**Platforms**: ground-borne (vehicles, towers), air-borne (drones, balloons, aircraft), and space-borne (satellites).

**Satellite Characteristics**:
- *Geostationary orbits* (~36,000 km): match Earth's rotation, continuous coverage of a fixed area, but low spatial resolution and poor polar coverage.
- *Near-polar/sun-synchronous orbits*: north–south path, consistent local time coverage.
- *Swath*: the ground area covered by the sensor, ranging from tens to hundreds of km wide.

**Sensor Resolutions** (four types):
- Spectral — which wavelengths are measured
- Radiometric — how precisely intensity is measured
- Spatial — the size of the smallest resolvable feature
- Temporal — how frequently the same area is revisited

---

## GIS Fundamentals

**What is GIS?**: A specialized DBMS that stores not just attribute data but the spatial location/shape of geographic features (points, lines, areas, pixels, TINs). Formally: computer hardware + software + people + geographic data used to capture, store, manipulate, analyze, manage, and present spatial data.

**Components of GIS**: hardware, software (input/manipulation tools, DBMS, analysis/query tools, GUI), spatial data (often the most expensive component), trained personnel, and methods.

**Benefits of GIS**: cost savings through efficiency, improved communication, better decision-making, better record keeping, and the ability to manage things "geographically."

**History of GIS** (four phases: early 1960s–mid 1970s; mid 1970s–early 1980s; 1982–late 1980s; late 1980s–present):
- *Origins of spatial analysis*: Charles Picquet's 1832 cholera map of Paris (early heat map); John Snow's 1854 London cholera map using point locations.
- *1960s*: Canada's CGIS — first computer-based map overlay system for land management, limited by primitive computing power.
- *Academia*: Harvard's SYMAP — first real demonstration of computerized thematic mapping.
- *US Census Bureau*: built digital street maps and hierarchical reporting (address → block → tract); 1970 census included a digital map.
- *Industry*: ESRI founded 1969 (environmental consulting, needed digital mapping tools); Intergraph founded 1969 as M&S Computing (CAD/CAM), renamed 1980.

**Applications of GIS**: broad cross-sector uses (urban planning, resource management, disaster response, etc. — shown via example slides).

**Digital Mapping Concepts**:
- A map is a representation of all/part of an area, usually on a flat surface.
- *Real maps* (hard copy) vs *virtual maps* (digital/mental representations).
- Benefits: recording/storing info, analyzing spatial patterns, communicating findings.
- *Map scale*: the reduction ratio from real world to paper. *Resolution*: how accurately features can be depicted at that scale.

**Geographic Features and Attributes**:
- Geography studies where features are located; geographic coordinate systems (latitude/longitude) pinpoint exact positions (e.g., Kathmandu 27.7172°N, 85.3240°E).
- *Georeferencing/geocoding*: assigning coordinates to features.
- Feature representations: points, lines, polygons (vector) and rasters (grid cells), each pairable with tabular attribute data.

**Map Elements**: data frame, title, legend, scale, north arrow, projection system, grid, and source/citation.

**Geographic Phenomena and Spatial Modeling**:
- *Geographic fields*: phenomena measurable everywhere in a study area — continuous (temperature, elevation) or discrete (land use, soil class).
- *Geographic objects*: phenomena occurring only in specific localities. Natural phenomena tend to be fields; man-made phenomena tend to be objects.

---

## Spatial Data Models

**Vector vs Raster**: vector represents the world as discrete points/lines/polygons; raster represents it as a grid of cells (pixels), each with a value.

**Vector Data Model & Topology**: covers how vector features relate spatially (adjacency, connectivity, containment) — topology components and how different GIS formats (e.g., shapefile vs geodatabase) handle topological relationships differently.

**Geospatial Data Analysis — Vector**:
- *Overlay operations*: combining multiple vector layers to derive new information.
  - Point-in-polygon, line-in-polygon, polygon-in-polygon overlays.
  - Basic overlay cases: Clip, Intersection, Union.
  - Common vector overlay problems (e.g., sliver polygons from imprecise boundaries).

**Geospatial Data Analysis — Raster/Image**:
- *Image-based overlay*: simple addition, Boolean combine, composite combine of raster layers.
- **Types of raster operations**:
  1. **Local operations** — cell-by-cell computation.
     - Single image: arithmetic/log/trig/power functions; unit conversion (e.g., slope % → degrees); one-to-one or range reclassification.
     - Multiple images ("map algebra"): summing/averaging layers, and the *combine* operation (unique output code per unique combination of inputs).
  2. **Neighborhood (focal) operations** — value depends on a focal cell plus its surrounding cells (rectangle, circle, annulus, wedge neighborhoods); used for terrain analysis, image processing, site selection, data simplification.
  3. **Zonal operations** — work on groups of cells (zones) that share a value/feature, even if non-contiguous; can summarize geometry (area, perimeter, centroid) of a single-image zone, or summarize an input image's values within zones defined by a second image.
  4. **Resampling** — interpolation methods (nearest neighbor, bilinear, cubic) to re-derive pixel values, typically when changing resolution/projection.
  5. **Aggregate operations** — statistical downsampling (sum, min, max, mean, median) to produce a coarser-resolution raster.
  6. **Distance measurement** — straight-line distance between cell centers.
  7. **Clip and mosaic** — clipping a raster to a mask/analysis boundary; mosaicking multiple rasters together.
  8. **Image data extraction** — pulling values from within a defined area (e.g., a circle), nulling everything outside it.

**Customizing QGIS with Python**: Python can be used in QGIS via the Python Console, startup scripts, custom expressions/actions, new processing algorithms, plugins, and standalone applications. Slides demonstrate issuing console commands, creating a new vector point layer with attributes, and writing a processing script.

---

## Coordinate Systems, Projections, and GNSS

**Coordinate System Basics**:
- *Horizontal coordinate systems* locate data across the Earth's surface (geographic, projected, or local).
- *Vertical coordinate systems* locate height/depth — gravity-based (mean sea level) or ellipsoidal.
- *Cartesian coordinate systems*: orthogonal axes intersecting at an origin, used for 2D projected space.
- *Geographic coordinates*: latitude (±90° from equator) and longitude (±180° from Greenwich meridian) — angular measurements on a sphere.

**Map Projections**: defined by name, type (e.g., cylindrical), description/parameters, and ellipsoid/datum. Mapping requires: (1) a mathematical model of the Earth (spheroid/ellipsoid), (2) a datum relating that model to real-world features, and (3) a projection to flatten the Earth onto a map with minimal distortion, using a coordinate grid. Different regions use different ellipsoids because the Earth isn't perfectly symmetric.

**UTM (Universal Transverse Mercator)**: the most widely used large-scale mapping projection; a transverse cylindrical projection divided into 60 zones of 6° longitude each, with the central meridian scaled to <1 and offset to 500,000 m to minimize distortion.

**GNSS/GPS**:
- GNSS = space-based satellite navigation for precise, automatic positioning.
- **GPS** (US NAVSTAR): developed by the US DoD (~$12 billion), history from 1973 proof-of-concept through full constellation (1995), Selective Availability turned off in 2000, GPS III modernization from 2017; ~31 satellites orbiting at ~12,000 miles, twice daily.
- **Other GNSS**: GLONASS (Russia, degraded but being restored with India), Galileo (EU + partners), BeiDou/Compass (China).
- **Four primary GPS functions**: position/coordinates, distance & direction between waypoints, travel progress reports, accurate time.
- **Three GPS components/segments**:
  - *Space segment*: ~32 satellites at ~20,200 km, arranged in 6 orbital planes, 8.5-year average lifespan, each carrying atomic clocks.
  - *Control segment*: ground stations (master control at Falcon AFB, monitor stations worldwide) that track and correct satellite orbits/clocks.
  - *User segment*: GPS receivers (antenna, processor, stable clock).
- **How GPS works**: uses *trilateration* — measuring distances to multiple satellites simultaneously to compute a precise position.

---

## Visual Image Interpretation

- **Definition**: extracting qualitative/quantitative information from photos or satellite images via human visual perception; used across geography, geology, agriculture, forestry, urban planning, defense, etc.
- **Manual vs digital interpretation**:
  - *Manual*: little special equipment needed, but limited to few images/bands at once and is subjective (varies between interpreters).
  - *Digital*: needs specialized/expensive equipment, but can process many bands/large datasets quickly, and is more objective/consistent.
- **Eight elements of visual interpretation** (ordered from basic to complex): tone/colour, shape, size, texture, site, shadow, association, pattern.
  - *Tone/colour*: relative brightness — depends on radiation, surface properties, composition (e.g., calm water appears dark, turbid water lighter).
  - *Shape*: outline of objects — straight edges suggest man-made features, irregular edges suggest natural features.
  - *Size*: relative to scale and other objects, aids quick target identification.
  - *Texture*: tonal variation frequency — rough (e.g., forest canopy) vs smooth (e.g., fields); especially key in radar imagery.
  - *Site*: topographic position/context (e.g., sewage plants near rivers).
  - *Shadow*: reveals object height/shape via sun angle — useful for tall structures, less useful for satellite imagery due to viewing angle.
  - *Association*: relationship between an object and its surroundings (e.g., a lake associated with boats/marinas).
  - *Pattern*: repetitive spatial arrangement (e.g., orchards, planned housing).
- **Image interpretation keys**: criteria combining the elements above.
  - *Selective keys*: example-based, showing representative images for chosen features.
  - *Elimination keys*: step-by-step decision-tree approach, eliminating options based on visual cues (a worked example distinguishes water body → urban → forest → agriculture → wetland/bare soil).

---

## Digital Image Processing

Four categories of digital image processing functions:

1. **Preprocessing** — required before analysis; radiometric and geometric corrections.
   - *Radiometric correction*: fixes sensor irregularities/noise (atmospheric correction/haze removal, sensor calibration, sun-angle normalization).
   - *Striping/destriping*: parallel-line artifacts from sensor calibration errors/aging hardware, corrected via statistical adjustment, spatial filtering, or Fourier analysis.
   - *Geometric correction*: fixes sensor-Earth geometry distortion; includes orthorectification, registration to map projections, and use of Ground Control Points (GCPs).
2. **Image enhancement** — improves visual appearance without adding new information (contrast stretching, edge enhancement, noise reduction, band combination) to make features more distinguishable.
3. **Image transformation** — combines multiple spectral bands via arithmetic operations (band ratioing, principal components analysis) to highlight features better than any single band.
4. **Image classification and analysis** — assigns each pixel to a class/theme based on statistical brightness characteristics; two generic approaches: **supervised** and **unsupervised classification**.

---

## Microwave Remote Sensing

- Uses wavelengths from 1 cm to 1 m; can observe through clouds/rain (all-weather) and penetrate deeper into vegetation/soil than visible/infrared.
- **Band naming** (short to long wavelength): Ka/K/Ku (early airborne radar, now uncommon), X-band (military/terrain mapping), C-band (CCRS Convair, NASA AirSAR, ERS-1/2, RADARSAT), S-band (Russian ALMAZ), L-band (SEASAT, JERS-1), P-band (longest, NASA experimental).
- **Advantages**: time- and weather-independent, sensitive to soil/vegetation/snow moisture, enhances surface roughness/relief detection, can penetrate cover, can image far from the flight path.
- **Passive microwave RS**: detects naturally emitted microwave energy (related to temperature/moisture); used in meteorology, hydrology, oceanography — atmospheric water/ozone content, soil moisture, sea ice/currents/winds, oil-slick detection.
- **Active microwave RS**: sensor supplies its own microwave energy; works day/night, largely immune to smoke/haze/fog/rain/snow; divided into imaging (RADAR) and non-imaging sensors.

**RADAR Imaging**:
- Components: transmitter, receiver, antenna, processing/recording electronics. Measures time delay between pulse transmission and backscattered echo to determine target distance/location.
- *Airborne radar*: flexible look angles/directions, can operate anytime weather permits, but affected by aircraft motion.
- *Space-borne radar*: stable, predictable orbital geometry, faster large-area coverage, but less flexible viewing geometry; narrower incidence-angle range (~5–15°) than airborne (~60–70°).
- **Range and azimuth resolution**: Range = (c × t)/2; range resolution ΔR = c/(2B); azimuth resolution ≈ R × θ (depends on beamwidth).
- **RAR vs SAR**:
  
| Feature                    | RAR (Real Aperture Radar)                             | SAR (Synthetic Aperture Radar)                                                 |
| -------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Definition**             | Uses the physical antenna to determine resolution     | Uses platform motion to create a virtual (synthetic) antenna                   |
| **Antenna**                | Real (physical)                                       | Synthetic (virtual)                                                            |
| **Azimuth Resolution**     | Lower; depends on antenna length and range            | High; nearly independent of range                                              |
| **Need for Large Antenna** | Yes                                                   | No                                                                             |
| **Signal Processing**      | Minimal                                               | Advanced digital processing                                                    |
| **Image Quality**          | Lower                                                 | Higher                                                                         |
| **Cost**                   | Lower                                                 | Higher                                                                         |
| **Complexity**             | Simple                                                | Complex                                                                        |
| **Applications**           | Weather radar, air traffic control, marine navigation | Earth observation, terrain mapping, disaster monitoring, military surveillance |

  
- Slide deck also lists example research topics combining RS/GIS with AI/ML (forest fire prediction, land cover classification, urban growth change detection, flood risk mapping, air quality prediction, etc. — several Nepal/Kathmandu-focused).

---

## Photographic and Digital Imaging

- **Cameras/aerial photography**: the oldest, simplest RS sensors; framing systems capturing near-instantaneous snapshots via a lens focusing onto a focal plane.
- Photographic film is sensitive ~0.3–0.9 µm (UV, visible, near-IR). Panchromatic film captures all visible light as black-and-white — the most common aerial film type.
- **Digital cameras**: use CCD arrays converting photons to electronic charge proportional to brightness, producing a digital number per pixel per band. Advantages: faster turnaround, better spectral resolution control, spatial resolution as fine as ~0.3 m and spectral resolution 0.012–0.3 mm; pixel arrays typically range 512×512 to 2048×2048.

**Medical Scanning Techniques** *(used as a cross-domain analogy for imaging principles)*:
- *Ultrasound*: sends 1–5 MHz sound waves, reflected boundaries recorded via time-of-flight; no radiation, poor resolution (~1 mm), cheap and easy but noisy/distorted.
- *X-rays*: film/digital/fluoroscopy, including Digital Subtraction Angiography (subtracting a pre-contrast image from post-contrast images).
- *CT scan*: builds 3D images from many 2D X-ray slices around one rotation axis (same physics as X-ray).
- *MRI*: uses strong magnetic fields, gradients, and radio waves to image organs.
- *CT vs MRI comparison*: CT uses X-rays and is better for trauma, bone, chest/lung imaging; MRI uses magnets/radio waves, doesn't show tendons/ligaments as well as it does soft tissue, and is better for spinal cord and brain tumor imaging.

**Hyperspectral Imaging (HSI)**: analyzes a wide, continuous spectrum per pixel (rather than just RGB), enabling material/object identification via unique spectral signatures, with fine wavelength resolution across visible and near-infrared.

---

## Photogrammetry and LiDAR

- **Photogrammetry**: the science of obtaining reliable measurements from photographs (properties of surfaces/objects without physical contact). Began mid-19th century with balloon aerial photos.
- **LiDAR** (Light Detection and Ranging): measures distances using laser pulses; emerged in the 1960s for atmospheric studies.
- **Comparison**:
  - LiDAR: generates its own light (weather/lighting independent), can penetrate foliage gaps to capture fine ground detail, but is expensive and only produces point clouds.
  - Photogrammetry: dependent on ambient light/photo quality, reconstructs only visible surfaces, works with a wide range of cameras/drones, and produces richer outputs — colorized point clouds, textured meshes, orthomosaics.
  - The two are often combined for more complete 3D reconstruction.

**Photogrammetry topic list**: Introduction; development & classification; the photogrammetric process; imagery/support-data acquisition; orientation and triangulation; stereo model compilation; stereoscopic 3D viewing and measurement; DTM/DEM generation; contour map generation; orthorectification; 3D feature extraction and scene modeling; relationship with LiDAR; radargrammetry and radar interferometry; and limitations.

- **Relationship to RS/GIS**: photogrammetry supplies precise geometric measurements, feeding into GIS databases and complementing broader RS interpretation.
- **Types of remotely received information** (photogrammetric context):
  - *Geometric* — spatial position/shape (most important for photogrammetry).
  - *Physical* — EM radiation properties (radiant energy, wavelength, polarization).
  - *Semantic* — meaning derived through interpretation.
  - *Temporal* — change over time via multi-date image comparison.
- **Photogrammetric products**: photographic products (from single or overlapping photos), computational results (e.g., aerial triangulation giving 3D ground-control coordinates; DEMs), and maps (planimetric, topographic, thematic).
- **Photo input vs map output**: a photo (perspective projection, ~0.5 GB per 9-inch frame, implicit/labeled data) is transformed into a map (orthogonal projection, smaller data size, less-explicit pixel-level information).
- **Image vs map properties**:
  - *Images* (vertical or oblique photographs — high oblique shows horizon, low oblique doesn't): perspective projection, non-uniform scale.
  - *Maps*: orthogonal (parallel) projection, uniform scale.
- **Scale and relief displacement**:
  - Photo scale = focal length / flying height above ground (s = f/(H−h); average scale uses average height).
  - If focal length/height are unknown but a reference map exists: photo scale = (photo distance/map distance) × map scale.
  - *Relief displacement*: the radial shift in an object's image position caused by its elevation above a reference datum — increases with the object's height and with distance from the photo's center (nadir point); it's why identical ground distances can appear unequal on a photo.
  - An **orthophoto** corrects for this displacement/relief and scale distortion so it behaves like a true map.

---

## Overall Summary

This deck is the complete lecture set for a graduate **Remote Sensing and GIS** course, moving through five broad arcs:

1. **Foundations of Remote Sensing** — what RS is, the EM spectrum, active/passive sensing, platforms, satellite orbits, and the four types of sensor resolution.
2. **GIS Theory and Spatial Data** — what GIS is, its history (from 1830s cholera maps to 1980s commercial GIS), its components/benefits, digital mapping concepts, and the vector/raster spatial data models, including detailed vector overlay operations and raster (local, focal, zonal, resampling, aggregate) operations, plus Python scripting in QGIS.
3. **Positioning and Projections** — coordinate systems, map projections (especially UTM), datums/ellipsoids, and the full GNSS landscape (GPS, GLONASS, Galileo, BeiDou), including how trilateration determines position.
4. **Image Interpretation and Processing** — the eight visual-interpretation elements and interpretation keys, followed by the four pillars of digital image processing (preprocessing, enhancement, transformation, classification), then microwave/radar remote sensing (passive vs active, RAR vs SAR) and camera-based/hyperspectral imaging, with a medical-imaging analogy (ultrasound, X-ray, CT, MRI).
5. **Photogrammetry and LiDAR** — deriving precise geometric measurements from photographs and laser data, covering scale, relief displacement, orthophotos, and how photogrammetric products (DEMs, orthorectified maps) differ from raw imagery, plus how LiDAR and photogrammetry complement each other.

Together, these units build from *what remote sensing data is and how it's captured*, to *how spatial data is stored and analyzed in a GIS*, to *how position is measured on Earth*, to *how images are interpreted and processed*, and finally to *how precise 3D geometry is extracted from imagery and lasers* — giving a full pipeline from raw sensor data to usable geospatial information.