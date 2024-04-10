'''
# System --> Windows & Python3.10.0
# File ----> interface.py
# Author --> Illusionna
# Create --> 2024/03/21 23:07:36
'''
# -*- Encoding: UTF-8 -*-


import winreg
from abc import (ABC, abstractmethod)


class SCAN_ABSTRACT(ABC):
    """扫描抽象类.

    Args:
        ABC (_type_): 扫描 Web 前端所需要的 static 静态文件内容完整性.
    """

    @abstractmethod
    def CalculateFileHash(dir:str) -> str:
        """计算文件的加密哈希散列值, 用于对比文件一致性.

        Args:
            dir (str): 文件路径.

        Returns:
            str: 哈希字符串.
        """
        pass
    
    @abstractmethod
    def Compare() -> bool:
        """对比所有 static 静态文件内容与标准值一致.

        Returns:
            bool: 若一致则跳过, 若不一致则从公网下载标准文件.
        """
        pass

    @abstractmethod
    def Download() -> None:
        """调用 scan.exe 程序下载公网文件.
        """
        pass


class PROOFREAD_ABSTRACT(ABC):
    """校对抽象类.

    Args:
        ABC (_type_): 校对 config.json 配置文件的初始化设置.
    """
    
    @abstractmethod
    def CreateJson() -> None:
        """创建初始化的 config.json 文件.
        """
        pass
    
    @abstractmethod
    def LoadJson() -> dict:
        """加载 config.json 文件中的数据.

        Returns:
            dict: 键值对.
        """
        pass
    
    @abstractmethod
    def WriteJson() -> None:
        """数据写入 config.json 文件中.
        """
        pass
    
    @abstractmethod
    def SkipJudge() -> None:
        """校对 skip 字段, 判断是否跳过新手引导教程.
        """
        pass

    @staticmethod
    def GetDesktopPath() -> str | None:
        """获取桌面路径.

        Returns:
            str: 可能的桌面路径.
        """
        try:
            tmp: 'function' = winreg.OpenKey(
                key = winreg.HKEY_CURRENT_USER,
                sub_key = r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            )
            desktop = winreg.QueryValueEx(tmp, 'Desktop')[0]
            return desktop
        except:
            return None


class GUIDE_ABSTRACT(ABC):
    """引导抽象类.

    Args:
        ABC (_type_): 用于指导新手完成 config.json 文件配置的前端.
    """

    @abstractmethod
    def Start() -> None:
        """启动 Web 引导界面进程.
        """
        pass


class USAGE_ABSTRACT(ABC):
    """使用抽象类.

    Args:
        ABC (_type_): 用于邮箱附件下载的前端.
    """

    @abstractmethod
    def Activate() -> None:
        """激活 Web 下载前端进程.
        """
        pass