from selenium import webdriver
from selenium.webdriver.common.by import By  # Import By for locating elements
import random
import time

webdriver = webdriver.Chrome()
webdriver.get("https://forms.gle/4z9woYnGGQWBc9fv9")
time.sleep(2)

# region Kāds ir jūsu dzimums?
o11xpath = '//*[@id="i5"]/div[3]/div'
o12xpath = '//*[@id="i8"]/div[3]/div'

# Randomly choose between the first and second option
choice_xpath = random.choice([o11xpath, o12xpath])

# Find the chosen option using its XPath and click it
choice_element = webdriver.find_element(By.XPATH, choice_xpath)
choice_element.click()

# Short delay to ensure the page reacts to the click
time.sleep(1)
# endregion

# region Kāds ir jūsu vecums gados?
o21xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'

# Generate a random number from 15 to 50
random_age = random.randint(15, 50)

# Find the text box using its XPath
o21 = webdriver.find_element(By.XPATH, o21xpath)

# Input the random number into the text box
o21.send_keys(str(random_age))

# Short delay to ensure the page reacts to the click
time.sleep(1)
# endregion

# region Kāds ir jūsu augstākais izglītības līmenis?
o31xpath = '//*[@id="i19"]/div[3]/div'
o32xpath = '//*[@id="i22"]/div[3]/div'
o33xpath = '//*[@id="i25"]/div[3]/div'
o34xpath = '//*[@id="i28"]/div[3]/div'
o35xpath = '//*[@id="i31"]/div[3]/div'
o36xpath = '//*[@id="i34"]/div[3]/div'
# Doktora studijas ir pārāk retas
# o37xpath = '//*[@id="i37"]/div[3]/div'

# Randomly choose between the first and seventh option
choice_xpath = random.choice([o31xpath, o32xpath, o33xpath, o34xpath, o35xpath, o36xpath
                              # , o37xpath
                              ])

# Find the chosen option using its XPath and click it
choice_element = webdriver.find_element(By.XPATH, choice_xpath)
choice_element.click()

# Short delay to ensure the page reacts to the click
time.sleep(1)
# endregion

# region Kāda ir jūsu nodarbošanās?
o41xpath = '//*[@id="i44"]/div[3]/div'
o42xpath = '//*[@id="i47"]/div[3]/div'
o43xpath = '//*[@id="i50"]/div[3]/div'
o44xpath = '//*[@id="i53"]/div[3]/div'

# Randomly choose between the first and second option
choice_xpath = random.choice([o41xpath, o42xpath, o43xpath, o44xpath])

# Find the chosen option using its XPath and click it
choice_element = webdriver.find_element(By.XPATH, choice_xpath)
choice_element.click()

# Short delay to ensure the page reacts to the click
time.sleep(1)
# endregion

# region Kādi ir jūsu ienākumi mēnesī eiro "uz rokas"? (NAV OBLIGĀTS)
o51xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'
# Calculate the range of valid numbers divisible by 50 between 0 and 3000
valid_wage = [number for number in range(0, 3001, 50)]

# Randomly select a number from the valid numbers
random_wage = random.choice(valid_wage)

# Find the text box using its XPath
o51 = webdriver.find_element(By.XPATH, o51xpath)

# Input the random number into the text box
o51.send_keys(str(random_wage))

# Short delay to ensure the page reacts to the click
time.sleep(1)
# endregion

# region Kurus sociālos medijus jūs izmantojat?
# List of XPaths for the checkboxes
xpath_list = [
    '//*[@id="i65"]/div[2]',
    '//*[@id="i68"]/div[2]',
    '//*[@id="i71"]/div[2]',
    '//*[@id="i74"]/div[2]',
    '//*[@id="i77"]/div[2]',
    '//*[@id="i80"]/div[2]',
    '//*[@id="i83"]/div[2]',
    '//*[@id="i86"]/div[2]',
    '//*[@id="i89"]/div[2]',
    '//*[@id="i92"]/div[2]',
    '//*[@id="i95"]/div[2]',
    '//*[@id="i98"]/div[2]',
    '//*[@id="i101"]/div[2]',
    '//*[@id="i104"]/div[2]',
]

clicked_xpaths = []  # List to keep track of clicked XPaths

num_iterations = random.randint(1, 14)  # Generate a random number between 1 and 14

for _ in range(num_iterations):
    # Filter out XPaths that have already been clicked
    available_xpaths = [xpath for xpath in xpath_list if xpath not in clicked_xpaths]

    # Check if there are still any checkboxes left to click
    if not available_xpaths:
        print("All checkboxes have been clicked.")
        break

    # Randomly choose from the remaining options
    choice_xpath = random.choice(available_xpaths)

    # Find the chosen option using its XPath and click it
    choice_element = webdriver.find_element(By.XPATH, choice_xpath)
    choice_element.click()

    # Add the clicked XPath to the list of clicked XPaths
    clicked_xpaths.append(choice_xpath)

    # Short delay to ensure the page reacts to the click
    time.sleep(1)
# endregion

# region Cik bieži jūs imantojat sociālos medijus?
# Only the first three options are picked
o71xpath = '//*[@id="i111"]/div[3]/div'
o72xpath = '//*[@id="i114"]/div[3]/div'
o73xpath = '//*[@id="i117"]/div[3]/div'
o74xpath = '//*[@id="i120"]/div[3]/div'
o75xpath = '//*[@id="i123"]/div[3]/div'

# Randomly choose between the first and seventh option
choice_xpath = random.choice([o71xpath, o72xpath, o73xpath, o74xpath, o75xpath])

# Find the chosen option using its XPath and click it
choice_element = webdriver.find_element(By.XPATH, choice_xpath)
choice_element.click()

# Short delay to ensure the page reacts to the click
time.sleep(1)
# endregion

# region Cik stundas dienā vidēji pavadāt, lietojot sociālos medijus ?
o81xpath = '//*[@id="i130"]/div[3]/div'
o82xpath = '//*[@id="i133"]/div[3]/div'
o83xpath = '//*[@id="i136"]/div[3]/div'
o84xpath = '//*[@id="i139"]/div[3]/div'
o85xpath = '//*[@id="i142"]/div[3]/div'
o86xpath = '//*[@id="i145"]/div[3]/div'

# Randomly choose between the first and seventh option
choice_xpath = random.choice([o81xpath, o82xpath, o83xpath, o84xpath, o85xpath, o86xpath])

# Find the chosen option using its XPath and click it
choice_element = webdriver.find_element(By.XPATH, choice_xpath)
choice_element.click()

# Short delay to ensure the page reacts to the click
time.sleep(1)
# endregion

# region Kā jūs vērtējat sociālo mediju ietekmi uz jūsu dzīves kvalitāti?
o91xpath = '//*[@id="i152"]/div[3]/div'
o92xpath = '//*[@id="i155"]/div[3]/div'
o93xpath = '//*[@id="i158"]/div[3]/div'
o94xpath = '//*[@id="i161"]/div[3]/div'
o95xpath = '//*[@id="i164"]/div[3]/div'

# Randomly choose between the first and seventh option
choice_xpath = random.choice([o91xpath, o92xpath, o93xpath, o94xpath, o95xpath])

# Find the chosen option using its XPath and click it
choice_element = webdriver.find_element(By.XPATH, choice_xpath)
choice_element.click()

# Short delay to ensure the page reacts to the click
time.sleep(1)
# endregion

# region Kā sociālie mediji ietekmē jūsu emocionālo labsajūtu
o101xpath = '//*[@id="i171"]/div[3]/div'
o102xpath = '//*[@id="i174"]/div[3]/div'
o103xpath = '//*[@id="i177"]/div[3]/div'
o104xpath = '//*[@id="i180"]/div[3]/div'
o105xpath = '//*[@id="i183"]/div[3]/div'

# Randomly choose between the first and seventh option
choice_xpath = random.choice([o101xpath, o102xpath, o103xpath, o104xpath, o105xpath])

# Find the chosen option using its XPath and click it
choice_element = webdriver.find_element(By.XPATH, choice_xpath)
choice_element.click()

# Short delay to ensure the page reacts to the click
time.sleep(1)
# endregion

# region Kā sociālie mediji ir ietekmējuši jūsu profesionālo izaugsmi vai kerjeras attīstību?
o111xpath = '//*[@id="i190"]/div[3]/div'
o112xpath = '//*[@id="i193"]/div[3]/div'
o113xpath = '//*[@id="i196"]/div[3]/div'
o114xpath = '//*[@id="i199"]/div[3]/div'
o115xpath = '//*[@id="i202"]/div[3]/div'

# Randomly choose between the first and seventh option
choice_xpath = random.choice([o111xpath, o112xpath, o113xpath, o114xpath, o115xpath])

# Find the chosen option using its XPath and click it
choice_element = webdriver.find_element(By.XPATH, choice_xpath)
choice_element.click()

# Short delay to ensure the page reacts to the click
time.sleep(1)
# endregion

# region Vai sociālie mediji ir palīdzējuši uzlabot jūsu sociālās saites?
o121xpath = '//*[@id="i209"]/div[3]/div'
o122xpath = '//*[@id="i212"]/div[3]/div'
o123xpath = '//*[@id="i215"]/div[3]/div'

# Randomly choose between the first and seventh option
choice_xpath = random.choice([o121xpath, o122xpath, o123xpath])

# Find the chosen option using its XPath and click it
choice_element = webdriver.find_element(By.XPATH, choice_xpath)
choice_element.click()

# Short delay to ensure the page reacts to the click
time.sleep(1)
# endregion

# region Vai sociālie mediji ir jūsu galvenais informācijas avots par notikumiem pasaulē?
o131xpath = '//*[@id="i222"]/div[3]/div'
o132xpath = '//*[@id="i225"]/div[3]/div'
o133xpath = '//*[@id="i228"]/div[3]/div'

# Randomly choose between the first and seventh option
choice_xpath = random.choice([o131xpath, o132xpath, o133xpath])

# Find the chosen option using its XPath and click it
choice_element = webdriver.find_element(By.XPATH, choice_xpath)
choice_element.click()

# Short delay to ensure the page reacts to the click
time.sleep(1)
# endregion

# region Vai esat mainījuši savu uzvedību un viedokļus,ietekmēti no informācijas,ko saņēmāt caur sociālajiem medijiem?
o141xpath = '//*[@id="i235"]/div[3]/div'
o142xpath = '//*[@id="i238"]/div[3]/div'
o143xpath = '//*[@id="i241"]/div[3]/div'

# Randomly choose between the first and seventh option
choice_xpath = random.choice([o141xpath, o142xpath, o143xpath])

# Find the chosen option using its XPath and click it
choice_element = webdriver.find_element(By.XPATH, choice_xpath)
choice_element.click()

# Short delay to ensure the page reacts to the click
time.sleep(1)
# endregion

# region Kā jūs vērtējat informācijas uzticamību, ko saņemat caur sociālajiem medijiem?
o151xpath = '//*[@id="i248"]/div[3]/div'
o152xpath = '//*[@id="i251"]/div[3]/div'
o153xpath = '//*[@id="i254"]/div[3]/div'
o154xpath = '//*[@id="i257"]/div[3]/div'
o155xpath = '//*[@id="i260"]/div[3]/div'

# Randomly choose between the first and seventh option
choice_xpath = random.choice([o151xpath, o152xpath, o153xpath, o154xpath, o155xpath])

# Find the chosen option using its XPath and click it
choice_element = webdriver.find_element(By.XPATH, choice_xpath)
choice_element.click()

# Short delay to ensure the page reacts to the click
time.sleep(1)
# endregion

# region iesniegt
sbxpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'

# Find the submit button and click it
submit_button = webdriver.find_element(By.XPATH, sbxpath)
submit_button.click()

# Close the browser after a short delay
time.sleep(3)
webdriver.quit()
# endregion
