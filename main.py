import simplekml

locations = [
    ("St. Petersburg, Florida", 27.7676, -82.6403),
    ("Congaree National Park", 33.781170, -80.779808),
    ("Great Smoky Mountains National Park", 35.6554, -83.4348),
    ("Mammoth Cave National Park", 37.186998, -86.099977),
    ("New River Gorge National Park", 37.9275, -81.0203),
    ("Shenandoah National Park", 38.5216, -78.4367),
    ("Acadia National Park", 44.3386, -68.2733),
    ("Cuyahoga Valley National Park", 41.2609, -81.5714),
    ("Indiana Dunes National Park", 41.6533, -87.0524),
    ("Voyageurs National Park", 48.4838, -92.8383),
    ("Theodore Roosevelt National Park", 46.9782, -103.5387),
    ("Badlands National Park", 43.8554, -102.3397),
    ("Wind Cave National Park", 43.6046, -103.4213),
    ("Rocky Mountain National Park", 40.3428, -105.6836),
    ("Great Sand Dunes National Park", 37.7916, -105.5942),
    ("Black Canyon of the Gunnison National Park", 38.5754, -107.7416),
    ("Mesa Verde National Park", 37.2309, -108.4618),
    ("Canyonlands National Park", 38.3269, -109.8783),
    ("Arches National Park", 38.7331, -109.5925),
    ("Capitol Reef National Park", 38.3670, -111.2615),
    ("Bryce Canyon National Park", 37.5930, -112.1871),
    ("Zion National Park", 37.2982, -113.0263),
    ("Great Basin National Park", 39.0046, -114.2182),
    ("Grand Teton National Park", 43.7904, -110.6818),
    ("Yellowstone National Park", 44.4279, -110.5885),
    ("Glacier National Park", 48.7596, -113.7870),
    ("North Cascades National Park", 48.7718, -121.2985),
    ("Mount Rainier National Park", 46.879966, -121.726911),
    ("Olympic National Park", 47.8021, -123.6044),
    ("Crater Lake National Park", 42.8684, -122.1685),
    ("Redwood National Park", 41.2132, -124.0046),
    ("Lassen Volcanic National Park", 40.4977, -121.4207),
    ("Yosemite National Park", 37.8651, -119.5383),
    ("Kings Canyon National Park", 36.8879, -118.5551),
    ("Sequoia National Park", 36.4864, -118.5658),
    ("Death Valley National Park", 36.5054, -117.0794),
    ("Joshua Tree National Park", 33.8734, -115.9010),
    ("Grand Canyon National Park", 36.1068, -112.1128),
    ("Petrified Forest National Park", 34.9099, -109.8068),
    ("Saguaro National Park", 32.2967, -111.1666),
    ("White Sands National Park", 32.7794, -106.1722),
    ("Carlsbad Caverns National Park", 32.1742, -104.4459),
    ("Guadalupe Mountains National Park", 31.8912, -104.8606),
]

kml = simplekml.Kml()

linestring = kml.newlinestring(name="Road Trip")
linestring.coords = [(lon, lat) for name, lat, lon in locations]

kml.save("road_trip.kml")
