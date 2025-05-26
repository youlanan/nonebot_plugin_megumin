import datetime
from .config import plugin_config

class Limit:
    """
    限制计算模块
    触发、补魔次数是按玩家算
    推荐模式0下需要记录群聊id
    """

    _today: str = datetime.date.today().isoformat()
    _groups: set[str] = set()
    _players: dict[str, list[int, int]] = {}
    _max_cast: int = plugin_config.megumin_max_cast
    _max_recover: int = plugin_config.megumin_max_recover

    @classmethod
    def _get_today(cls) -> str:
        return datetime.date.today().isoformat()

    @classmethod
    def check_date(cls) -> None:
        now = cls._get_today()
        if now != cls._today:
            cls._today = now
            cls._groups.clear()
            cls._players.clear()

    @classmethod
    def allow_video(cls, groupid: str) -> bool:
        cls.check_date()
        if groupid in cls._groups:
            return False
        cls._groups.add(groupid)
        return True

    @classmethod
    def no_can_spells(cls, userid: str) -> bool:
        if cls._max_cast == 0:
            return False
        cls.check_date()
        player = cls._players.get(userid)
        if player is None:
            cls._players[userid] = [cls._max_recover, cls._max_cast - 1]
            return False
        if player[1] > 0:
            player[1] -= 1
            return False
        return True

    @classmethod
    def no_can_recover(cls, userid: str) -> bool:
        cls.check_date()
        player = cls._players.get(userid)
        new_max_recover = 1 if cls._max_recover == 0 else cls._max_recover
        if player is None:  # 不会有人在无限施法的情况下补魔吧
            cls._players[userid] = [new_max_recover, cls._max_cast]
            return False
        if player[0] > 0:
            player[0] -= 1
            player[1] += cls._max_cast  # 不会有人在施法没用完前补魔吧
            return False
        return True
