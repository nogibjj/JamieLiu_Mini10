The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            nan |
|  1 | Albania           |              89 |               132 |              54 |                            nan |
|  2 | Algeria           |              25 |                 0 |              14 |                            nan |
|  3 | Andorra           |             245 |               138 |             312 |                            nan |
|  4 | Angola            |             217 |                57 |              45 |                            nan |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            nan |
|  6 | Argentina         |             193 |                25 |             221 |                            nan |
|  7 | Armenia           |              21 |               179 |              11 |                            nan |
|  8 | Australia         |             261 |                72 |             212 |                            nan |
|  9 | Austria           |             279 |                75 |             191 |                            nan |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            nan |
|  1 | Albania           |              89 |               132 |              54 |                            nan |
|  2 | Algeria           |              25 |                 0 |              14 |                            nan |
|  3 | Andorra           |             245 |               138 |             312 |                            nan |
|  4 | Angola            |             217 |                57 |              45 |                            nan |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            nan |
|  6 | Argentina         |             193 |                25 |             221 |                            nan |
|  7 | Armenia           |              21 |               179 |              11 |                            nan |
|  8 | Australia         |             261 |                72 |             212 |                            nan |
|  9 | Austria           |             279 |                75 |             191 |                            nan |

The operation is describe data

The truncated output is: 

|    | summary   | country     |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:----------|:------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | count     | 193         |         193     |          193      |        193      |                              0 |
|  1 | mean      |             |         106.161 |           80.9948 |         49.4508 |                                |
|  2 | stddev    |             |         101.143 |           88.2843 |         79.6976 |                                |
|  3 | min       | Afghanistan |           0     |            0      |          0      |                                |
|  4 | max       | Zimbabwe    |         376     |          438      |        370      |                                |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            nan |
|  1 | Albania           |              89 |               132 |              54 |                            nan |
|  2 | Algeria           |              25 |                 0 |              14 |                            nan |
|  3 | Andorra           |             245 |               138 |             312 |                            nan |
|  4 | Angola            |             217 |                57 |              45 |                            nan |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            nan |
|  6 | Argentina         |             193 |                25 |             221 |                            nan |
|  7 | Armenia           |              21 |               179 |              11 |                            nan |
|  8 | Australia         |             261 |                72 |             212 |                            nan |
|  9 | Austria           |             279 |                75 |             191 |                            nan |

The operation is query data

The query is SELECT country, beer_servings, total_litres_of_pure_alcohol FROM Drinks WHERE beer_servings > 100

The truncated output is: 

|    | country           |   beer_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|-------------------------------:|
|  0 | Andorra           |             245 |                            nan |
|  1 | Angola            |             217 |                            nan |
|  2 | Antigua & Barbuda |             102 |                            nan |
|  3 | Argentina         |             193 |                            nan |
|  4 | Australia         |             261 |                            nan |
|  5 | Austria           |             279 |                            nan |
|  6 | Bahamas           |             122 |                            nan |
|  7 | Barbados          |             143 |                            nan |
|  8 | Belarus           |             142 |                            nan |
|  9 | Belgium           |             295 |                            nan |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            nan |
|  1 | Albania           |              89 |               132 |              54 |                            nan |
|  2 | Algeria           |              25 |                 0 |              14 |                            nan |
|  3 | Andorra           |             245 |               138 |             312 |                            nan |
|  4 | Angola            |             217 |                57 |              45 |                            nan |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            nan |
|  6 | Argentina         |             193 |                25 |             221 |                            nan |
|  7 | Armenia           |              21 |               179 |              11 |                            nan |
|  8 | Australia         |             261 |                72 |             212 |                            nan |
|  9 | Austria           |             279 |                75 |             191 |                            nan |

The operation is transform data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol | alcohol_category   |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|:-------------------|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            nan | Low Beer           |
|  1 | Albania           |              89 |               132 |              54 |                            nan | Moderate Beer      |
|  2 | Algeria           |              25 |                 0 |              14 |                            nan | Low Beer           |
|  3 | Andorra           |             245 |               138 |             312 |                            nan | High Beer          |
|  4 | Angola            |             217 |                57 |              45 |                            nan | High Beer          |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            nan | High Beer          |
|  6 | Argentina         |             193 |                25 |             221 |                            nan | High Beer          |
|  7 | Armenia           |              21 |               179 |              11 |                            nan | Low Beer           |
|  8 | Australia         |             261 |                72 |             212 |                            nan | High Beer          |
|  9 | Austria           |             279 |                75 |             191 |                            nan | High Beer          |

