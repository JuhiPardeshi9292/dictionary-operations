def get_first_name(uid: str, c_fn_map: dict[str, str], u_c_map: dict[str, str]) -> str:
    can_uid = u_c_map[uid]
    first_name = c_fn_map[can_uid]
    return first_name

def get_last_name(uid: str, c_ln_map: dict[str, str], u_c_map: dict[str, str]) -> str:
    can_uid = u_c_map[uid]
    last_name = c_ln_map[can_uid]
    return last_name

def get_rank(uid: str, c_rank_map: dict[str, int], u_c_map: dict[str, str]) -> int:
    can_uid = u_c_map[uid]
    rank = c_rank_map[can_uid]
    return rank

def del_money(uid: str, rank_money_map: dict[int, int], c_rank_map: dict[str, int], u_c_map: dict[str, str]) -> dict[int, int]:
    rank = get_rank(uid, c_rank_map, u_c_map)
    del rank_money_map[rank]
    return rank_money_map


def update_money(uid: str, new_money: int, rank_money_map: dict[int, int], c_rank_map: dict[str, int],
                 u_c_map: dict[str, str]) -> int:
    rank = get_rank(uid, c_rank_map, u_c_map)
    rank_money_map[rank] = new_money
    money = rank_money_map[rank]
    return money