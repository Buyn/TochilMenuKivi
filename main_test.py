# ----------------------------------------------
# * import block# :
import unittest
# import main
from main import *
# from model.globalsvar import *


# ----------------------------------------------
# * class Test : 
# ** ----------------------------------------------:
class Test(unittest.TestCase):
# ** @classmethod #setUpClass#  : 
    @classmethod #setUpClass# {{{
    def setUpClass(self):
        print("*"*33,"*"*33)
        self.mw = Main_Windows()
        self.fk = FirstKivy()
    #     print ("file opened")
    #     print("*"*33,"*"*33)
    #     self.gs.sheet_main.update_acell('A1', 'Bingo!')
        
        
# ----------------------------------------------
# ** @classmethod #tearDownClass# : 
    # @classmethod #tearDownClass# {{{
    # def tearDownClass(cls):
    #     print("*"*33,"*"*33)
    #     print("tear down module")
    #     print("*"*33,"*"*33)

# ----------------------------------------------
# ** def test_init1 : 
    def test_init1(self):# {{{
        mw = Main_Windows()
        # temp_A = 11
        # temp_B = 14
        self.assertIsNotNone( mw.temp_A)
        self.assertIsNotNone( mw.temp_B)
        self.assertEqual( mw.temp_A, 11)
        self.assertEqual( mw.temp_B, 14)

            				
# ----------------------------------------------
# ** def firstKivy : 
    def test_firstKivy(self):# {{{
        # self.assertIsNotNone( FirstKivy.build("SDf") )
        self.assertIsNotNone( self.fk.build() )

        
# ----------------------------------------------
# ** def newText : 
    def test_newText(self):# {{{
        self.assertIsNotNone( self.fk.build() )
        self.assertEqual( self.fk.newtext, "New!")

        
# ----------------------------------------------
# ** ----------------------------------------------:
# * class Test_Fun(unittest.TestCase): : 
# ** ----------------------------------------------:
class Test_Fun(unittest.TestCase):

# ** def test_sandbox(self):
    def test_sandbox(self):
        from datetime import date, datetime
        now = datetime.now()
        # print("now =", now)
        # dd/mm/YY H:M:S
        # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        # print("date and time =", dt_string)	
        print("date.today = ", date.today())
        # print("datetime.now = ", 
        #     # datetime.now(tz=None).strftime("%d/%m/%Y %H:%M:%S")
        #     datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        #     )
        print("datetime.now = ", 
            datetime.now().strftime("%d/%m/%Y")
            )
        print("datetime.now = ", 
            datetime.now().strftime("%H:%M:%S")
            )

# ** ----------------------------------------------:
# * def suite Init(): : 
def suite_Init():
    suite = unittest.TestSuite()
    # suite.addTest(Test('test_init1'))
    suite.addTest(Test_Fun('test_sandbox'))
    # suite.addTest(Test('test_firstKivy'))
    # suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite
# ----------------------------------------------


# * Test runer : 
# ----------------------------------------------
# (compile " D:/Development/version-control/GitHub/Vadim/Tochil/main_test.py -k init")
# (compile " python -m unittest D:/Development/version-control/GitHub/Vadim/Tochil/main_test.py ")
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    runner = unittest.TextTestRunner()
    runner.run(suite_Init())
    # unittest.main()
# * ----------------------------------------------:
