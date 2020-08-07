# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:02:44 2020

@author: PC-Home
"""
# Create a list of the BRICS countries
country = [ 
            "Brazil", 
            "Russia", 
            "India", 
            "China", 
            "South Africa"
          ]

capitals = {
    "Brazil": "Brasilia",
    "Russia": "Moscow",
    "India": "New Delhi",
    "China": "Beijing",
    "South Africa": [
                        "Pretoria",
                        "Cape Town",
                        "Bloemfontein"
                    ]
           }

# Print the list and dictionary
print( country)
print( capitals)
print( capitals["South Africa"][1] )

