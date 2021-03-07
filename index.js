var osmtogeojson = require('osmtogeojson');
var fs = require('fs');
var https = require('https');

https.get('https://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3Barea%5B%22name%22%3D%22Mississauga%22%5D%2D%3E%2Emiss%3B%28node%5B%22amenity%22%3D%22bicycle%5Fparking%22%5D%28area%2Emiss%29%3Bway%5B%22amenity%22%3D%22bicycle%5Fparking%22%5D%28area%2Emiss%29%3Brelation%5B%22amenity%22%3D%22bicycle%5Fparking%22%5D%28area%2Emiss%29%3B%29%3Bout%20center%3B%3E%3Bout%20skel%20qt%3B%0A', function (res) {
    var json = '';

    res.on('data', function (chunk) {
        json += chunk;
    });

    res.on('end', function () {
        if (res.statusCode === 200) {
            fs.writeFileSync('docs/maps/data/bike_parking.geojson',JSON.stringify(osmtogeojson(JSON.parse(json))));
        } else {
            console.log('Status:', res.statusCode);
        }
    });
}).on('error', function (err) {
      console.log('Error:', err);
});


//osmtogeojson(osm_data);
