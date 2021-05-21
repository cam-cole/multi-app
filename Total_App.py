#Cameron's App
#Developed by Cameron Cole

#Import Packages
import tkinter as tk
import yfinance as yf
from selenium import webdriver
import time
import random
from random import randint

#Function to quit entire Application
def quit_main():
    main.destroy()
 
#Function to create and run Greenfield Application
def greenfield_application():
    #Function to get Greenfield card number input and download card
    def get_cards():
        driver = webdriver.Chrome(#File Path to Chromedriver)
        driver.get(#Web address for Target's Greenfield Website)
        time.sleep(20)
        list = card_entry.get()
        list = list.split(',')
    
        for i in list:
            driver.get(#Web address for Target's Greenfield website 
                + str(i))
            time.sleep(9)

            drop_down_menu = driver.find_element_by_id('card-view-more')
            drop_down_menu.click()

            export_csv = driver.find_element_by_id('export-to-csv-btn')
            export_csv.click()
        
        time.sleep(5)
        driver.close()
     
    #Function to quit Greenfield Application
    def quit():
        greenfield_window.destroy()
    
    #Window Configuration for Greenfield Application
    greenfield_window = tk.Tk()
    greenfield_window.title("Greenfield Download App")

    card_label = tk.Label(master = greenfield_window,text = 'Enter Card Numbers Below:', bg = 'black', fg = 'light green')
    card_entry = tk.Entry(master = greenfield_window)
    download_button = tk.Button(master = greenfield_window, text = 'Download Cards', bg = 'black', fg = 'light green', command = get_cards)
    quit_button = tk.Button(master = greenfield_window, text = 'Quit', bg = 'black', fg = 'light green', command=quit)

    card_label.grid(row = 0, column = 0, sticky = 'nsew')
    card_entry.grid(row = 1, column = 0, sticky = 'nsew')
    download_button.grid(row = 0, column = 1, sticky = 'nsew')
    quit_button.grid(row = 1, column = 1, sticky = 'nsew')

    #Run Greenfield_Application
    greenfield_window.mainloop()


#Function to create and run Dice Roll Application
def dice_roll_application():
    #Function to roll two dice in Dice Roll Application
    def dice_roll():
        label_result['text'] = 'Your dice roll is: ' + str(randint(1,6) + randint(1,6))
    
    #Function to roll one die in Dice Roll Application
    def die_roll():
        label_result['text'] = 'Your die roll is: ' + str(randint(1,6))
    
    #Function to quit Dice Roll Application
    def quit():
        dice_window.destroy()

    #Window Configuration for Dice Roll Application
    dice_window = tk.Tk()
    dice_window.title('Dice Rolling App')

    button_roll = tk.Button(master = dice_window, text = 'One Die', command=die_roll, bg = 'black', fg = 'red')
    button_roll2 = tk.Button(master = dice_window, text = 'Two Dice', command=dice_roll, bg = 'black', fg = 'red')
    label_result = tk.Label(master = dice_window, bg = 'black', fg = 'red', width = 20)
    quit_button = tk.Button(master = dice_window, text = 'Quit', bg = 'black', fg = 'red', command = quit)

    button_roll.grid(row= 0, column = 0, sticky = 'nsew')
    button_roll2.grid(row = 1, column = 0, sticky = 'nsew')
    label_result.grid(row = 0, column = 1, sticky = 'nsew')
    quit_button.grid(row = 1, column = 1, sticky = 'nsew')

    #Run Dice Roll Application
    dice_window.mainloop()

#Function to create and run Stock Application
def stock_application():
    #Function to take stock ticker and get stock price
    def get_current_price():
        tick = ticker_entry.get()
        ticker = yf.Ticker(tick)
        company_name = ticker.info['longName']
        todays_data = ticker.history(period = '1d')
        stock_price = str(todays_data['Close'][0])
        stock_price_label.configure(text = company_name + ' Price is: ' + stock_price)
    
    #Function to quit Stock Application   
    def quit():
        stock_window.destroy()
    
    #Function to clear Stock Application inputs
    def clear():
        ticker_entry.delete('0', 'end')
        stock_price_label.configure(text = '')

    #Window Configuration for Stock Application   
    stock_window = tk.Tk()
    stock_window.title('Stock Price Application')

    stock_ticker = tk.Label(master = stock_window,text = 'Enter Stock Ticker:', bg = 'black', fg = 'red')
    ticker_entry = tk.Entry(master = stock_window, width = 40)
    submit_button = tk.Button(master = stock_window, text = 'Submit', bg = 'black', fg = 'red', command = get_current_price)
    stock_price_label = tk.Label(master = stock_window, bg = 'black', fg = 'red')
    clear_button = tk.Button(master = stock_window, text = 'Clear', bg = 'black', fg = 'red', command = clear)
    quit_button = tk.Button(master = stock_window, text = 'Quit', bg = 'black', fg = 'red', command = quit)

    stock_ticker.grid(row = 0, column = 0, sticky = 'nsew')
    ticker_entry.grid(row = 1, column = 0, sticky = 'nsew')
    stock_price_label.grid(row = 2, column = 0, sticky = 'nsew')
    submit_button.grid(row = 0, column = 1, sticky = 'nsew')
    clear_button.grid(row = 1, column = 1, sticky = 'nsew')
    quit_button.grid(row = 2, column = 1, sticky = 'nsew')

    #Run Stock Application
    stock_window.mainloop()
    
#Function to create and run Number Generator Application   
def number_generator_application():
    def generate_number():
        low = int(low_number.get())
        high = int(high_number.get())
        number = random.randint(low, high)
        number_label.configure(text = number)
    
    #Function to quit Number Generator Application
    def quit():
        number_window.destroy()
    
    #Function to clear Number Generator Application inputs
    def clear():
        low_number.delete('0', 'end')
        high_number.delete('0', 'end')
        number_label.configure(text = '')

    #Window Configuration for Number Generator Application   
    number_window = tk.Tk()
    number_window.title('Random Number Generator')
    
    number_range = tk.Label(master = number_window, text = 'Enter Number Range:', bg = 'black', fg = 'light green')
    low_number = tk.Entry(master = number_window, width = 40)
    high_number = tk.Entry(master = number_window, width = 40)
    generate_button = tk.Button(master = number_window, text = 'Generate', bg = 'black', fg = 'light green', command = generate_number)
    number_label = tk.Label(master = number_window, bg = 'black', fg = 'light green')
    clear_button = tk.Button(master = number_window, text = 'Clear', bg = 'black', fg = 'light green', command = clear)
    quit_button = tk.Button(master = number_window, text = 'Quit', bg = 'black', fg = 'light green', command = quit)
    declaration = tk.Label(master = number_window, text = 'Your random generated number is: ', bg = 'black', fg = 'light green')

    number_range.grid(row = 0, column = 0, sticky = 'nsew')
    low_number.grid(row = 1, column = 0, sticky = 'nsew')
    high_number.grid(row = 2, column = 0, sticky = 'nsew')
    declaration.grid(row = 3, column = 0, sticky = 'nsew')
    generate_button.grid(row = 0, column = 1, sticky = 'nsew')
    clear_button.grid(row = 1, column = 1, sticky = 'nsew')
    quit_button.grid(row = 2, column = 1, sticky = 'nsew')
    number_label.grid(row = 3, column = 1, sticky = 'nsew')

    #Run Number Generator Application
    number_window.mainloop()


#Function to create and run Google Search Application
def google_search_app():
    #Function to perform Google Search
    def search_google():
        driver = webdriver.Chrome(r"C:\Users\Z0052V1\Documents\chromedriver.exe")
        driver.get('https://www.google.com/')
        time.sleep(5)
        search_term = str(term_entry.get())
        
        search_box = driver.find_element_by_name('q')
        search_box.send_keys(search_term)
        
        execute_search = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
        execute_search.click()
      
    #Function to quit Google Search Application    
    def quit():
        google_window.destroy()
        
    #Window Configuration for Google Search Application
    google_window = tk.Tk()
    google_window.title('Google Search')
    
    term_label = tk.Label(master = google_window, text = 'Enter your search term or phrase below: ', bg = 'black', fg = 'orange')
    term_entry = tk.Entry(master = google_window)
    search_button = tk.Button(master = google_window, text = 'Search', bg = 'black', fg = 'orange', command = search_google)
    quit_google = tk.Button(master = google_window, text = 'Quit', bg = 'black', fg = 'orange', command = quit)
    
    term_label.grid(row = 0, column = 0, sticky = 'nsew')
    term_entry.grid(row = 1, column = 0, sticky = 'nsew')
    search_button.grid(row = 0, column = 1, sticky = 'nsew')
    quit_google.grid(row = 1, column = 1, sticky = 'nsew')
    
    #Run Google Search Application
    google_window.mainloop()


#Main Window
main = tk.Tk()
main.title('Multitool App')

number_generator_app = tk.Button(text = 'Number Generator', bg = 'black', fg = 'red', command = number_generator_application)
dice_app = tk.Button(text = 'Dice Roll App', bg = 'black', fg = 'red', command = dice_roll_application)
greenfield_app = tk.Button(text = 'Greenfield Download', bg = 'black', fg = 'red', command = greenfield_application)
stock_app = tk.Button(text = 'Stock Prices', bg = 'black', fg = 'red', command = stock_application)
google_app = tk.Button(text = 'Google Search', bg = 'black', fg = 'red', command = google_search_app)
main_quit = tk.Button(text = 'Quit', bg = 'black', fg = 'red', command = quit_main)

number_generator_app.grid(row = 0, column = 0, sticky = 'nsew')
dice_app.grid(row = 1, column = 0, sticky = 'nsew')
greenfield_app.grid(row = 0, column = 1, sticky = 'nsew')
stock_app.grid(row = 1, column = 1, sticky = 'nsew')
google_app.grid(row = 2, column = 0, sticky = 'nsew')
main_quit.grid(row = 2, column = 1, sticky = 'nsew')

main.mainloop()
