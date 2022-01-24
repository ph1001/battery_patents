# Imports
from datetime import datetime
import plotly.io as pio


#############
# Functions #
#############

def message():

    filename_this = __file__.split('/')[-1]
    print('executing a function from '+filename_this)


# From Plots_countries
def current_time_string():

    #message()

    now_ = datetime.now()
    time_string = f'{now_.year}-{now_.month if now_.month>=10 else str(0)+str(now_.month)}-{now_.day if now_.day>=10 else str(0)+str(now_.day)}_{now_.hour if now_.hour>=10 else str(0)+str(now_.hour)}{now_.minute if now_.minute>=10 else str(0)+str(now_.minute)}'

    return time_string


# From Plots_countries
def image_saver(figure, filename, eps):

    message()
    
    if eps:
        filename_string = filename + '.eps'
        pio.write_image(figure, filename_string, width = 1920/2, height = 1080/2, scale=1.0)

    else:
        filename_string = filename + '.png'
        pio.write_image(figure, filename_string, width=1500, height=900)



# From Plots_countries
#country_labels_UN_dict = {'CN':'China', 'JP':'Japan', 'US':'United States of America', 'KR':'Republic of Korea',
#                          'DE':'Germany','TW':'China, Taiwan Province of China', 'CA':'Canada', 'AU':'Australia',
#                          'FR':'France', 'GB':'United Kingdom'
#                         }


# From Plots_countries
country_labels_dict = {'CN':'China', 'JP':'Japan', 'US':'USA', 'KR':'South Korea',
                       'WO':'World Intellectual Property Organization (WIPO)', 'EP':'European Patent Office (EPO)',
                       'DE':'Germany','TW':'Taiwan', 'CA':'Canada', 'AU':'Australia', 'FR':'France','GB':'UK',
                       'RU':'Russia', 'HK': 'Hong Kong', 'KP': 'North Korea'
                      }


numbers_dict = {
    1:'one', 2: 'two', 3:'three', 4:'four', 5:'five',
    6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten'
}


########
# Data #
########

# From Plots_countries
ctry_code_name_dict = {
    # from here: from PATSTAT table TLS801_COUNTRY
    'AD': 'Andorra',
    'AE': 'United Arab Emirates',
    'AF': 'Afghanistan',
    'AG': 'Antigua and Barbados',
    'AI': 'Anguilla',
    'AL': 'Albania',
    'AM': 'Armenia',
    'AN': 'Netherlands Antilles ',
    'AO': 'Angola',
    'AP': 'African Regional Intellectual Property Organization (ARIPO)',
    'AR': 'Argentina', # Changed this manually. Was: 'Argentinia'
    'AT': 'Austria',
    'AU': 'Australia',
    'AW': 'Aruba',
    'AZ': 'Azerbaijan',
    'BA': 'Bosnia and Herzegovina',
    'BB': 'Barbados',
    'BD': 'Bangladesh',
    'BE': 'Belgium',
    'BF': 'Burkina Faso',
    'BG': 'Bulgaria',
    'BH': 'Bahrain',
    'BI': 'Burundi',
    'BJ': 'Benin',
    'BM': 'Bermuda',
    'BN': 'Brunei Daussalam',
    'BO': 'Bolivia (Plurinational State of)',
    'BQ': 'Bonaire, Saint Eustatius and Saba',
    'BR': 'Brazil',
    'BS': 'Bahamas',
    'BT': 'Bhutan',
    'BU': 'Burma',
    'BV': 'Bouvet Island',
    'BW': 'Botswana',
    'BX': 'Benelux Office for Intellectual Property (BOIP)',
    'BY': 'Belarus',
    'BZ': 'Belize',
    'CA': 'Canada',
    'CD': 'Democratic Republic of the Congo',
    'CF': 'Central African Republic',
    'CG': 'Congo',
    'CH': 'Switzerland',
    'CI': "Côte d'Ivoire",
    'CK': 'Cook Islands',
    'CL': 'Chile',
    'CM': 'Cameroon',
    'CN': 'China',
    'CO': 'Colombia',
    'CR': 'Costa Rica',
    'CS': 'Czechoslovakia',
    'CU': 'Cuba',
    'CV': 'Cabo Verde',
    'CW': 'Curaçao',
    'CY': 'Cyprus',
    'CZ': 'Czechia',
    'DD': 'German Democratic Republic',
    'DE': 'Germany',
    'DJ': 'Djibouti',
    'DK': 'Denmark',
    'DL': 'German Democratic Republic',
    'DM': 'Dominica',
    'DO': 'Dominican Republic',
    'DZ': 'Algeria',
    'EA': 'Eurasian Patent Organization (EAPO)',
    'EC': 'Ecuador',
    'EE': 'Estonia',
    'EG': 'Egypt',
    'EH': 'Western Sahara',
    'EM': 'European Union Intellectual Property Office (EUIPO)',
    'EP': 'European Patent Office (EPO)',
    'ER': 'Eritrea',
    'ES': 'Spain',
    'ET': 'Ethiopia',
    'EU': 'European Union',
    'FI': 'Finland',
    'FJ': 'Fiji',
    'FK': 'Falkland Islands (Malvinas)',
    'FO': 'Faroe Islands',
    'FR': 'France',
    'GA': 'Gabon',
    'GB': 'United Kingdom',
    'GC': 'Patent Office of the Cooperation Council for the Arab States of the Gulf (GCC Patent Office)',
    'GD': 'Grenada',
    'GE': 'Georgia',
    'GG': 'Guernsey',
    'GH': 'Ghana',
    'GI': 'Gibraltar',
    'GL': 'Greenland',
    'GM': 'Gambia',
    'GN': 'Guinea',
    'GQ': 'Equatorial Guinea',
    'GR': 'Greece',
    'GS': 'South Georgia and the South Sandwich Islands',
    'GT': 'Guatemala',
    'GW': 'Guinea-Bissau',
    'GY': 'Guyana',
    'HK': 'Hong Kong SAR (China)',
    'HN': 'Honduras',
    'HR': 'Croatia',
    'HT': 'Haiti',
    'HU': 'Hungary',
    'IB': 'International Bureau of the World Intellectual Property Organization (WIPO)',
    'ID': 'Indonesia',
    'IE': 'Ireland',
    'IL': 'Israel',
    'IM': 'Isle of Man',
    'IN': 'India',
    'IQ': 'Iraq',
    'IR': 'Iran (Islamic Republic of)',
    'IS': 'Iceland',
    'IT': 'Italy',
    'JE': 'Jersey',
    'JM': 'Jamaica',
    'JO': 'Jordan',
    'JP': 'Japan',
    'KE': 'Kenya',
    'KG': 'Kyrgyzstan',
    'KH': 'Cambodia',
    'KI': 'Kiribati',
    'KM': 'Comoros',
    'KN': 'Saint Kitts and Nevis',
    'KP': "Democratic People's Republic of Korea",
    'KR': 'Republic of Korea',
    'KW': 'Kuwait',
    'KY': 'Cayman Islands',
    'KZ': 'Kazakhstan',
    'LA': "Lao People's Democratic Republic",
    'LB': 'Lebanon',
    'LC': 'Saint Lucia',
    'LI': 'Liechtenstein',
    'LK': 'Sri Lanka',
    'LR': 'Liberia',
    'LS': 'Lesotho',
    'LT': 'Lithuania',
    'LU': 'Luxembourg',
    'LV': 'Latvia',
    'LY': 'Libya',
    'MA': 'Morocco',
    'MC': 'Monaco',
    'MD': 'Republic of Moldova',
    'ME': 'Montenegro',
    'MG': 'Madagascar',
    'MK': 'North Macedonia',
    'ML': 'Mali',
    'MM': 'Myanmar',
    'MN': 'Mongolia',
    'MO': 'Macao SAR (China)',
    'MP': 'Northern Mariana Islands',
    'MR': 'Mauritania',
    'MS': 'Montserrat',
    'MT': 'Malta',
    'MU': 'Mauritius',
    'MV': 'Maledives',
    'MW': 'Malawi',
    'MX': 'Mexico',
    'MY': 'Malaysia',
    'MZ': 'Mozambique',
    'NA': 'Namibia',
    'NE': 'Niger',
    'NG': 'Nigeria',
    'NI': 'Nicaragua',
    'NL': 'Netherlands',
    'NO': 'Norway',
    'NP': 'Nepal',
    'NR': 'Nauru',
    'NZ': 'New Zealand',
    'OA': 'African Intellectual Property Organisation (OAPI)',
    'OM': 'Oman',
    'PA': 'Panama',
    'PE': 'Peru',
    'PG': 'Papua New Guinea',
    'PH': 'Philippines',
    'PK': 'Pakistan',
    'PL': 'Poland',
    'PT': 'Portugal',
    'PW': 'Palau',
    'PY': 'Paraguay',
    'QA': 'Qatar',
    'QZ': 'Community Plant Variety Office (EU) (CPVO)',
    'RO': 'Romania',
    'RS': 'Serbia',
    'RU': 'Russian Federation',
    'RW': 'Rwanda',
    'SA': 'Saudi Arabia', # Changed this manually. Was: 'Saudia Arabia'
    'SB': 'Solomon Islands',
    'SC': 'Seychelles',
    'SD': 'Sudan',
    'SE': 'Sweden',
    'SG': 'Singapore',
    'SH': 'Saint Helena, Ascension and Tristan da Cunha',
    'SI': 'Slovenia',
    'SK': 'Slovakia',
    'SL': 'Sierra Leone',
    'SM': 'San Marino',
    'SN': 'Senegal',
    'SO': 'Somalia',
    'SR': 'Suriname',
    'SS': 'South Sudan',
    'ST': 'Sao Tome and Principe',
    'SU': 'Soviet Union',
    'SV': 'El Salvador',
    'SX': 'Sint Maarten (Dutch part)',
    'SY': 'Syrian Arab Republic',
    'SZ': 'Eswatini',
    'TC': 'Turks and Caicos Islands',
    'TD': 'Chad',
    'TG': 'Togo',
    'TH': 'Thailand',
    'TJ': 'Tajikistan',
    'TL': 'Timor-Leste',
    'TM': 'Turkmenistan',
    'TN': 'Tunisia',
    'TO': 'Tonga',
    'TR': 'Turkey',
    'TT': 'Trinidad and Tobago',
    'TV': 'Tuvalu',
    'TW': 'Chinese Taipei',
    'TZ': 'United Republic of Tanzania',
    'UA': 'Ukraine',
    'UG': 'Uganda',
    'US': 'United States of America',
    'UY': 'Uruguay',
    'UZ': 'Uzbekistan',
    'VA': 'Holy See',
    'VC': 'Saint Vincent and the Grenadines',
    'VE': 'Venezuela (Bolivarian Republic of)',
    'VG': 'British Virgin Islands',
    'VN': 'Viet Nam',
    'VU': 'Vanuatu',
    'WO': 'World Intellectual Property Organisation (WIPO)',
    'WS': 'Samoa',
    'XN': 'Nordic Patent Institute (NPI)',
    'XU': 'International Union for the Protection of New Varieties of Plants (UPOV)',
    'XV': 'Visegrad Patent Institute (VPI)',
    'XX': 'unknown',
    'YD': 'Democratic Yemen',
    'YE': 'Yemen',
    'YU': 'Yugoslavia/Serbia and Montenegro',
    'ZA': 'South Africa',
    'ZM': 'Zambia',
    'ZW': 'Zimbabwe',
    # from here: manual additions 
    'other': 'other',
    'NC': 'New Caledonia',
    'PR': 'Puerto Rico',
    'RE': 'Réunion',
    'GF': 'French Guiana',
    'GP': 'Guadeloupe',
    'MH': 'Marshall Islands'
}
