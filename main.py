from dictionary import get_first_name, get_rank, del_user, get_money, update_money, inc_amt, dec_amt, del_money, del_rank
from functions import calc_func, calc_sum

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
    print(calc_func(2, 3))
    print(calc_sum(2, 3))
    print(get_first_name("jp", c_fn_map, u_c_map))
    print(get_rank("jp", c_rank_map, u_c_map))
    print(del_user("jp", u_c_map, c_fn_map, c_ln_map, c_rank_map))
    print(get_money("ss", rank_money_map, c_rank_map, u_c_map))
    print(update_money(8, 25000, rank_money_map, c_rank_map))
    print(inc_amt(8, 5000, rank_money_map))
    print(dec_amt(8, 2000, rank_money_map))
    print(del_user("as", u_c_map, c_fn_map, c_ln_map, c_rank_map))
    print(u_c_map)
    print(c_fn_map)
    print(c_ln_map)
    print(c_rank_map)
    print(del_money(20, rank_money_map))
    print(del_rank(8, c_rank_map, rank_money_map))
