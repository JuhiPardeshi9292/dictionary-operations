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

