import scrapy
import json


class ShellspiderSpider(scrapy.Spider):
    name = "shellSpider"
    allowed_domains = ["shellretaillocator.geoapp.me"]

    nc_cities_coordinates = [
    (35.759573, -79.019300),  # Raleigh
    (36.0726, -79.7910),      # Greensboro
    (35.2271, -80.8431),      # Charlotte
    (35.2272, -78.6872),      # Durham
    (35.6213, -80.9311),      # Concord
    (35.6123, -80.8617),      # Gastonia
    (36.0035, -79.8191),      # Chapel Hill
    (35.8168, -78.7811),      # Cary
    (35.7040, -77.0469),      # Greenville
    (35.2778, -80.7347),      # Huntersville
    (35.3985, -77.9962),      # Wilson
    (35.5350, -78.9497),      # Goldsboro
    (35.9000, -80.0000),      # Statesville
    (34.2257, -77.9447),      # Wilmington
    (35.2158, -80.1732),      # Mooresville
    (35.9654, -78.9173),      # Apex
    (35.6510, -81.1890),      # Hickory
    (35.1700, -80.8400),      # Monroe
    (35.0527, -78.8784),      # Fayetteville
    (35.4799, -79.1803),      # Sanford
    (35.1085, -77.0441),      # New Bern
    (35.9382, -77.7907),      # Rocky Mount
    (35.6213, -77.5110),      # Tarboro
    (36.0765, -80.2351),      # Winston-Salem
    (35.9236, -79.0558),      # High Point
    (36.0999, -80.2710),      # Kernersville
    (35.2920, -81.5356),      # Shelby
    (35.2321, -82.7350),      # Brevard
    (36.2134, -81.6746),      # Boone
    (35.5951, -82.5515),      # Asheville
    (35.9382, -77.7907),      # Knightdale
    (34.7541, -77.4306),      # Jacksonville
    (35.5993, -81.6970),      # Morganton
    (36.0810, -79.1019),      # Mebane
    (35.9073, -79.0562),      # Elon
    (34.2549, -77.8824),      # Bolivia
    (34.5044, -78.2463),      # Bolton
    (35.4261, -83.4463),      # Bryson City
    (35.2676, -81.1062),      # Lincolnton
    (35.3459, -81.5356),      # Cherryville
    (36.1869, -80.1333),      # Elkin
    (36.2674, -79.7611),      # Reidsville
    (35.5651, -80.8733),      # Kannapolis
    (36.1818, -80.4096),      # Thomasville
    (36.3120, -80.2679),      # Jamestown
    (36.3920, -79.9822),      # Stokesdale
    (35.4112, -78.9941),      # Angier
    (35.6622, -79.1601),      # Asheboro
    (36.0957, -79.4378),      # Burlington
    (35.6957, -80.4649),      # Salisbury
    (35.6881, -78.8357),      # Holly Springs
    (35.5843, -78.7994),      # Fuquay-Varina
    (35.0768, -80.6697),      # Indian Trail
    (35.7157, -78.6291),      # Garner
    (35.4848, -80.8564),      # Cornelius
    (35.6509, -78.4561),      # Clayton
    (35.1168, -80.7229),      # Matthews
    (34.2387, -77.8226),      # Leland
    (35.1796, -80.6550),      # Mint Hill
    (34.9876, -80.5979),      # Waxhaw
    (36.0296, -80.3843),      # Clemmons
    (35.9101, -79.0753),      # Carrboro
    (35.3226, -80.6501),      # Harrisburg
    (35.0768, -80.6697),      # Indian Trail
    (35.7157, -78.6291),      # Garner
    (35.4848, -80.8564),      # Cornelius
]


    def start_requests(self):
        # Generate API URLs for each coordinate
        for lat, lng in self.nc_cities_coordinates:
            url = (
                f"https://shellretaillocator.geoapp.me/api/v2/locations/nearest_to"
                f"?lat={lat}&lng={lng}&limit="
            )
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Parse the JSON response
        data = json.loads(response.text)

        # Extract the required fields from each location
        for location in data.get('locations', []):
            yield {
                'id': location.get('id'),
                'name': location.get('name'),
                'lat': location.get('lat'),
                'lng': location.get('lng'),
                'brand': location.get('brand'),
                'inactive': location.get('inactive'),
                'address': location.get('address'),
                'city': location.get('city'),
                'state': location.get('state'),
                'postcode': location.get('postcode'),
                'telephone': location.get('telephone'),
                'country': location.get('country'),
                'amenities': location.get('amenities'),
                'website_url': location.get('website_url'),
                'formatted_address': location.get('formatted_address'),
                'mdm_site_category': location.get('mdm_site_category'),
                'open_status': location.get('open_status'),
                'fuels': location.get('fuels'),
            }
