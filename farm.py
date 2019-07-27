class Field:
    fields = []
    food_harvested = 0

    def __init__(self, crop, hectare):
        '''This method iniatlizes a new Field, with crop and hectare as attributes.'''
        self.crop = crop
        self.hectare = hectare

    def __str__(self):
        return f'Your {self.crop.capitalize()} field is {self.hectare} hectares.'

    @classmethod
    def create(cls, new_crop, new_hectare):
        new_field = Field(new_crop, new_hectare)
        cls.fields.append(new_field)
        print(f'Added a {new_field.crop} field of {new_field.hectare} hectares!')
        return new_field

    @classmethod
    def harvest_crops(cls):
        # pass #Collect food from all fields. 
        #Record total
        #Display

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
    def check_status(cls): #Status of fields (size, type)
        if len(cls.fields) > 0:
            for field in cls.fields:
                print (f'{field}')
        # else:
        #     print('You haven\'t harvested anything yet!')
        # pass #How much food produced till now.
        return f'The farm has {cls.food_harvested} harvested food so far.'


    @classmethod
    def relax(cls): #Provides lovely description of fields?
        if len(cls.fields) > 0:
            for field in cls.fields:
                if field.crop == 'corn':
                    print (f'{field.hectare} hectares of tall green stalks rustling in the breeze fill your horizon.')
                elif field.crop == 'wheat':
                    print (f'The sun hangs low, casting an orange glow on a sea of {field.hectare} hectares of wheat.')
            return 'Wasn\'t that nice?'
        else:
            return 'You haven\'t planted anything yet!'