<?php
	// $domain = 'http://a.tile.osm.org'; $suffix = '';
	// $domain = 'http://a.basemaps.cartocdn.com/light_all'; $suffix = '@2x';
	$domain = 'http://server.arcgisonline.com/ArcGIS/rest/services/World_Physical_Map/MapServer/tile'; $suffix = '';

	$maxz = 6;

	for ($z = 0; $z < $maxz; $z++) {
		echo "Z: ".$z."\n";
		for ($x = 0; $x < pow(2, $z); $x++) {
			for ($y = 0; $y < pow(2, $z); $y++) {
				// http://a.tile.osm.org/0/0/0.png
				// Auswahl https://leaflet-extras.github.io/leaflet-providers/preview/
				$url = $domain. '/'. $z. '/'. $x. '/'. $y. $suffix. '.png'; // OSM und CartoDB
				$url = $domain. '/'. $z. '/'. $y. '/'. $x. $suffix. '.png'; // Physical ESRI

				file_put_contents('tile'. $z. '-'. $x. '-'. $y. '.png' , fopen($url, 'r'));
			}
		}
	}
?>
