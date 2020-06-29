# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1
class NewsStory():
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    
    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate
    
# TODO: NewsStory


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, string_phrase):
        self.phrase = str.lower(string_phrase)
        
    def is_phrase_in(self, text):
        text_proper = str.lower(text)
        punctuation = string.punctuation
        for punct in punctuation:
            if punct in text_proper:
                text_proper = text_proper.replace(punct, " ")
        text_list = text_proper.split()
        text_check = " ".join(text_list)
        result_list = []
        for word in text_list:
            if word in self.phrase and word not in result_list:
                result_list.append(word)
        result_phrase = " ".join(result_list)
        return self.phrase == result_phrase and result_phrase in text_check
    

                
        
# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def __init__(self, string_phrase):
        PhraseTrigger.__init__(self, string_phrase)
    
    def evaluate(self, story):
        title = story.get_title()
        return super().is_phrase_in(title)
        
# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, string_phrase):
        PhraseTrigger.__init__(self, string_phrase)
    
    def evaluate(self, story):
        desc = story.get_description()
        return super().is_phrase_in(desc)
# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, time_string):
        self.t_date = datetime.strptime(time_string, "%d %b %Y %H:%M:%S")
        #self.t_date = self.t_date.replace(tzinfo=pytz.timezone("EST"))
        #self.t_date = t_date.replace(tzinfo=pytz.timezone("EST"))


# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    
    def evaluate(self, news):
        news_date = news.get_pubdate().replace(tzinfo=None)
        return self.t_date > news_date


class AfterTrigger(TimeTrigger):
    
    def evaluate(self, news):
        news_date = news.get_pubdate().replace(tzinfo=None)
        return self.t_date < news_date

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, other_trigger):
        self.evaluate_trigger = other_trigger
    
    def evaluate(self, news_piece):
        result = self.evaluate_trigger.evaluate(news_piece)
        return not result
# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, triggerA, triggerB):
        self.A = triggerA
        self.B = triggerB
    
    def evaluate(self, news_piece):
        result_A = self.A.evaluate(news_piece)
        result_B = self.B.evaluate(news_piece)
        return result_A and result_B
# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, triggerA, triggerB):
        self.A = triggerA
        self.B = triggerB
    
    def evaluate(self, news_piece):
        result_A = self.A.evaluate(news_piece)
        result_B = self.B.evaluate(news_piece)
        return result_A or result_B

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    filtered_stories = []
    for st in stories:
        for t in triggerlist:
            if t.evaluate(st):
                filtered_stories.append(st)
    return filtered_stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
# =============================================================================
# =============================================================================
    trigger_dict = {"TITLE": TitleTrigger, "DESCRIPTION": DescriptionTrigger, 
                    "AFTER": AfterTrigger, "BEFORE": BeforeTrigger}
    logic_trigger = {"NOT": NotTrigger, "AND": AndTrigger, "OR": OrTrigger}
    result_trigger_dict = {}
    for spec in lines:
        spec_list = spec.split(",")
        if spec_list[1] in trigger_dict:
            t = trigger_dict[spec_list[1]]
            result_trigger_dict[spec_list[0]] = t(spec_list[2])
        elif spec_list[1] in logic_trigger:
            logic_t = logic_trigger[spec_list[1]]
            result_trigger_dict[spec_list[0]] = logic_t(spec_list[2], spec_list[3])
    result_list = []
    for spec in lines:
        if spec[0:3] == "ADD":
            add_cmd = spec.split(",")
            for entry in add_cmd:
                if entry in result_trigger_dict:
                    result_list.append(result_trigger_dict[entry])

    
# =============================================================================
#     trig_dict = {}
#     trig_list = []
#     for i in range(len(lines)):
#         trig = lines[i].split(',')
#         if trig[1] == 'TITLE':
#             trig_dict[trig[0]] = TitleTrigger(trig[2])
#         elif trig[1] == 'DESCRIPTION':
#             trig_dict[trig[0]] = DescriptionTrigger(trig[2])
#         elif trig[1] == 'AFTER':
#             trig_dict[trig[0]] = AfterTrigger(trig[2])
#         elif trig[1] == 'BEFORE':
#             trig_dict[trig[0]] = BeforeTrigger(trig[2])
#         elif trig[1] == 'NOT':
#             trig_dict[trig[0]] = NotTrigger(trig[2])
#         elif trig[1] == 'AND':
#             trig_dict[trig[0]] = AndTrigger(trig_dict[trig[2]], trig_dict[trig[3]])
#         elif trig[0] == 'ADD':
#             for x in range(1, len(trig)):
#                 trig_list.append(trig_dict[trig[x]])
#     return trig_list
# =============================================================================

    return result_list # for now, print it so you see what it contains!
    



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Biden")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

