##web_map_app/
#|-app.py
#|-templates/
#|  L_ map.html
#L static/
#  L style.css

from flask import Flask, render_template
import folium

app = Flask(__name__)  # Corrected line

@app.route('/')
def index():
    # Create a map centered at Phoenix, Arizona latitude and longitude
    m = folium.Map(location=[33.4484, -112.0740], zoom_start=13)

    # Save the map to an HTML file
    m.save('templates/map.html')

    # Render the map in the browser
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)
