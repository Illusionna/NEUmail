'''
# System --> Windows & Python3.10.0
# File ----> Factory.py
# Author --> Illusionna
# Create --> 2024/03/24 22:17:58
'''
# -*- Encoding: UTF-8 -*-


import os
import re
import hashlib
from utils.inherit import SCAN
from abc import (ABCMeta, abstractmethod)


class SAVE(metaclass=ABCMeta):
    """附件保存纯虚类, 继承 type 元类, 提供给派生子类实现父类指定的规范化功能.

    Args:
        metaclass (_type_, optional): type 元类.
    """

    SUBJECT_MAX_LENGTH = 72

    def __init__(self, dir:str, fileName:str, data:bytes) -> None:
        self.dir = dir
        self.fileName = fileName
        self.data = data
 
    def SaveAttachments(self, path:str, isOverwrite:bool) -> None:
        """公有成员函数: 根据要求把附件写入本次磁盘.

        Args:
            path (str): 路径.
            isOverwrite (bool): 是否覆盖重名文件.
        """
        if not os.path.exists(path):
            os.makedirs(path)
        self.fileName: str = SAVE.SameFileNameHashCheckAndUpdate(
            path = path,
            isOverwrite = isOverwrite,
            fileName = self.fileName,
            data = self.data
        )
        if self.fileName != None:
            with open(os.path.join(path, self.fileName), 'wb') as f:
                f.write(self.data)

    @staticmethod
    def SameFileNameHashCheckAndUpdate(
        path:str,
        isOverwrite:bool,
        fileName:str,
        data:bytes    
    ) -> list[str]:
        """静态公有函数: 相同文件路径(即文件名)的哈希 SHA-256 散列检查并更新.

        Args:
            path (str): 保存在本地磁盘的附件父根目录.
            isOverwrite (bool): 是否覆盖同名且哈希 SHA-256 散列不同的文件.
            fileName (str): 来自邮箱的附件文件名.
            data (bytes): 附件字节流.

        Returns:
            str | None: 需要更新的递归子文件路径.
        """
        filesDir: list[str] = [SCAN.SlashBackslash(i) for i in SCAN.RecursiveGetFiles(path)]
        filesHash: dict = dict(
            zip(
                [os.path.basename(i) for i in filesDir],
                [SCAN.CalculateFileHash(i) for i in filesDir]
            )
        )
        if fileName in filesHash.keys():
            if isOverwrite:
                # 如果次目录下有重名文件且哈希散列不同.
                #   - 则返回文件名被重写数据流.
                #   - 否则散列相同返回空指针跳过.
                # 这么做的目的在于如果一个人给我发相同附件(指代内容相同).
                # 我不必在覆盖的前提下真的去再次 IO 写入该相同附件.
                # 我只会在覆盖的前提下, 同名文件但内容不同才会 IO 写入.
                tmp: str = hashlib.sha256(data).hexdigest()
                if filesHash[fileName] != tmp:
                    return fileName
                else:
                    return None
            else:
                fileNumber = 2
                (pureName, extension) = os.path.splitext(fileName)
                existFiles: list = os.listdir(path)
                while fileName in existFiles:
                    fileName = pureName + f'({str(fileNumber)})' + extension
                    fileNumber = -~fileNumber
                return fileName
        else:
            return fileName

    @staticmethod
    def GetNormativeFolder(dir:str) -> str:
        """获取规范化的文件夹名称.

        Args:
            dir (str): 目录名.

        Returns:
            str: 规范化的目录名.
        """
        try:
            name = re.sub('[*"/:?|<>\n]', '', dir, 0)
            name = name[0:min(SAVE.SUBJECT_MAX_LENGTH, len(name))].strip()
            return name
        except:
            return '正则化匹配异常@单独文件夹'

    @abstractmethod
    def Save(self) -> None:
        """抽象纯虚函数: 保存附件.
        """
        pass


class ALL_ATTACHMENTS_IN_ONE_FOLDER(SAVE):
    """继承保存纯虚类, 所有附件一个文件夹类.

    Args:
        SAVE (_type_): 保存纯虚类.
    """

    def __init__(self, dir:str, fileName:str, data:bytes, isOverwrite:bool) -> None:
        super().__init__(dir, fileName, data)
        self.isOverwrite = isOverwrite

    def Save(self) -> None:
        """重写公有函数: 保存附件.
        """
        self.SaveAttachments(self.dir, self.isOverwrite)


class ONE_FOLDER_PER_EMAIL_ADDRESS(SAVE):
    """继承保存纯虚类, 每个邮箱一个文件夹类.

    Args:
        SAVE (_type_): 保存纯虚类.
    """

    def __init__(
        self,
        dir:str,
        fileName:str,
        data:bytes,
        isOverwrite:bool,
        emailAddress:str
    ) -> None:
        super().__init__(dir, fileName, data)
        self.emailAddress = SAVE.GetNormativeFolder(emailAddress)
        self.isOverwrite = isOverwrite

    def Save(self) -> None:
        """重写公有函数: 保存附件.
        """
        self.SaveAttachments(os.path.join(self.dir, self.emailAddress), self.isOverwrite)


class ONE_FOLDER_PER_SUBJECT(SAVE):
    """继承保存纯虚类, 每个主题一个文件夹类.

    Args:
        SAVE (_type_): 保存纯虚类.
    """

    def __init__(self, dir:str, fileName:str, data:bytes, isOverwrite:bool, subject:str) -> None:
        super().__init__(dir, fileName, data)
        self.subject = SAVE.GetNormativeFolder(subject)
        self.isOverwrite = isOverwrite

    def Save(self) -> None:
        """重写公有函数: 保存附件.
        """
        self.SaveAttachments(os.path.join(self.dir, self.subject), self.isOverwrite)


class ONE_FOLDER_PER_NICKNAME(SAVE):
    """继承保存纯虚类, 每个昵称一个文件夹类.

    Args:
        SAVE (_type_): 保存纯虚类.
    """

    def __init__(self, dir:str, fileName:str, data:bytes, isOverwrite:bool, nickname:str) -> None:
        super().__init__(dir, fileName, data)
        self.nickname = SAVE.GetNormativeFolder(nickname)
        self.isOverwrite = isOverwrite

    def Save(self) -> None:
        """重写公有函数: 保存附件.
        """
        self.SaveAttachments(os.path.join(self.dir, self.nickname), self.isOverwrite)


class ONE_FOLDER_PER_SUBJECT_MULTIPLE_EMAIL_ADDRESS(SAVE):
    """继承保存纯虚类, 每个主题多个邮箱一个文件夹类.

    Args:
        SAVE (_type_): 保存纯虚类.
    """

    def __init__(
        self,
        dir:str,
        fileName:str,
        data:bytes,
        isOverwrite:str,
        emailAddress:str,
        subject:str
    ) -> None:
        super().__init__(dir, fileName, data)
        self.emailAddress = SAVE.GetNormativeFolder(emailAddress)
        self.subject = SAVE.GetNormativeFolder(subject)
        self.isOverwrite = isOverwrite

    def Save(self) -> None:
        """重写公有函数: 保存附件.
        """
        self.SaveAttachments(
            path = os.path.join(self.dir, self.subject, self.emailAddress),
            isOverwrite = self.isOverwrite
        )


class FACTORY:
    """附件保存格式类.
    """

    def __init__(self, attachmentSaveMode:str, isOverwrite:bool) -> None:
        self.attachmentSaveMode = attachmentSaveMode
        self.isOverwrite = isOverwrite

    def __call__(self, dir:str, fileName:str, data:bytes, container:object) -> None:
        """重写类调用函数.

        Args:
            dir (str): 附件保存绝对路径父目录.
            fileName (str): 相对路径文件名.
            data (bytes): 文件的数据字节流.
            container (object): 容器类对象.
        """
        mode = {
            '所有附件一个文件夹': ALL_ATTACHMENTS_IN_ONE_FOLDER(
                dir=dir, fileName=fileName, data=data, isOverwrite=self.isOverwrite
            ),
            '每个邮箱一个文件夹': ONE_FOLDER_PER_EMAIL_ADDRESS(
                dir=dir, fileName=fileName, data=data, isOverwrite=self.isOverwrite, emailAddress=container.emailAddress
            ),
            '每个主题一个文件夹': ONE_FOLDER_PER_SUBJECT(
                dir=dir, fileName=fileName, data=data, isOverwrite=self.isOverwrite, subject=container.subject),
            '每个昵称一个文件夹': ONE_FOLDER_PER_NICKNAME(
                dir=dir, fileName=fileName, data=data, isOverwrite=self.isOverwrite, nickname=container.nickname
            ),
            '每个主题多个邮箱一个文件夹': ONE_FOLDER_PER_SUBJECT_MULTIPLE_EMAIL_ADDRESS(
                dir=dir, fileName=fileName, data=data, isOverwrite=self.isOverwrite, emailAddress=container.emailAddress, subject=container.subject
            )
        }
        return mode[self.attachmentSaveMode]