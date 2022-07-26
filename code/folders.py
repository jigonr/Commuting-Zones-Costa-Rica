import os

# Folder structure

CODEDIR = "codes"
DATADIR = "data"
RAW_DATA = os.path.join(DATADIR, "00-raw_data")
INTERMEDIATE_DATA = os.path.join(DATADIR, "01-intermediate_data")
FINAL_DATA = os.path.join(DATADIR, "02-final_data")
OUTDIR = "output"
FIGURES_OUTPUT = os.path.join(OUTDIR, "01-figures")
FIGURES_MAIN_TEXT_OUTPUT = os.path.join(FIGURES_OUTPUT, "01-main_text")
FIGURES_APPENDIX_OUTPUT = os.path.join(FIGURES_OUTPUT, "02-appendix")
TABLES_OUTPUT = os.path.join(OUTDIR, "02-tables")
TABLES_MAIN_TEXT_OUTPUT = os.path.join(TABLES_OUTPUT, "01-main_text")
TABLES_APPENDIX_OUTPUT = os.path.join(TABLES_OUTPUT, "02-appendix")

# Input files

## Raw Data

### Census 2011
census2011_file = os.path.join(RAW_DATA, r"CR_CENSO2011_Muestra10%_NBI.sav")

### Costa Rican map
costa_rica_shapefile = os.path.join(RAW_DATA, "cri_admbnda_adm2_2021_WGS_84.shp")

### Region concordance table
region_concordance_file = os.path.join(RAW_DATA, "region_concordance.xlsx")

### Costa Rican Roads Network Dataset
costa_rican_roads_file = os.path.join(RAW_DATA, "costa-rica-latest.osm")

### ENAHO 2020
enaho2020_file = os.path.join(RAW_DATA, "ENAHO 2020.sav")

### ENAHO 2021
enaho2021_file = os.path.join(RAW_DATA, "ENAHO 2021.sav")

## Intermediate Data

### Costa Rican Commuting Zones
costa_rican_commuting_zones_file = os.path.join(INTERMEDIATE_DATA, "czcr.xlsx")

### Employment Census 2011
employment2011_file = os.path.join(INTERMEDIATE_DATA, "employment2011.xlsx")

## Final Data

### Costa Rican Route Distance and Travel Time
costa_rican_municipalities_distance_matrix = os.path.join(FINAL_DATA, "distances.xlsx")

