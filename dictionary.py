def get_first_name(uid: str, c_fn_map: dict[str, str], u_c_map: dict[str, str]) -> str:
    """
    Get the first name of a user.

    :param uid: Human-readable user ID.
    :param c_fn_map: Mapping of canonical user ID to first name.
    :param u_c_map: Mapping of human-readable user ID to canonical user ID.
    :return: The user's first name.
    """
    can_uid = u_c_map[uid]
    first_name = c_fn_map[can_uid]
    return first_name

def get_last_name(uid: str, c_ln_map: dict[str, str], u_c_map: dict[str, str]) -> str:
    """
    Get the last name of a user.

    :param uid: Human-readable user ID.
    :param c_ln_map: Mapping of canonical user ID to last name.
    :param u_c_map: Mapping of human-readable user ID to canonical user ID.
    :return: The user's last name.
    """

    can_uid = u_c_map[uid]
    last_name = c_ln_map[can_uid]
    return last_name

def get_rank(uid: str, c_rank_map: dict[str, int], u_c_map: dict[str, str]) -> int:
    """
    Get the rank of a user.

    :param uid: Human-readable user ID.
    :param c_rank_map: Mapping of canonical user ID to rank.
    :param u_c_map: Mapping of human-readable user ID to canonical user ID.
    :return:  returns user's rank.
    """
    can_uid = u_c_map[uid]
    rank = c_rank_map[can_uid]
    return rank

def update_money(rank: int, new_money: int, rank_money_map: dict[int, int], c_rank_map: dict[str, int],
                 ) -> int:
    """
    Update the money associated with a rank.

    :param rank: Rank whose money needs to be updated.
    :param new_money: New money amount.
    :param rank_money_map: Mapping of rank to money.
    :param c_rank_map: Mapping of canonical user ID to rank.
    :return: The previous money amount.
    """
    prev_money = rank_money_map[rank]
    rank_money_map[rank] = new_money
    return prev_money


def update_first_name(uid: str, new_first_name: str, c_fn_map: dict[str, str], u_c_map: dict[str, str]) -> str:
    """
    Update the first name of a user.

    :param uid: Human-readable user ID.
    :param new_first_name: New first name to assign.
    :param c_fn_map: Mapping of canonical user ID to first name.
    :param u_c_map: Mapping of human-readable user ID to canonical user ID.
    :return: The updated first name.
    """
    first_name = get_first_name(uid, c_fn_map, u_c_map)
    can_uid = u_c_map[uid]
    c_fn_map[can_uid] = new_first_name
    return first_name

def update_last_name(uid: str, new_last_name: str, c_fn_map: dict[str, str], u_c_map: dict[str, str]) -> str:
    """
    Update the last name of a user.

    :param uid: Human-readable user ID.
    :param new_last_name: New last name to assign.
    :param c_fn_map: Mapping of canonical user ID to last name.
    :param u_c_map: Mapping of human-readable user ID to canonical user ID.
    :return: The updated last name.
    """
    last_name = get_first_name(uid, c_fn_map, u_c_map)
    can_uid = u_c_map[uid]
    c_fn_map[can_uid] = new_last_name
    return last_name

def update_rank(uid: str, new_rank: int, c_rank_map: dict[str, int], u_c_map: dict[str, str]) -> int:
    """
    Update the rank of a user.

    :param uid: Human-readable user ID.
    :param new_rank: New rank to assign.
    :param c_rank_map: Mapping of canonical user ID to rank.
    :param u_c_map: Mapping of human-readable user ID to canonical user ID.
    :return: The updated rank.
    """
    prev_rank = get_rank(uid, c_rank_map, u_c_map)
    can_uid = u_c_map[uid]
    c_rank_map[can_uid] = new_rank
    return prev_rank

def get_money(uid: str, rank_money_map: dict[int, int], c_rank_map: dict[str, int], u_c_map: dict[str, str]) -> int:
    """
    Get the money associated with a user's rank.

    :param uid: Human-readable user ID.
    :param rank_money_map: Mapping of rank to money.
    :param c_rank_map: Mapping of canonical user ID to rank.
    :param u_c_map: Mapping of human-readable user ID to canonical user ID.
    :return: The money associated with the user's rank.
    """
    rank = get_rank(uid, c_rank_map, u_c_map)
    money = rank_money_map[rank]
    return money

def inc_amt(rank: int, inc_amt: int, rank_money_map: dict[int, int]) -> int:
    """
    Increase the money associated with a rank.

    :param rank: Rank whose money needs to be increased.
    :param inc_amt: Amount to increase.
    :param rank_money_map: Mapping of rank to money.
    :return: The updated money amount.
    """
    prev_money = rank_money_map[rank]
    new_money = prev_money + inc_amt
    rank_money_map[rank] = new_money
    return new_money

def dec_amt(rank: int, dec_amt: int, rank_money_map: dict[int, int]) -> int:
    """
    Decrease the money associated with a rank.

    :param rank: Rank whose money needs to be decreased.
    :param dec_amt: Amount to decrease.
    :param rank_money_map: Mapping of rank to money.
    :return: The updated money amount.
    """
    prev_amt = inc_amt(rank, -dec_amt, rank_money_map)
    return prev_amt

def del_user(uid: str, u_c_map: dict[str, str], c_fn_map: dict[str, str], c_ln_map: dict[str, str], c_rank_map: dict[str, int]) -> \
tuple[str, str, str, int]:
    can_uid = u_c_map[uid]
    prev_rank = c_rank_map[can_uid]
    prev_fn = c_fn_map[can_uid]
    prev_ln = c_ln_map[can_uid]
    del u_c_map[uid]
    del c_fn_map[can_uid]
    del c_ln_map[can_uid]
    del c_rank_map[can_uid]
    return can_uid, prev_fn, prev_ln, prev_rank