import playsound
import speech as sp
import speechRecognizer as recog

def site_selection():   
    text=""
    while text!="exit":
        sp.speak("Please select your web site")
        try: 
            text=recog.talk()
            if "Facebook" in text:
                condition = "Facebook"
                print("Share/Like/Comment")
                in_site_selection(condition)
                print("Thank You For using Facebook") 

            elif "Google" in text:
                condition = "Google"
                print("Search your content")
                in_site_selection(condition)
                print("Thank You For using Google") 
                            
            elif "eBay" in text:
                condition = "eBay"
                sp.speak("eBay it is")
                in_site_selection(condition)
                print("Thank You For using Ebay")
        except:
            print("Unknown Command (site_selection)")    

def in_site_selection(condition):
    text=""
    sp.speak("Please select what you want to do in here") 
    while text!="exit":    
        try:
            text=recog.talk()
            if condition=="eBay":
                import eBay_Controller as ebay
                ebay.commands(text)

            elif condition=="Facebook":
                print("condition")
                import Facebook_Gmail as fg
                fg.facebook()
                            
            elif condition=="Google":
                import Facebook_Gmail as fg
                fg.google(text)
        except:
            print("Unknown Command (in_site_selection)")   


site_selection()