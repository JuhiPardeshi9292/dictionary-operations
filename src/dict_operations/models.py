class DeletedUser:
    def __init__(self, can_uid: str, first_name: str, last_name: str, rank: int):
        self.can_uid = can_uid
        self.first_name = first_name
        self.last_name = last_name
        self.rank = rank

class DeletedRank:
    def __init__(self, deleted: bool, rank: int):
        self.deleted = deleted
        self.rank = rank

class DeletedMoney:
    def __init__(self, deleted: bool, money: int):
        self.deleted = deleted
        self.money = money