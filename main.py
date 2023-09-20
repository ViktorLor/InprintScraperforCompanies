list = ['Knapp AG', 'Kuhn Holding GmbH', 'Kwizda Holding GmbH', 'Leder & Schuh AG Humanic', 'Leier Holding GmbH',
        'Leyrer + Graf Baugesellschaft m.b.H.', 'LKW Walter Internationale Transportorganisation AG',
        'Loacker Recycling GmbH', 'Magna Steyr Fahrzeugtechnik AG & CO KG', 'Mahle Filtersysteme Austria GmbH',
        'Manner AG', 'Marcher Fleischwerke Österreich', 'Markant Österreich GmbH', 'Mayer & Co Beschläge GmbH (MACO)',
        'Mayr-Melnhof Holz', 'Mayr-Melnhof Karton AG', 'med-el elektromedizinische Geräte GmbH',
        'Media - Saturn Beteiligungs GmbH', 'Metro Cash & Carry Österreich GmbH', 'Miba AG', 'Mondi Group',
        'Montanwerke Brixlegg AG','Mpreis WarenvertriebsGmbH', 'MTH Retail Group', 'Neuman Fried v. GmbH', 'NÖM AG',
        'Novomatic AG', 'Ottakringer Brauerei AG', 'PALFINGER AG', 'Palmers Textil AG', 'Pappas Holding GmbH', 'PERI',
        'Pfeifer Holding GmbH', 'PKE Electronics AG', 'Plansee', 'Polytec Holding AG', 'PÖTTINGER Landtechnik GmbH',
        'Rauch Fruchtsäfte GmbH & Co OG', 'RHI Magnesita', 'Rhomberg Bau Gruppe',
        'Rosenberger Hochfrequenztechnik GmbH & Co. KG', 'S&T AG', 'Sandoz GmbH', 'Sappi',
        'Schachermayer GmbH', 'Schiebel Elektronische Geräte GmbH', 'Schmid Industrieholding GmbH', 'Schwarzmüller Wilhelm GmbH',
        'SEMPERIT AG', 'Sibur International GmbH', 'SIG Combibloc GmbH & CO KG', 'SIGNA Group of Companies',
        'Silhouette International Schmied AG', 'SKB Industrieholding', 'SKF Österreich AG',
        'Stahl- und Walzwerk Marienhütte GmbH', 'Stora Enso Wood Products GmbH', 'Swarovski KG', 'TCG Unitech GmbH',
        'Thöni Industriebetriebe', 'Trenkwalder Group AG', 'Trodat Trotec Holding GmbH',
        'Trumpf Maschinen Austria GmbH & CO KG', 'TTS', 'UBM Development', 'Unger Stahlbau GmbH',
        'Unser Lagerhaus Warenhandels GmbH', 'Unterberger Beteiligungs GmbH', 'VA Intertrading AG', 'Viega',
        'Viking GmbH (Stihl Tirol)', 'VIVATIS Holding AG', 'VOGL + CO', 'Wacker Neuson Linz GmbH', 'Welser Profile',
        'Weyland GmbH', 'Wienerberger AG', 'Wiesbauer', 'Windhager Zentralheizung GmbH', 'Wolf Holding GmbH',
        'Wolfgang Denzel Auto AG', 'Wolford AG', 'Wopfinger Baustoffindustrie GmbH',
        'Zentrasport Österreich eGen. (Sport2000 & Gigasport)', 'ZKW', 'Zumtobel Group']

# replace & with %26
list = [x.replace('&', '%26') for x in list]

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create folder for files
import os
if not os.path.exists('companies_raw_files'):
	os.makedirs('companies_raw_files')
	# create txt files for each company
	for company_name in list:
		file = open('companies_raw_files/' + company_name + '.txt', 'w')
		file.close()

# Create a Firefox WebDriver instance using webdriver_manager
driver = webdriver.Firefox(executable_path=r'C:\Users\Vik\Documents\4. Private\01. University\PycharmProjects\data_scraper\geckodriver.exe')

# Read the list of company names from a file (one per line)


# Loop through each company name and search on Google
for i,company_name in enumerate(list):
    
    #open a new firefox tab
    driver.execute_script("window.open('');")
    #switch to the new tab
    driver.switch_to.window(driver.window_handles[i])
    # Visit the Google homepage
    driver.get('https://www.google.com/search?q=' + company_name + ' impressum imprint')
