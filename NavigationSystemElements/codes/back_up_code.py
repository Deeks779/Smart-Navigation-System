#1
import folium
import pandas as pd
from folium import plugins
import json
loc=(23.077386057472637,76.85258607068243)
m=folium.Map(location=loc, width="75%", zoom_start= 17)
folium.TileLayer('stamentoner').add_to(m)
#display(m)

#2
def add_col(file_name,col_name):
    with open(file_name) as f:
        t = json.load(f)
    folium.Choropleth(geo_data=t,fill_color=col_name,line_color='black').add_to(m)

#3
ab_map='C:/Users/Deeksha/Desktop/Project ex1/map.geojson'
add_col(ab_map,'#FF0000')
mph_map='C:/Users/Deeksha/Desktop/Project ex1/multi_purpose_hall.geojson'
add_col(mph_map,'#FF0000')
lc_map='C:/Users/Deeksha/Desktop/Project ex1/lab_complex.geojson'
add_col(lc_map,'#FF0000')
al_map='C:/Users/Deeksha/Desktop/Project ex1/aerospace_lab.geojson'
add_col(al_map,'#FF0000')
gh1_map='C:/Users/Deeksha/Desktop/Project ex1/girls_hostel_block1.geojson'
add_col(gh1_map,'#C154C1')
gh2_map='C:/Users/Deeksha/Desktop/Project ex1/girls_hostel_block2.geojson'
add_col(gh2_map,'#C154C1')
bh1_map='C:/Users/Deeksha/Desktop/Project ex1/boy_1.geojson'
add_col(bh1_map,'#0000FF')
bh2_map='C:/Users/Deeksha/Desktop/Project ex1/boy_2.geojson'
add_col(bh2_map,'#0000FF')
bh3_map='C:/Users/Deeksha/Desktop/Project ex1/boy_3.geojson'
add_col(bh3_map,'#0000FF')
bh4_map='C:/Users/Deeksha/Desktop/Project ex1/boy_4.geojson'
add_col(bh4_map,'#0000FF')
bh5_map='C:/Users/Deeksha/Desktop/Project ex1/boy_5.geojson'
add_col(bh5_map,'#0000FF')
bh6_map='C:/Users/Deeksha/Desktop/Project ex1/boy_6.geojson'
add_col(bh6_map,'#0000FF')
mayuri_map='C:/Users/Deeksha/Desktop/Project ex1/mayuri.geojson'
add_col(mayuri_map,'#FFA500')
ub_map='C:/Users/Deeksha/Desktop/Project ex1/underbelly.geojson'
add_col(ub_map,'#FFA500')
vb_map='C:/Users/Deeksha/Desktop/Project ex1/vollyball.geojson'
add_col(vb_map,'#008000')
cr_map='C:/Users/Deeksha/Desktop/Project ex1/cricket_ground.geojson'
add_col(cr_map,'#008000')
fb_map='C:/Users/Deeksha/Desktop/Project ex1/football_ground.geojson'
add_col(fb_map,'#008000')
fb_map='C:/Users/Deeksha/Desktop/Project ex1/pond.geojson'
add_col(fb_map,'#008000')
ue_map='C:/Users/Deeksha/Desktop/Project ex1/university_entrance.geojson'
add_col(ue_map,'#FF0000')

with open('C:/Users/Deeksha/Desktop/Project ex1/enterance_path.geojson') as f:
   t = json.load(f)
    
folium.Choropleth(geo_data=t,fill_color='black',line_color='black').add_to(m)
display(m)
