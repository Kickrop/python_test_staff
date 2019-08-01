# -*- coding: utf-8 -*-

import time
import random
from selenium import webdriver

country = "USA"

dicts_from_file = []
with open('wc_list.txt','r') as inf:
    for line in inf:
        dicts_from_file.append(eval('line'))

#wc = {'Acoustics',	'Acoustics',	'Agricultural Economics & Policy',	'Agricultural Engineering',	'Agriculture, Dairy & Animal Science',	'Agriculture, Multidisciplinary',	'Agronomy',	'Allergy',	'Anatomy & Morphology',	'Andrology',	'Anesthesiology',	'Anthropology',	'Archaeology',	'Architecture',	'Area Studies',	'Art',	'Asian Studies',	'Astronomy & Astrophysics',	'Audiology & Speech-Language Pathology',	'Automation & Control Systems',	'Behavioral Sciences',	'Biochemical Research Methods',	'Biochemistry & Molecular Biology',	'Biodiversity Conservation',	'Biology',	'Biophysics',	'Biotechnology & Applied Microbiology',	'Business',	'Business, Finance',	'Cardiac & Cardiovascular Systems',	'Cell & Tissue Engineering',	'Cell Biology',	'Chemistry, Analytical',	'Chemistry, Applied',	'Chemistry, Inorganic & Nuclear',	'Chemistry, Medicinal',	'Chemistry, Multidisciplinary',	'Chemistry, Organic',	'Chemistry, Physical',	'Classics',	'Clinical Neurology',	'Communication',	'Computer Science, Artificial Intelligence',	'Computer Science, Cybernetics',	'Computer Science, Hardware & Architecture',	'Computer Science, Information Systems',	'Computer Science, Interdisciplinary Applications',	'Computer Science, Software Engineering',	'Computer Science, Theory & Methods',	'Construction & Building Technology',	'Criminology & Penology',	'Critical Care Medicine',	'Crystallography',	'Cultural Studies',	'Dance',	'Demography',	'Dentistry, Oral Surgery & Medicine',	'Dermatology',	'Developmental Biology',	'Ecology',	'Economics',	'Education & Educational Research',	'Education, Scientific Disciplines',	'Education, Special',	'Electrochemistry',	'Emergency Medicine',	'Endocrinology & Metabolism',	'Energy & Fuels',	'Engineering, Aerospace',	'Engineering, Biomedical',	'Engineering, Chemical',	'Engineering, Civil',	'Engineering, Electrical & Electronic',	'Engineering, Environmental',	'Engineering, Geological',	'Engineering, Industrial',	'Engineering, Manufacturing',	'Engineering, Marine',	'Engineering, Mechanical',	'Engineering, Multidisciplinary',	'Engineering, Ocean',	'Engineering, Petroleum',	'Entomology',	'Environmental Sciences',	'Environmental Studies',	'Ergonomics',	'Ethics',	'Ethnic Studies',	'Evolutionary Biology',	'Family Studies',	'Film, Radio, Television',	'Fisheries',	'Folklore',	'Food Science & Technology',	'Forestry',	'Gastroenterology & Hepatology',	'Genetics & Heredity',	'Geochemistry & Geophysics',	'Geography',	'Geography, Physical',	'Geology',	'Geosciences, Multidisciplinary',	'Geriatrics & Gerontology',	'Gerontology',	'Health Care Sciences & Services',	'Health Policy & Services',	'Hematology',	'History',	'History & Philosophy of Science',	'History of Social Sciences',	'Horticulture',	'Hospitality, Leisure, Sport & Tourism',	'Humanities, Multidisciplinary',	'Imaging Science & Photographic Technology',	'Immunology',	'Industrial Relations & Labor',	'Infectious Diseases',	'Information Science & Library Science',	'Instruments & Instrumentation',	'Integrative & Complementary Medicine',	'International Relations',	'Language & Linguistics',	'Law',	'Limnology',	'Linguistics',	'Literary Reviews',	'Literary Theory & Criticism',	'Literature',	'Literature, African, Australian, Canadian',	'Literature, American',	'Literature, British Isles',	'Literature, German, Dutch, Scandinavian',	'Literature, Romance',	'Literature, Slavic',	'Logic',	'Management',	'Marine & Freshwater Biology',	'Materials Science, Biomaterials',	'Materials Science, Ceramics',	'Materials Science, Characterization & Testing',	'Materials Science, Coatings & Films',	'Materials Science, Composites',	'Materials Science, Multidisciplinary',	'Materials Science, Paper & Wood',	'Materials Science, Textiles',	'Mathematical & Computational Biology',	'Mathematics',	'Mathematics, Applied',	'Mathematics, Interdisciplinary Applications',	'Mechanics',	'Medical Ethics',	'Medical Informatics',	'Medical Laboratory Technology',	'Medicine, General & Internal',	'Medicine, Legal',	'Medicine, Research & Experimental',	'Medieval & Renaissance Studies',	'Metallurgy & Metallurgical Engineering',	'Meteorology & Atmospheric Sciences',	'Microbiology',	'Microscopy',	'Mineralogy',	'Mining & Mineral Processing',	'Multidisciplinary Sciences',	'Music',	'Mycology',	'Nanoscience & Nanotechnology',	'Neuroimaging',	'Neurosciences',	'Nuclear Science & Technology',	'Nursing',	'Nutrition & Dietetics',	'Obstetrics & Gynecology',	'Oceanography',	'Oncology',	'Operations Research & Management Science',	'Ophthalmology',	'Optics',	'Ornithology',	'Orthopedics',	'Otorhinolaryngology',	'Paleontology',	'Parasitology',	'Pathology',	'Pediatrics',	'Peripheral Vascular Disease',	'Pharmacology & Pharmacy',	'Philosophy',	'Physics, Applied',	'Physics, Atomic, Molecular & Chemical',	'Physics, Condensed Matter',	'Physics, Fluids & Plasmas',	'Physics, Mathematical',	'Physics, Multidisciplinary',	'Physics, Nuclear',	'Physics, Particles & Fields',	'Physiology',	'Planning & Development',	'Plant Sciences',	'Poetry',	'Political Science',	'Polymer Science',	'Primary Health Care',	'Psychiatry',	'Psychology',	'Psychology, Applied',	'Psychology, Biological',	'Psychology, Clinical',	'Psychology, Developmental',	'Psychology, Educational',	'Psychology, Experimental',	'Psychology, Mathematical',	'Psychology, Multidisciplinary',	'Psychology, Psychoanalysis',	'Psychology, Social',	'Public Administration',	'Public, Environmental & Occupational Health',	'Radiology, Nuclear Medicine & Medical Imaging',	'Rehabilitation',	'Religion',	'Remote Sensing',	'Reproductive Biology',	'Respiratory System',	'Rheumatology',	'Robotics',	'Social Issues',	'Social Sciences, Biomedical',	'Social Sciences, Interdisciplinary',	'Social Sciences, Mathematical Methods',	'Social Work',	'Sociology',	'Soil Science',	'Spectroscopy',	'Sport Sciences',	'Statistics & Probability',	'Substance Abuse',	'Surgery',	'Telecommunications',	'Theater',	'Thermodynamics',	'Toxicology',	'Transplantation',	'Transportation',	'Transportation Science & Technology',	'Tropical Medicine',	'Urban Studies',	'Urology & Nephrology',	'Veterinary Sciences',	'Virology',	'Water Resources',	'Women's Studies',	'Zoology'}

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

for i in range(0,3):
    driver.get('https://apps.webofknowledge.com/WOS_AdvancedSearch_input.do?locale=en_US&errorKey=&SID=N1TMK4OsNNo7AU7gZyN&product=WOS&errorKey=&errorKey=&search_mode=AdvancedSearch&viewType=input');
    #driver.get('https://apps.webofknowledge.com/WOS_AdvancedSearch_input.do?locale=en_US&errorKey=&viewType=input&SID=N18vVK7TxuPDKozh8s8&product=WOS&search_mode=AdvancedSearch');
    time.sleep(random.randrange(4,6)) # Let the user actually see something!
    #search_box = driver.find_element_by_name('q')
    #search_box.send_keys('ChromeDriver')
    #search_box.submit()
    entertext = "DT=(article or proceedings paper or review) AND PY=2011-2015 AND WC=(" + dicts_from_file[i].rstrip() + ") AND CU=(" + USA + ")"
    driver.find_element_by_id('value(input1)').send_keys(entertext)
    time.sleep(random.randrange(1,2))
    driver.find_element_by_class_name('searchButtons').click()
    time.sleep(random.randrange(1,2))
    driver.find_element_by_class_name('historyResults').click()
    time.sleep(random.randrange(1,2))
    driver.find_element_by_id('OrgEnhancedName_img').click()
    time.sleep(random.randrange(1,2))
    driver.find_element_by_name('OrgEnhancedName').click()
    time.sleep(random.randrange(1,2))
    textdata = driver.find_element_by_id('OrgEnhancedName_raMore_tr').get_attribute('innerHTML')
    file = open("WoS_WC/wc_" + dicts_from_file[i].rstrip() + "_" + str(i) + ".html","w")
    file.write(textdata)
    time.sleep(random.randrange(1,2))
    file.close()
print "----------------------------"
print "all done"
print "----------------------------"
quit()
