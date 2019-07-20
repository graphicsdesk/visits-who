library(tidyverse)
library(jsonlite)
library(maps)
library(mapdata)

events <- fromJSON("../data/events-20190719.json")

states <- map_data("state")
ggplot() +
  geom_polygon(data = states, aes(x = long, y = lat, group = group), fill = "gray80", color = "white") + 
  geom_point(data = events, aes(x = lng, y = lat)) +
  coord_fixed(1.3)
  
