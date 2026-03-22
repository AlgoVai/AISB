from AIWGS.models import Institute

class InstituteService:
    def __init__(self):
        pass

    def Get(self):
        data = Institute.objects.all()
        return data
    def createInstitute(self,data):
        result = Institute.objects.create(**data)
        return result
    