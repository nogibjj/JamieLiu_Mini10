The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is describe data

The truncated output is: 

|    | summary   | country     |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:----------|:------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | count     | 193         |         193     |          193      |        193      |                       193      |
|  1 | mean      |             |         106.161 |           80.9948 |         49.4508 |                         4.7171 |
|  2 | stddev    |             |         101.143 |           88.2843 |         79.6976 |                         3.7733 |
|  3 | min       | Afghanistan |           0     |            0      |          0      |                         0      |
|  4 | max       | Zimbabwe    |         376     |          438      |        370      |                        14.4    |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is query data

The query is SELECT country, beer_servings, total_litres_of_pure_alcohol FROM Drinks WHERE beer_servings > 100

The truncated output is: 

|    | country           |   beer_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|-------------------------------:|
|  0 | Andorra           |             245 |                           12.4 |
|  1 | Angola            |             217 |                            5.9 |
|  2 | Antigua & Barbuda |             102 |                            4.9 |
|  3 | Argentina         |             193 |                            8.3 |
|  4 | Australia         |             261 |                           10.4 |
|  5 | Austria           |             279 |                            9.7 |
|  6 | Bahamas           |             122 |                            6.3 |
|  7 | Barbados          |             143 |                            6.3 |
|  8 | Belarus           |             142 |                           14.4 |
|  9 | Belgium           |             295 |                           10.5 |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is transform data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol | alcohol_category   |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|:-------------------|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   | Low Beer           |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 | Moderate Beer      |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 | Low Beer           |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 | High Beer          |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 | High Beer          |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 | High Beer          |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 | High Beer          |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 | Low Beer           |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 | High Beer          |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 | High Beer          |

