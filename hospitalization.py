import pandas as pd

# helper function to get hospitalization data

ADMIN_NHS_MAPPING = {
 'England': 'England',
 'South East': 'South East',
 'Scotland': 'Scotland',
 'Wales': 'Wales',
 'London': 'London',
 'South West': 'South West',
 'East of England': 'East of England',
 'North West': 'North West',
 'Yorkshire and The Humber': 'North East and Yorkshire',
 'West Midlands': 'Midlands',
 'East Midlands': 'Midlands',
 'North East': 'North East and Yorkshire',
 'Northern Ireland': 'Northern Ireland'
}

def get_hospitalization_data():

    admin_mapping_df = pd.DataFrame.from_dict(ADMIN_NHS_MAPPING, orient='index').reset_index().rename(
        columns={'index': 'region', 0: 'NHSRegion'}
    )

    download_success = False
    try:
        df_hospital = pd.read_csv(
            'https://api.coronavirus.data.gov.uk/v2/data?areaType=nhsRegion&metric=hospitalCases&format=csv'
        )
        download_success = True
    except urllib.error.URLError as exception:
        print(exception)

    if download_success:
        nhs_bed_occupancy = df_hospital[
                (df_hospital.date >= '2020-07-01') & (~df_hospital.hospitalCases.isnull())
            ].rename(
            columns={'areaName': 'NHSRegion', 'hospitalCases': 'hospital_cases'}
        )[['NHSRegion', 'date', 'hospital_cases']]
    else:
        nhs_bed_occupancy = pd.DataFrame(
            {'NHSRegion': NHS_REGIONS, 'hospital_cases': 'missing'}
        )
    admin_mapping_df = pd.DataFrame.from_dict(ADMIN_NHS_MAPPING, orient='index').reset_index().rename(
        columns={'index': 'region', 0: 'NHSRegion'}
    )
    return admin_mapping_df.merge(
        nhs_bed_occupancy,
        on='NHSRegion',
        how='left'
    ).drop(columns='NHSRegion')
