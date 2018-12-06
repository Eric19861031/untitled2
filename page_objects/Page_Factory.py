from page_objects.Demo_Page import Demo_page
from conf.page_dict import page

class PageFactory():

    @staticmethod
    def get_page_object(page_name):

        for key,value in page.items():
            if key == page_name.lower():
                test_obj = value

        return test_obj