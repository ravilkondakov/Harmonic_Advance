from django.db import models
from django.utils.translation import gettext as _


class Numbers(models.Model):
    '''
    create a database
    '''
    numbers = models.CharField(max_length=100, name=_('numbers'))
    target = models.IntegerField(name=_('target'))

    '''
    make a property for return current indexes from set
    '''
    @property
    def costing(self):
        for i, v in enumerate(self.numbers):
            for i2, v2 in enumerate(self.numbers):
                if i != i2:
                    if v + v2 == self.target:
                        return i, i2
        '''
        raise error if answer not in numbers
        '''
        return {'error': 'no data satisfying the conditions'}
