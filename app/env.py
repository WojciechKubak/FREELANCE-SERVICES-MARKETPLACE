def env_to_bool(env_var: str) -> bool:
    return str(env_var).upper() in ["TRUE", "1", "YES"]


def env_to_int(env_var: str) -> int:
    return int(env_var)


def env_to_list(env_var: str, sep: str = ",") -> list[str]:
    return str(env_var).split(sep)
