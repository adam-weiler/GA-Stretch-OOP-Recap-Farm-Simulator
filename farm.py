class Field:
    fields = []
    food_harvested = 0

    def __init__(self, crop, hectare):
        '''This method initializes a new Field, with crop 
        and hectare as attributes.'''
        self.crop = crop
        self.hectare = hectare

    def __str__(self):
        return f'Your {self.crop.capitalize()} field is {self.hectare} hectares.'

    @classmethod
    def create(cls, new_crop, new_hectare):
        '''This classmethod creates a new Field object, 
        appends it to the fields list, and returns a 
        message.'''
        new_field = Field(new_crop, new_hectare)
        cls.fields.append(new_field)
        return f'Added a {new_field.crop} field of {new_field.hectare} hectares!'

    @classmethod
    def harvest_crops(cls):
        '''This classmethod harvests each Field in the 
        fields list, adds to the food_harvested total,
        and returns a message.'''
        if len(cls.fields) > 0:
            for field in cls.fields:
                if field.crop == 'corn':
                    food = field.hectare * 20
                elif field.crop == 'wheat':
                    food = field.hectare * 30
                cls.food_harvested += food
                print (f'Harvesting {food} food from a {field.hectare} hectare {field.crop} field.')
            return f'The farm has {cls.food_harvested} harvested food so far.'
        else:
            return 'You haven\'t planted anything yet!'

    @classmethod
    def check_status(cls):
        '''This classmethod prints each Field's __str__
        method, and returns a message.'''
        if len(cls.fields) > 0:
            for field in cls.fields:
                print (f'{field}')
        #This will return a statement, even if there are no Fields.
        return f'The farm has {cls.food_harvested} harvested food so far.'

    @classmethod
    def relax(cls):
        '''This classmethod prints a desiption for each Field,
        based on the crop, and returns a message.'''
        if len(cls.fields) > 0:
            for field in cls.fields:
                if field.crop == 'corn':
                    print (f'{field.hectare} hectares of tall green stalks rustling in the breeze fill your horizon.')
                elif field.crop == 'wheat':
                    print (f'The sun hangs low, casting an orange glow on a sea of {field.hectare} hectares of wheat.')
            return 'Wasn\'t that nice?'
        else:
            return 'You haven\'t planted anything yet!'