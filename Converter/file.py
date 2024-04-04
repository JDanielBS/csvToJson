'''Module that provides the File class'''

class File:
    '''
    Class that represents a file in the file system. 

    ...

    Attributes
    ----------
    path: str
        the path of the file in the file system
    '''

    def __init__(self, path):
        self.__path = path

    def get_path(self) -> str:
        '''
        Returns the path of the file
        '''

        return self.__path
