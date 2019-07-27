class Field:
    fields = []

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
        return(new_field)

    def harvest_crops(self):
        pass #Collect food from all fields. 
        #Record total
        #Display

    @classmethod
    def check_status(cls): #Status of fields (size, type)
        if len(cls.fields) > 0:
            for field in cls.fields:
                print (f'{field}')
            return f'The farm has 27? harvested food so far.'
        else:
            print('You haven\'t harvested anything yet!')
        pass #How much food produced till now.

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