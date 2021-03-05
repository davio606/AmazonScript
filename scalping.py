import time 
from selenium import webdriver 

browser = webdriver.Chrome('/Users/david/chromedriver')

browser.get("https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF/ref=sr_1_3?dchild=1&keywords=ryzen+5&qid=1614731958&s=electronics&sr=1-3")

buyButton = False

while not buyButton:

	try:

		addToCartBtn = addButton = browser.find_element_by_id("add-to-cart-button")
		addToCartBtn.click()
		print("Added I think")

		time.sleep(1)

		#protectionPlanButton = planButton = browser.find_element_by_id("attachSiNoCoverage-announce")
		protectionPlanButton = planButton = browser.find_element_by_xpath('//button[@id="attachSiNoCoverage-announce"]')
		protectionPlanButton.click()
		print("clicked maybe")

		time.sleep(1)

		proceedToCheckoutButton = checkoutButton = browser.find_element_by_xpath('//input[@aria-labelledby="attach-sidesheet-checkout-button-announce"]')
		proceedToCheckoutButton.click()
		print("clicked?")

		#sign in
		email_area = browser.find_element_by_id("ap_email")
		email_area.send_keys("XXXXXXX")

		continueButton = continuedButton = browser.find_element_by_xpath('//input[@aria-labelledby="continue-announce"]')
		continueButton.click()
		print("email entered")

		password_area = browser.find_element_by_id("ap_password")
		password_area.send_keys("XXXXXXX")

		signInButton = signButton = browser.find_element_by_xpath('//input[@aria-labelledby="auth-signin-button-announce"]')
		signInButton.click()
		print("signed in!")

		buyButton = True
		# credit card plus buy?

	except:

		print("not added")
		time.sleep(1)
		browser.refresh()