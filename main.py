from src.dict_operations.dictionary import (
    get_first_name,
    get_last_name,
    get_rank,
    update_money,
    update_first_name,
    update_last_name,
    update_rank,
    get_money,
    inc_amt,
    dec_amt,
    del_user,
    del_money,
    del_rank,
    del_money_unsafe,
    del_money_safe,
)
from src.dict_operations.functions import calc_func, calc_sum

u_c_map: dict[str, str] = {
    "ss": "jsNczheCKMY",
    "jp": "O2zPUceb_ws",
    "as": "mtblw50vlyg",
}

c_fn_map: dict[str, str] = {
    "jsNczheCKMY": "suhas",
    "O2zPUceb_ws": "juhi",
    "mtblw50vlyg": "ankit",
}

c_ln_map: dict[str, str] = {
    "jsNczheCKMY": "srivastava",
    "O2zPUceb_ws": "pardeshi",
    "mtblw50vlyg": "singh",
}

c_rank_map: dict[str, int] = {
    "jsNczheCKMY": 8,
    "O2zPUceb_ws": 10,
    "mtblw50vlyg": 2,
}

rank_money_map: dict[int, int] = {
    8: 20_000,
    10: 10_000,
    2: 8_000,
    20: 2_000,
}

if __name__ == '__main__':
    calc_result = calc_func(2,3)
    sum_result = calc_sum(2,3)

    first_name = get_first_name("jp", c_fn_map, u_c_map)
    last_name = get_last_name("jp", c_ln_map, u_c_map)
    rank = get_rank("jp", c_rank_map, u_c_map)
    updated_money = update_money(8, 25000, rank_money_map, c_rank_map)
    previous_first_name = update_first_name("jp", "juhiP", c_fn_map, u_c_map)
    previous_last_name = update_last_name("jp", "pardeshi", c_ln_map, u_c_map)
    previous_rank = update_rank("jp", 10, c_rank_map, u_c_map)
    money = get_money("ss", rank_money_map, c_rank_map, u_c_map)
    increased_money = inc_amt(8, 5000, rank_money_map)
    decreased_money = dec_amt(8, 2000, rank_money_map)
    deleted_user = del_user("as", u_c_map, c_fn_map, c_ln_map, c_rank_map)
    deleted_money = del_money(2000, rank_money_map)
    deleted_rank = del_rank(8, c_rank_map, rank_money_map)
    deleted_money_unsafe = del_money_unsafe(2000, rank_money_map)
    deleted_money_safe = del_money_safe(8000, rank_money_map, c_rank_map)
