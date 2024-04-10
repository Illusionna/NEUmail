'''
# System --> Windows & Python3.10.0
# File ----> EmailDownload.py
# Author --> Illusionna
# Create --> 2024/03/22 12:13:47
'''
# -*- Encoding: UTF-8 -*-


import os
import re
import sys
import poplib
import imaplib
from typing import Literal
from datetime import datetime
from utils.core.Filter import *
from alive_progress import alive_bar
from abc import (ABC, abstractmethod)
from utils.core.Tool import TRANSFORM
from utils.core.Factory import FACTORY
from utils.inherit import (SCAN, PROOFREAD_ABSTRACT)


class PROTOCOL(ABC):
    """协议抽象类.

    Args:
        ABC (_type_): 提供给 POP 和 IMAP 继承.
    """

    @abstractmethod
    def ConnectServer() -> None:
        """抽象纯虚函数: 连接服务器.
        """
        pass

    @abstractmethod
    def ConnectEmail() -> None:
        """抽象纯虚函数: 登录服务器上的邮箱.
        """
        pass

    @abstractmethod
    def Disconnect() -> None:
        """抽象纯虚函数: 断开服务器连接.
        """
        pass

    @abstractmethod
    def GetEmailStatus() -> tuple:
        """抽象纯虚函数: 获得邮件状态信息.

        Returns:
            tuple: 元组第一个数是一共 X 封邮件, 第二个数是一共占 X 的磁盘空间, 单位字节.
        """
        pass

    @abstractmethod
    def GetEmailList() -> list[list]:
        """抽象纯虚函数: 获得邮件列表.

        Returns:
            list[list]: 嵌套列表, 子列表第一个元素是邮件编号, 第二个元素是邮件占用大小.
        """
        pass

    @abstractmethod
    def GetEmailHeaderBytesStream(idx:str) -> bytes:
        """抽象纯虚函数: 获取邮件头部字节流, 为了优先快速遍历.

        Args:
            idx (str): 符串形式的邮件编号.

        Returns:
            bytes: 头字节(流).
        """
        pass

    @abstractmethod
    def GetEmailFullBytesStream(idx:str) -> bytes:
        """抽象纯虚函数: 获取邮件全字节流, 为了下载附件.

        Args:
            idx (str): 字符串形式的邮件编号.

        Returns:
            bytes: 全字节(流).
        """
        pass


class POP(PROTOCOL):
    """POP3 邮局继承协议类, 速度更快, 精度更低.
    """

    SKIP = False

    def __init__(
        self,
        emailAddress:str,
        serverAddress:str,
        protocolPassword:str
    ) -> None:
        """
        初始化构造函数: MAXLINE 取 2048 长度.
        """
        self.emailAddress = emailAddress
        self.serverAddress = serverAddress
        self.protocolPassword = protocolPassword
        # ---------------------------------------------------------------------
        poplib._MAXLINE = 2048
        '''
        这是大佬的原话: ``This is to prevent reading arbitrary length lines. RFC 1939 limits POP3 line length to 512 characters, including CRLF. We have selected 2048 just to be on the safe side''.
        参考 RFC 邮局协议话题: https://bugs.python.org/issue23906
        '''
        # ---------------------------------------------------------------------
        self.ConnectServer()
        if not POP.SKIP:
            self.ConnectEmail()
        
    def ConnectServer(self) -> None:
        """重写公有成员函数: 尝试连接到主机服务器.
        """
        try:
            self.connection = poplib.POP3_SSL(self.serverAddress)
            self.connection.set_debuglevel(False)
            print(self.connection.getwelcome().decode())
        except:
            print(f'POP 服务器\033[31m {self.serverAddress} \033[0m地址不对吧? 或者断网了?')
            print('要不要再看看文档, 天资聪颖的您一看就懂.')
            print('\033[32mhttps://Illusionna.vercel.app\033[0m')
            sys.exit()
            self.connection = None
            # sys.exit()
            POP.SKIP = True
            self.Disconnect()

    def ConnectEmail(self) -> None:
        """重写公有成员函数: 尝试连接到对应的邮箱.
        """
        self.connection.user(self.emailAddress)
        try:
            self.connection.pass_(self.protocolPassword)
            print('\n服务器邮箱\033[32m登录成功\033[0m, 开始下载附件...')
        except:
            self.Disconnect()
            print(f'\n服务器的邮箱\033[31m登陆失败\033[0m, 确保邮箱\033[33m {self.emailAddress} \033[0m已开启 POP3 服务\n检查 {self.emailAddress} 邮箱或\033[33m {self.protocolPassword} \033[0m协议密码是否正确\n或者服务器地址和邮箱地址是否对应\n指导文档:\033[32m https://Illusionna.vercel.app\033[0m')
            # input('\n按 Enter 键退出...')
            sys.exit()

    def Disconnect(self) -> None:
        """重写公有成员函数: 正常关闭或者出现异常时, 断开连接以释放资源.
        """
        if self.connection is None:
            try:
                1 / 0
            except:
                print(f'POP 服务器\033[31m {self.serverAddress} \033[0m地址不对吧? 或者断网了?')
                print('要不要再看看文档, 天资聪颖的您一看就懂.')
                print('\033[32mhttps://Illusionna.vercel.app\033[0m')
                # input('\n按 Enter 键退出...')
                sys.exit()
        else:
            try:
                self.connection.close()
            except:
                print('服务器断开连接时发生错误, 没事, 这是网络层的问题.')
                # input('\n按 Enter 键退出...')
                sys.exit()
    
    def GetEmailStatus(self) -> tuple:
        """重写公有成员函数: 返回邮箱状态信息.

        Returns:
            tuple: 元组第一个数是一共 X 封邮件, 第二个数是一共占 X 的磁盘空间, 单位字节.
        """
        return self.connection.stat()

    def GetEmailList(self) -> list[list]:
        """重写公有成员函数: 获取邮箱的全部首字段信息.

        Returns:
            list[list]: 返回全部邮件头字段列表.
        """
        (__, mailList, __) = self.connection.list()
        return [
            [i.split()[0].decode(), int(i.split()[-1].decode())]
            for i in reversed(mailList)
        ]
        
    def GetEmailHeaderBytesStream(self, idx:str) -> bytes:
        """重写公有成员函数: 获取邮件头部字节流, 为了优先快速遍历.

        Args:
            idx (str): 字符串形式的邮件编号.

        Returns:
            bytes: 头字节(流).
        """
        (__, bytesStream, __) = self.connection.top(idx, 120)
        try:
            mailHeaderEnd: int = bytesStream.index(b'')
        except:
            mailHeaderEnd: int = len(bytesStream)
        return b'\n'.join(bytesStream[:mailHeaderEnd])

    def GetEmailFullBytesStream(self, idx:str) -> bytes:
        """重写公有成员函数: 获取邮件全字节流, 为了下载附件.

        Args:
            idx (str): 字符串形式的邮件编号.

        Returns:
            bytes: 全字节(流).
        """
        (__, bytesStream, __) = self.connection.retr(idx)
        return b'\n'.join(bytesStream)


class IMAP(PROTOCOL):
    """IMAP 交互邮件访问继承协议类, 通过调试, 貌似 IMAP4 兼容 POP3, 精度更高, 速度慢.
    """
    
    SKIP = False

    def __init__(
        self,
        emailAddress:str,
        serverAddress:str,
        protocolPassword:str    
    ) -> None:
        """
        初始化构造函数.
        """
        self.emailAddress = emailAddress
        self.serverAddress = serverAddress
        self.protocolPassword = protocolPassword
        self.ConnectServer()
        if not IMAP.SKIP:
            self.ConnectEmail()
        
    def ConnectServer(self) -> None:
        """重写公有成员函数: 尝试连接到主机服务器.
        """
        try:
            self.connection = imaplib.IMAP4_SSL(self.serverAddress)
            print(f'+OK IMAP4 ready 服务器\033[32m {self.serverAddress} \033[0m连接成功.')
        except:
            print(f'IMAP 服务器\033[31m {self.serverAddress} \033[0m地址不对吧? 或者断网了?')
            print('要不要再看看文档, 天资聪颖的您一看就懂.')
            print('\033[32mhttps://Illusionna.vercel.app\033[0m')
            # input('\n按 Enter 键退出...')
            sys.exit()
            self.connection = None
            IMAP.SKIP = True
            IMAP.Disconnect(self)

    def ConnectEmail(self) -> None:
        """重写公有成员函数: 尝试连接到对应的邮箱.
        """
        try:
            self.connection.login(self.emailAddress, self.protocolPassword)
            print('\n服务器邮箱\033[32m登录成功\033[0m, 开始下载附件...')
        except:
            print(f'\n服务器的邮箱\033[31m登陆失败\033[0m, 确保邮箱\033[33m {self.emailAddress} \033[0m已开启 IMAP 服务\n检查 {self.emailAddress} 邮箱或\033[33m {self.protocolPassword} \033[0m协议密码是否正确\n或者服务器地址和邮箱地址是否对应\n指导文档:\033[32m https://Illusionna.vercel.app\033[0m')
            # input('\n按 Enter 键退出...')
            sys.exit()

    def Disconnect(self) -> None:
        """重写公有成员函数: 正常关闭或者出现异常时, 断开连接以释放资源.
        """
        if self.connection is None:
            try:
                1 / 0
            except:
                print(f'IMAP 服务器\033[31m {self.serverAddress} \033[0m地址不对吧? 或者断网了?')
                print('要不要再看看文档, 天资聪颖的您一看就懂.')
                print('\033[32mhttps://Illusionna.vercel.app\033[0m')
                # input('\n按 Enter 键退出...')
                sys.exit()
        else:
            try:
                self.connection.close()
            except:
                print('服务器断开连接时发生错误, 没事, 这是网络层的问题.')
                # input('\n按 Enter 键退出...')
                sys.exit()
    
    def GetEmailStatus(self) -> tuple:
        """重写公有成员函数: 返回邮箱状态信息.

        Returns:
            tuple: 元组第一个数是一共 X 封邮件, 第二个数固定为 None 磁盘占用空间大小.
        """
        (__, msg) = self.connection.status('INBOX', '(MESSAGES)')
        quantity = int(re.findall(r'\d+', msg[0].decode())[0])
        return (quantity, None)
    
    def GetEmailList(self) -> list[list]:
        """重写公有成员函数: 获取邮箱的全部首字段信息.

        Returns:
            list[list]: 返回全部邮件头字段列表.
        """
        try:
            # 优先尝试直接选择, 如果不行再一个个判断.
            self.connection.select()
            (__, mailList) = self.connection.search(None, '(ALL)')
            return [[x.decode(), None] for x in reversed(mailList[0].split())]
        except:
            if self.serverAddress == 'imap.163.com' or 'pop.163.com':
                # -------------------------------------
                # 测试网页 163 邮箱 AUTH ID 字段.
                # -------------------------------------
                # imaplib.Commands['ID'] = ('AUTH')
                # args = ('name', 'XXXX', 'contact', 'XXXX@163.com', 'version', '1.0.0', 'vendor', 'myclient')
                # print(self.connection._simple_command('ID', '("' + '" "'.join(args) + '")'))
                # (tmpA, tmpB) = self.connection._simple_command('ID', '("' + '" "'.join(args) + '")')
                # print(self.connection._untagged_response(tmpA, tmpB, 'ID'))
                # -------------------------------------
                imaplib.Commands['ID'] = ('AUTH')
                args = ('name', 'XXXX', 'contact', 'XXXX@163.com', 'version', '1.0.0', 'vendor', 'myclient')
                self.connection._simple_command('ID', '("' + '" "'.join(args) + '")')
                self.connection.select()
                (__, mailList) = self.connection.search(None, '(ALL)')
                return [[x.decode(), None] for x in reversed(mailList[0].split())]
            else:
                print(f'敬请期待 {self.serverAddress} 服务器 (/(ㄒoㄒ)/~~)')
                # input('\n按 Enter 键退出...')
                sys.exit()
                
    def GetEmailHeaderBytesStream(self, idx:str) -> bytes:
        """重写公有成员函数: 获取邮件头部字节流, 为了优先快速遍历.

        Args:
            idx (str): 字符串形式的邮件编号.

        Returns:
            bytes: 头字节(流).
        """
        (__, bytesStream) = self.connection.fetch(idx, '(BODY[HEADER])')    # (RFC822)
        if bytesStream[0] is None:
            print('IMAP 协议解析邮件失败')
        return bytesStream[0][1]

    def GetEmailFullBytesStream(self, idx:str) -> bytes:
        """重写公有成员函数: 获取邮件全字节流, 为了下载附件.

        Args:
            idx (str): 字符串形式的邮件编号.

        Returns:
            bytes: 全字节(流).
        """
        (__, bytesStream) = self.connection.fetch(idx, '(RFC822)')  # '(BODY[HEADER])'
        IMAP.SIZE = int(re.findall(r'\d+', bytesStream[0][0].split()[2].decode())[0])
        return bytesStream[0][1]


class EMAIL:
    """邮箱附件下载类, 用于批量化下载附件, 亲测好用 (｡･ω･｡)ﾉ♡ 哟.
    """
    
    PROGRESS = 0

    def __init__(
        self,
        *args,
        emailAddress: str | None,
        protocolPassword: str | None,
        protocol:str,
        serverAddress: str | None,
        attachmentSaveDirectory: str | None = SCAN.SlashBackslash(
            (os.getcwd() + os.sep + 'Attachments') if not PROOFREAD_ABSTRACT.GetDesktopPath()
            else SCAN.SlashBackslash(PROOFREAD_ABSTRACT.GetDesktopPath() + os.sep + 'Attachments')
        ),
        attachmentSaveMode: Literal[
            '所有附件一个文件夹',
            '每个邮箱一个文件夹',
            '每个主题一个文件夹',
            '每个昵称一个文件夹',
            '每个主题多个邮箱一个文件夹'
        ] = '所有附件一个文件夹',
        headSeveralEmail:int = 1000000,
        isOverwrite:bool = False,
        timeZone:str = 'GMT+8',
        timePeriodRange:list = ['', datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
        filterEmailAddress:list[str] = [],
        filterNickname:list[str] = [],
        filterSubject:list[str] = [],
        showLogs:bool = False,
        **kwargs
    ) -> None:
        """初始化构造函数: Windows 终端渲染, 赋值公有成员变量.

        Args:
            emailAddress (str | None): 邮箱地址.
            protocolPassword (str | None): 协议密码.
            protocol (str): 协议类型, 目前只有 POP3 和 IMAP 两种.
            serverAddress (str | None): 服务器地址.
            attachmentSaveDirectory (str | None): 附件保存路径, 默认桌面, 如果找不到则保存到当前工作路径.
            attachmentSaveMode (Literal[ ): 附件保存模式, 见形参注解的 5 种字面量, 默认所有附件一个文件夹.
            headSeveralEmail (int): 收取邮箱顶部若干封邮件, 即收取全部邮件, 默认一个超大值.
            isOverwrite (bool): 是否覆盖附件所在的本地磁盘同名文件, 默认不覆盖.
            timeZone (str): 时区, 采用 GMT+X 格式, 发行版已删除旧的 UTC 格式, 默认东八区.
            timePeriodRange (list): 收取某个时间段内的附件, 默认到本地时间为止.
            filterEmailAddress (list[str]): 过滤掉的邮件地址, 不收取其附件, 默认空列表.
            filterNickname (list[str]): 过滤掉的发件人昵称, 不收其附件, 默认空列表.
            filterSubject (list[str]): 过滤掉的邮件主题, 不收取相应的附件, 默认空列表.
            showLogs (bool): 是否显示日志, 默认不显示.
        """
        self.__dict__.update(**kwargs)
        self.emailAddress = emailAddress
        self.protocolPassword = protocolPassword
        self.protocol = protocol
        self.serverAddress = serverAddress
        self.attachmentSaveDirectory = attachmentSaveDirectory
        self.attachmentSaveMode = attachmentSaveMode
        self.headSeveralEmail = headSeveralEmail
        self.isOverwrite = isOverwrite
        self.timeZone = timeZone
        self.timePeriodRange = timePeriodRange
        self.filterEmailAddress = filterEmailAddress
        self.filterNickname = filterNickname
        self.filterSubject = filterSubject
        self.showLogs = showLogs 
        self.__Inspect()
        self.__CheckProtocol()
        self.originalFilesNumber = len(SCAN.RecursiveGetFiles(attachmentSaveDirectory))

    def __CheckProtocol(self) -> None:
        """私有成员函数: 检查邮件协议类型.
        """
        if self.protocol.lower() in ['pop', 'pop3']:
            self.receiver = POP(
                emailAddress = self.emailAddress,
                serverAddress = self.serverAddress,
                protocolPassword = self.protocolPassword
            )
        elif self.protocol.lower() in ['imap', 'imap4']:
            self.receiver = IMAP(
                emailAddress = self.emailAddress,
                serverAddress = self.serverAddress,
                protocolPassword = self.protocolPassword
            )
        else:
            print(f'\033[31mError: \033[0m请问您这 {self.protocol} 是什么最新的邮件协议, 既不是 POP 又不是 IMAP...')
            # input('\n按 Enter 键退出...')
            sys.exit()

    def Download(self) -> tuple:
        """公有成员函数: 登录服务器邮箱成功后下载附件.
        
        Returns:
            tuple: 返回附件下载的结果信息列表以及其他记录元组.
        """
        params: dict = {
            'parseNumber': 0,
            'increaseNumber': 0,
            'filterNumber': 0,
            'diskFilesNumber': 0,
            'spaceUsage': 0,
        }
        products = []
        if self.receiver is None:
            print('未接收到来自邮箱返回的状态信息...')
            # input('\n按 Enter 键退出...')
            sys.exit()
        fty: object = FACTORY(self.attachmentSaveMode, self.isOverwrite)
        (quantities, totalSize) = self.receiver.GetEmailStatus()
        if self.showLogs:
            print('\033[31m红代表错误\033[0m | \033[33m黄代表警告\033[0m')
            print('\033[32m绿代表下载\033[0m | \033[36m蓝代表过滤\033[0m')
            print(f'附件保存目录: {self.attachmentSaveDirectory}\n')
        print(f'邮件总数量: {quantities}')
        print(f'邮件总大小: {TRANSFORM.BytesTransform(totalSize)}\n')
        # 获取所有邮件的先行信息, 即邮件编号和占用大小(单位字节).
        antecedentInformation: list[list] = EMAIL.InterceptTop(
            L = self.receiver.GetEmailList(),
            breakpoint = int(self.headSeveralEmail)
        )
        warning: int = 0
        N = len(antecedentInformation)
        with alive_bar(N, bar='bubbles', spinner='notes2') as bar:
            pos = 1
            for (idx, mailSize) in antecedentInformation:
                try:
                    headContents: bytes = self.receiver.GetEmailHeaderBytesStream(idx)
                    headMessage: object = TRANSFORM.ParseMailBytesStream(headContents)
                    container: object = TRANSFORM.ParseMessageInformation(headMessage, mailSize)
                except:
                    if self.showLogs:
                        print(f'\033[33mWarning --> 邮件编号: [{pos}]\033[0m, 邮件解析失败(\033[43m不影响附件下载\033[0m), 后续手动检查吧...')
                    warning = -~warning
                    bar()   # 如果遇到异常邮件, 解析失败后依然增加进度条.
                    continue
                try:
                    fullContents: bytes = self.receiver.GetEmailFullBytesStream(idx)
                    fullMessage: object = TRANSFORM.ParseMailBytesStream(fullContents)
                    TRANSFORM.AddFilterAttachmentsName(fullMessage, container)
                    params['parseNumber'] = -~params['parseNumber']
                except:
                    fullMessage = None
                    if self.showLogs:
                        print(f'\033[31mError --> 邮件编号: [{pos}] \033[0m\033[41m未能解析邮件字节流.\033[0m')
                ftr: object = FILTER()
                ftr.AddFilter(SUBJECT(set(self.filterSubject), container.subject))
                ftr.AddFilter(ADDRESS(set(self.filterEmailAddress), container.emailAddress))
                ftr.AddFilter(NICKNAME(set(self.filterNickname), container.nickname))
                ftr.AddFilter(DATE(self.timePeriodRange, self.timeZone, container.date))
                if not ftr.Filter():
                    try:
                        TRANSFORM.ParseAttachments(
                            factory = fty,
                            message = fullMessage,
                            container = container,
                            dir = self.attachmentSaveDirectory
                        )
                        if self.protocol.lower() in ['imap', 'imap4']:
                            container.size = TRANSFORM.BytesTransform(IMAP.SIZE)
                        if len(container.attachments) != 0:
                            products.append(
                                [
                                    container.emailAddress,
                                    container.attachments,
                                    container.subject,
                                    container.date
                                ]
                            )
                        if self.showLogs:
                            if len(container.attachments) != 0:
                                print(f'\033[32m{container}\033[0m')
                            else:
                                print(container)
                    except:
                        if self.showLogs:
                            print(f'\033[31mError --> 邮件编号: [{pos}] \033[0m\033[41m未能解析邮件字节流, 附件下载失败!\033[0m')
                else:
                    params['filterNumber'] = -~params['filterNumber']
                    if self.showLogs:
                        print(f'\033[36m{container}\033[0m')
                bar()
                pos = -~pos
                EMAIL.PROGRESS = round(100 * (pos) / N, 2)
        print(f'一共\033[31m {warning} \033[0m封邮件首部信息解析失败(不影响附件解析).')
        terminalFilesNumber = len(SCAN.RecursiveGetFiles(self.attachmentSaveDirectory))
        print(f'新增\033[32m {terminalFilesNumber - self.originalFilesNumber} \033[0m封邮件.')
        params['increaseNumber'] = terminalFilesNumber - self.originalFilesNumber
        params['diskFilesNumber'] = len(SCAN.RecursiveGetFiles(self.attachmentSaveDirectory))
        params['spaceUsage'] = TRANSFORM.BytesTransform(EMAIL.GetFolderSize(self.attachmentSaveDirectory))
        EMAIL.PROGRESS = 0
        if self.showLogs:
            print('\033[31m红代表错误\033[0m | \033[33m黄代表警告\033[0m')
            print('\033[32m绿代表下载\033[0m | \033[36m蓝代表过滤\033[0m')
            print(f'附件保存目录: {self.attachmentSaveDirectory}\n')
        return (products, params)

    @staticmethod
    def InterceptTop(L:list[list], breakpoint:int) -> list[list]:
        """静态函数: 截取嵌套列表前 breakpoint 个子嵌套列表.

        Args:
            L (list[list]): 传入嵌套列表.
            breakpoint (int): 截断点处.

        Returns:
            list[list]: 截断后的嵌套列表.
        """
        if 0 < breakpoint <= len(L):
            return L[:breakpoint]
        else:
            return L

    def __Inspect(self) -> None:
        """私有成员函数: 检查实例化对象的实参是否合法.
        """
        L = ['所有附件一个文件夹', '每个邮箱一个文件夹', '每个主题一个文件夹', '每个昵称一个文件夹', '每个主题多个邮箱一个文件夹']
        if self.attachmentSaveMode not in L:
            print(f'暂未提供\033[31m "{self.attachmentSaveMode}" \033[0m保存模式')
            print('仅有如下 5 种:')
            for i in L:
                print(f'\t{i}')
            # input('\n按 Enter 键退出...')
            sys.exit()
        try:
            tmp = re.search(r'[-+]\d+', self.timeZone).group()
            prefix = self.timeZone[:self.timeZone.find(tmp)]
            if prefix.lower() == 'gmt':
                self.timeZone = tmp
            else:
                1 / 0
        except:
            print(f'格林尼治标准时区有误\033[31m "{self.timeZone}" \033[0m')
            print(f'如果你想用东八区, 实参应为:\033[32m GMT+8 \033[0m')
            print(f'如果你想用西三区, 实参应为:\033[32m GMT-3 \033[0m')
            # input('\n按 Enter 键退出...')
            sys.exit()
    
    @staticmethod
    def GetFolderSize(dir:str) -> int:
        """静态函数: 获取文件夹大小.

        Args:
            dir (str): 目录.

        Returns:
            int: 整型.
        """
        totalSize = 0
        for (path, __, files) in os.walk(dir):
            for file in files:
                filePath = os.path.join(path, file)
                totalSize = totalSize + os.path.getsize(filePath)
        return totalSize