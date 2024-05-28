#!/usr/bin/env python3
import pickle

""" Defines a custom Python class named CustomObject. """


class CustomObject:
    """ Initializes the attributes. """
    def __init__(self, name, age, is_student):
        """ Initialization with name, age and is_student. """
        self.name = name
        self.age = age
        self.is_student = is_student

    """ A display method that prints out the object's attributes. """
    def display(self):
        """ Displays the formated output."""
        if self.is_student:
            is_student = "True"
        else:
            is_student = "False"
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    """ A serialize method that serializes the current instance of the object
        and save it to the provided filename.
    """
    def serialize(self, filename):
        """ Serialize custom Python objects using the pickle module.
        
        Args:
            filename: The name of the file from which it serialized.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization error: {e}")

    """ A class method named deserialize that loads and returns an instance of
        the CustomObject from the provided filename.
    """
    @classmethod
    def deserialize(cls, filename):
        """ Deserialize custom Python objects using the pickle module.
        
        Args:
            cls: The custom class CustomObject.
            filename: The name of the file from which it deserialized.
        Returns:
            An instance of the CustomObject from the provided filename or
            otherwise None.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                else:
                    print("File does not contain the CustomObject instance.")
                    return None
        except Exception as e:
            print(f"Deserialization error: {e}")
            return None
