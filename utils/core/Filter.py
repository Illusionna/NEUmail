'''
# System --> Windows & Python3.10.0
# File ----> Filter.py
# Author --> Illusionna
# Create --> 2024/03/24 22:23:35
'''
# -*- Encoding: UTF-8 -*-


import sys
from abc import (ABC, abstractmethod)
from email.utils import (parsedate_tz, mktime_tz)
from datetime import (datetime, timezone, timedelta)


class JUDGE(ABC):
    """条件判断抽象类, 用于被继承派生类.

    Args:
        ABC (_type_): 抽象类祖师爷 🤣👉🤡.
    """

    @abstractmethod
    def Judge(self) -> bool:
        """抽象纯虚函数: 判断附件信息是否符合条件.

        Returns:
            bool: 派生类重写判断条件, 返回布尔型.
        """
        pass


class SUBJECT(JUDGE):
    """主题继承条件判断抽象类.

    Args:
        JUDGE (_type_): 条件判断抽象类.
    """

    def __init__(self, filterSubject:set[str], subject:str) -> None:
        """初始化构造函数.

        Args:
            filterSubject (set[str]): 希望过滤的主题集合.
            subject (str): 邮件的主题.
        """
        self.filterSubject = filterSubject
        self.subject = subject
        
    def Judge(self) -> bool:
        """重写公有成员函数: 判断主题是否符合筛选条件.

        Returns:
            bool: 布尔型是或否.
        """
        if len(self.filterSubject) == 0:
            return False
        else:
            self.subject = ''.join(filter(lambda x: x.strip(), self.subject))
            if any(
                (word.strip() and (word.strip().lower() in self.subject.lower()))
                for word in self.filterSubject
            ):
                return True
            else:
                return False


class ADDRESS(JUDGE):
    """邮件地址继承条件判断抽象类.

    Args:
        JUDGE (_type_): 条件判断抽象类.
    """
    
    def __init__(self, filterEmailAddress:set[str], emailAddress:str) -> None:
        """初始化构造函数.

        Args:
            filterEmailAddress (set[str]): 希望过滤的邮件地址.
            emailAddress (str): 邮件的地址.
        """
        self.filterEmailAddress = filterEmailAddress
        self.emailAddress = emailAddress
        
    def Judge(self) -> bool:
        """重写公有成员函数: 判断邮件地址是否符合筛选条件.

        Returns:
            bool: 布尔型是或否.
        """
        if len(self.filterEmailAddress) == 0:
            return False
        else:
            if any(
                word.lower() == self.emailAddress.lower()
                for word in self.filterEmailAddress
            ):
                return True
            else:
                return False


class NICKNAME(JUDGE):
    """昵称继承条件判断抽象类.

    Args:
        JUDGE (_type_): 条件判断抽象类.
    """
    
    def __init__(self, filterNickname:set[str], nickname:str) -> None:
        """初始化构造函数.
        
        Args:
            filterNickname (set[str]): 希望过滤的昵称.
            nickname (str): 邮件的昵称.
        """
        self.filterNickname = filterNickname
        self.nickname = nickname

    def Judge(self) -> bool:
        """重写公有成员函数: 判断昵称是否符合筛选条件.

        Returns:
            bool: 布尔型是或否.
        """
        if len(self.filterNickname) == 0:
            return False
        else:
            self.nickname = ''.join(filter(lambda x: x.strip(), self.nickname))
            if any(
                (word.strip() and (word.strip().lower() in self.nickname.lower()))
                for word in self.filterNickname
            ):
                return True
            else:
                return False


class DATE(JUDGE):
    """时间段继承条件判断抽象类.

    Args:
        JUDGE (_type_): 条件判断抽象类.
    """

    def __init__(self, timePeriodRange:list, timeZone:str, date:str) -> None:
        """初始化构造函数.

        Args:
            timePeriodRange (list): 希望保留的时间段.
            timeZone (str): 时区.
            date (str): 邮件的时间.
        """
        self.timePeriodRange = timePeriodRange
        self.date = date
        self.symbol: str = timeZone[0]
        if 1 <= int(timeZone[1:]) <= 12:
            self.timeZone = int(timeZone[1:])
        else:
            print(f'时区\033[33m GMT{timeZone} \033[0m超过合法范围, 已按照北京东八区重置.')
            self.timeZone = 8

    def Judge(self) -> bool:
        """重写公有成员函数: 判断时间段是否符合筛选条件.

        Returns:
            bool: 布尔型是或否.
        """
        if self.date == None:
            return False
        if len(self.timePeriodRange) == 2:
            if (len(self.timePeriodRange[0]) == 0) & (len(self.timePeriodRange[1]) == 0):
                DATE.__Exit(self.timePeriodRange)
            else:
                try:
                    if len(self.timePeriodRange[0]) == 0:
                        # 假设人能活一百岁.
                        self.startTime = datetime.strptime(
                            (datetime.now() - timedelta(days=36500)).strftime("%Y-%m-%d %H:%M:%S"),
                            '%Y-%m-%d %H:%M:%S'
                        )
                        self.endTime = datetime.strptime(self.timePeriodRange[1], '%Y-%m-%d %H:%M:%S')
                    elif len(self.timePeriodRange[1]) == 0:
                        self.startTime = datetime.strptime(self.timePeriodRange[0], '%Y-%m-%d %H:%M:%S')
                        self.endTime = datetime.strptime(
                            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            '%Y-%m-%d %H:%M:%S'
                        )
                    else:
                        self.startTime = datetime.strptime(self.timePeriodRange[0], '%Y-%m-%d %H:%M:%S')
                        self.endTime = datetime.strptime(self.timePeriodRange[1], '%Y-%m-%d %H:%M:%S')
                    try:
                        transformTime = datetime.fromtimestamp(
                            mktime_tz(parsedate_tz(self.date)),
                            tz = timezone(
                                timedelta(
                                    hours=(
                                        -self.timeZone if (self.symbol == '-') else self.timeZone
                                    )
                                )
                            )
                        ).strftime('%Y-%m-%d %H:%M:%S')
                        transformTime = datetime.strptime(transformTime, '%Y-%m-%d %H:%M:%S')
                    except:
                        # 如果再次异常, 那么不按照时间段过滤这份邮件算了, 也下载到本地吧 (*Φ皿Φ*).
                        try:
                            transformTime = datetime.strptime(
                                self.date, '%Y-%m-%d %H:%M:%S %z'
                            ).replace(tzinfo=None)
                        except:
                            return False
                    if self.endTime < self.startTime:
                        print(f'时间区间截止时间\033[31m {self.timePeriodRange[1]}\033[0m')
                        print(f'时间区间开始时间\033[31m {self.timePeriodRange[0]}\033[0m')
                        print('截止时间比开始时间早? 熵减过程? 你是认真的嘛?')
                        print('\n\033[31m按 Enter 键退出...\033[0m')
                        # input('\n按 Enter 键退出...')
                        sys.exit()
                    if self.startTime <= transformTime <= self.endTime:
                        return False
                    else:
                        return True
                except:
                    DATE.__Exit(self.timePeriodRange)
        else:
            DATE.__Exit(self.timePeriodRange)

    @staticmethod
    def __Exit(timePeriodRange:list) -> None:
        """静态私有函数: 打印并退出.
        """
        demoA = ['', '2024-3-12 00:00:00']
        demoB = ['2024-02-12 07:00:00', '']
        demoC = ['2024-02-12 07:00:00', '2024-3-12 00:00:00']
        print(f'希望保留附件的 timePeriodRange 时间段\033[31m {timePeriodRange} \033[0m格式错误.')
        print('参考如下格式设置时间:')
        print('\t如果想收取到 2024 年 3 月 12 日前的附件, 可以设置:')
        print(f'\t\t{demoA}')
        print('\t如果想从 2024 年 2 月 12 日上午七点开始收取, 可以设置:')
        print(f'\t\t{demoB}')
        print('\t如果想收取以上两个时间段的附件, 可以设置:')
        print(f'\t\t{demoC}')
        print('\n\033[31m按 Enter 键退出...\033[0m')
        # input('\n按 Enter 键退出...')
        sys.exit()


class FILTER:
    """过滤器类, 用于筛选过滤的附件.
    """

    def __init__(self) -> None:
        self.filter: list = []

    def AddFilter(self, judge:JUDGE) -> None:
        """公有成员函数: 增加过滤器.

        Args:
            judge (JUDGE): 传入过滤器判断类型对象.
        """
        self.filter.append(judge)

    def Filter(self) -> bool:
        """公有成员函数: 按照过滤器列表进行筛选过滤.

        Returns:
            bool: 返回某封邮箱附件是否需要过滤.
        """
        tmp: bool = False
        for condition in self.filter:
            if not condition.Judge():
                tmp = tmp | False
            else:
                tmp = tmp | True
        return tmp