# ISCF Project
## MVP
- Website
- Time viz of energy usage
    - x axis is time
    - y axis is energy usage
    - can switch between:
        - category (type of consumer)
        - transformer (specific consumer transformer)
        - each of these is a line on the graph
- Geographical viz of energy usage
    - Background is location
    - point is transformer
    - a bit of cloud around it
    - color of cloud is how much energy they used
## Data Description
### dfc_day.csv
#### Columns
- idx
- date
- category
    - MSI, Residential, Water Works
    - What type of user
- conload
    - maximum energy they can use
- imp
    - how much energy was used by that consumer on that date
### dfm_day.csv
- idx
- date
- MTR_NUMBER
    - meter number of a specific consumer
- conload
- imp
    - same as above
### geo_dtr_1day_cons.csv
- latitude
- longitude
    - location of transformer
- active_energy
    - energy used by consumer
- active_energy_exp
    - energy generated by consumer (solar, etc)
- other columns as well
## Example/Inspirations
- https://streamlit-example-app-download-app-lk16x1.streamlitapp.com/
- https://github.com/streamlit/example-app-commenting