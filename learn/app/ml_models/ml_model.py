class MLModel(object):
    def __init__(self, location: str, format: str):
        """
        initalize a model from file location and of type
        format (e.g. pytorch or tensorflow) into an object that
        can be train()'d or can predict()
        """
        self.location = location
        self.format = format

    def __repr__(self):
        return f"MLModel({self.__dict__})"
