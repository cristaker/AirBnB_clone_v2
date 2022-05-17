#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """this class is for test """

    def test_ClassExist(self):
        """verify class exist"""

        clp = "<class 'models.place.Place'>"
        pl = Place()
        self.assertTrue(str(type(pl)), clp)

    def test_attributeExist(self):
        """verify attributes exist"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ test_city_id """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ test_name """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ test_description """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ test_number_rooms """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ test_number_bathrooms """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ test_max_guest """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ test_price_by_night """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ test_latitude """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ test_latitude """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_place_ids(self):
        """ test_latitude """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    def setUpClass(cls):
        pass

    def test_pep8_conformance_place(self):
        pass

    def test_pep8_conformance_test_place(self):
        pass

    def test_place_module_docstring(self):
        pass

    def test_place_class_docstring(self):
        pass

    def test_place_func_docstrings(self):
        pass


    def test_is_subclass(self):
        pass

    def test_name_attr(self):
        pass

    def test_to_dict_creates_dict(self):
        pass

    def test_str(self):
        pass
