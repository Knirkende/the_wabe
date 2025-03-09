from app.model.archetypes import DynamicEntity

class Tove(DynamicEntity):

    TOVE = 'Tove'
    __mapper_args__ = {'polymorphic_identity': TOVE}

    def __init__(self, **kwargs):
        super().__init__(entity_type=self.TOVE, **kwargs)

class Borogove(DynamicEntity):
    
    BOROGOVE = 'Borogove'
    __mapper_args__ = {'polymorphic_identity': BOROGOVE}

    def __init__(self, **kwargs):
        super().__init__(entity_type=self.BOROGOVE, **kwargs)