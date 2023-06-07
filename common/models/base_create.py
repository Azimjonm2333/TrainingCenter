from .create_update_time import CreateUpdatetimeModel

class BaseModelCreate(CreateUpdatetimeModel):
    """
    Abstact Base model with uuid pk and create and update time
    """

    class Meta:
        abstract = True
