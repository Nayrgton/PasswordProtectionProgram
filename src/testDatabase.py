## @file testDatabase.py
#  @brief This file unittests the functions used for.
#  @author Joseph Lu
#  @date November 16, 2017

import unittest
import Encrypt
import database

## @brief
class testDatabase(unittest.TestCase):

    def setUp(self):
        self.keys = [Encrypt.generKey() for i in range(3)]
        database.CreateTables()

    def tearDown(self):
        database.DropTables()

    def test_FRDB4(self):
        database.Insert("First","Test","", Encrypt.cryptEncode(self.keys[0],"First123"), self.keys[0])
        database.Insert("Second","Test","First", Encrypt.cryptEncode(self.keys[1], "Second1"), self.keys[1])
        database.Insert("Third","Test","Username",Encrypt.cryptEncode(self.keys[2], "Third123"), self.keys[2])

        All = database.GetAll()
        Types = database.GetT("Test")
        First_id = database.GetId(1)
	First_Name = database.GetN("First")

	self.assertEqual(len(All), 3)
	self.assertEqual(len(Types), 3)
	self.assertEqual(All[0], First_id)
	self.assertEqual(All[0], First_Name)
	self.assertEqual(Types[0], First_id)
	self.assertEqual(Types[0], First_Name)
	[self.assertEqual(x.AccType, "Test") for x in Types]

    def test_FRDB1(self):
        database.Insert("First","","", Encrypt.cryptEncode(self.keys[0],"First123"), self.keys[0])

        First = database.GetN("First")

        self.assertEqual(First.AccName, "First") # if master password has "First" as Name
        self.assertNotEqual(First.HashVal, "First123") # if master password is directly in database
        self.assertEqual(First.ID, 1)             # if master password has 1 as ID.

    def test_FRDB2_1(self):
        database.Insert("First","","", Encrypt.cryptEncode(self.keys[0],"First123"), self.keys[0])
        database.Insert("Second","","First", Encrypt.cryptEncode(self.keys[1], "Second1"), self.keys[1])
        database.Insert("Third","Type","Username",Encrypt.cryptEncode(self.keys[2], "Third123"), self.keys[2])
        oldQuery = database.GetN("First")

        database.UpdateP(1,Encrypt.cryptEncode(self.keys[0], "First321"))

        newQuery = database.GetN("First")

        self.assertEqual(oldQuery.ID, newQuery.ID)
        self.assertNotEqual(Encrypt.cryptDecode(self.keys[0],oldQuery.HashVal.encode('utf-8')), Encrypt.cryptDecode(self.keys[0],newQuery.HashVal.encode('utf-8')))

    def test_FRDB2_2(self):
        database.Insert("First","","", Encrypt.cryptEncode(self.keys[0],"First123"), self.keys[0])
        database.Insert("Second","","First", Encrypt.cryptEncode(self.keys[1], "Second1"), self.keys[1])
        database.Insert("Third","Type","Username",Encrypt.cryptEncode(self.keys[2], "Third123"), self.keys[2])
        oldQuery = database.GetN("First")

        database.UpdateU(1,"ChangedFirst")

        newQuery = database.GetN("First")

        self.assertEqual(oldQuery.ID, newQuery.ID)
        self.assertNotEqual(oldQuery.UserName, newQuery.UserName)
    
    def test_FRDB3(self):
        database.Insert("First","","", Encrypt.cryptEncode(self.keys[0],"First123"), self.keys[0])
        database.Insert("Second","","First", Encrypt.cryptEncode(self.keys[1], "Second1"), self.keys[1])
        database.Insert("Third","Type","Username",Encrypt.cryptEncode(self.keys[2], "Third123"), self.keys[2])
        
        databaseLengthBefore = len(database.GetAll())
        oldQuery = database.GetId(1)

        database.Delete(1)

        databaseLengthAfter = len(database.GetAll())

        self.assertEqual(oldQuery.AccName, "First")
        with self.assertRaises(IndexError):
        	database.GetId(1)

if __name__ == '__main__':
    unittest.main()

