'''
# System --> Windows & Python3.10.0
# File ----> tool.py
# Author --> Illusionna
# Create --> 2024/03/22 14:31:25
'''
# -*- Encoding: UTF-8 -*-


import re
import datetime
from email.parser import Parser
from email.utils import parseaddr
from email.header import decode_header
from utils.core.Factory import FACTORY


class CONTAINER:
    """容器类, 当垃圾桶存数据, 嘿嘿 (●ˇ∀ˇ●).
    """

    def __init__(self) -> None:
        self.subject = None
        self.emailAddress = None
        self.nickname = None
        self.date = None
        self.size = None
        self.attachments = []
        
    def AddAttachmentName(self, name:str) -> None:
        """公有成员函数: 添加附件名称到容器垃圾桶的附件字段中.

        Args:
            name (str): 字符串名称.
        """
        self.attachments.append(name)

    def __str__(self) -> str:
        """重写类字符串序列化函数.

        Returns:
            str: 键值对式字符串.
        """
        tmp = ''
        for (key, value) in self.__dict__.items():
            tmp = tmp + f'{key}: {value}\n'
        return tmp


class TRANSFORM:
    """转化类.
    """
    
    @staticmethod
    def BytesTransform(byteSize:int | None) -> str:
        """静态公有函数: 把字节转化为大家通常认知的单位.

        Args:
            byteSize (int | None): 传入字节的尺寸大小.

        Returns:
            str: 转化后的字符串.
        """
        transformTable = {
            'B': [1, (1 << 10) - 1],
            'KB': [(1 << 10), (1 << 20) - 1],
            'MB': [(1 << 20), (1 << 30) - 1],
            'GB': [(1 << 30), (1 << 40) - 1],
            'TB': [(1 << 40), (1 << 99) - 1]
        }
        if byteSize:
            for (key, value) in transformTable.items():
                if (value[0] <= byteSize <= value[1]):
                    return f'{(byteSize / transformTable[key][0]):.2f} {key}'
        else:
            return '不晓得'
    
    @staticmethod
    def ParseMailBytesStream(contentBytesStream:bytes) -> object:
        """静态公有函数: 接卸邮件字节流.

        Args:
            contentBytesStream (bytes): 邮件字节流.

        Returns:
            object: 返回 'email.message.Message' 对象.
        """
        try:
            mailContent: str = contentBytesStream.decode()
        except UnicodeDecodeError as e:
            mailContent: str = contentBytesStream.decode(encoding='GB18030', errors='replace')
        return Parser().parsestr(mailContent)
    
    @staticmethod
    def ParseMessageInformation(message:object, size:int) -> CONTAINER:
        """静态公有函数: 解析 'email.message.Message' 邮件对象的内容信息.

        Args:
            message (object): 'email.message.Message' 类型的邮件对象.
            size (int): 邮件尺寸大小.

        Returns:
            CONTAINER: 容器垃圾桶类.
        """
        container = CONTAINER()
        TRANSFORM.__ParseSubject(container, message.get('Subject'))
        TRANSFORM.__ParseSender(container, message.get('From'))
        TRANSFORM.__ParseDate(container, message)
        container.size = TRANSFORM.BytesTransform(size)
        return container

    @staticmethod
    def __ParseSubject(container:CONTAINER, bytesStream:bytes) -> None:
        """静态私有函数: 解析字节流的主题.

        Args:
            container (CONTAINER): 容器.
            bytesStream (bytes): 邮件字节流.
        """
        try:
            container.subject = TRANSFORM.__DecodeMailInformationBytesToString(
                bytesStream = bytesStream
            )
        except:
            container.subject = '【!#已重置: 无主题#!】'

    @staticmethod
    def __DecodeMailInformationBytesToString(bytesStream:bytes) -> str:
        """静态私有函数: 把邮件信息由字节流解码成字符串.

        Args:
            bytesStream (bytes): 字节流.

        Returns:
            str: 字符串.
        """
        result = []
        for (value, charset) in decode_header(bytesStream):
            if type(value) != str:
                if charset is None:
                    value = value.decode(errors='replace')
                elif charset.lower() in ['gbk', 'gb2312', 'gb18030']:
                    value = value.decode(encoding='gb18030', errors='replace')
                else:
                    value = value.decode(charset, errors='replace')
            result.append(value)
        return ' '.join(result)
    
    @staticmethod
    def __ParseSender(container:CONTAINER, bytesStream:bytes) -> None:
        """静态私有函数: 解析字节流的发件人邮箱地址和其昵称.

        Args:
            container (CONTAINER): 容器.
            bytesStream (bytes): 邮件字节流.
        """
        (name, emailAddress) = parseaddr(bytesStream)
        container.emailAddress = emailAddress
        try:
            container.nickname = TRANSFORM.__DecodeMailInformationBytesToString(name)
        except:
            container.nickname = '【!#已重置: 佚名#!】'
            
    @staticmethod    
    def __ParseDate(container:CONTAINER, message:object) -> None:
        """静态私有函数: 解析字节流的发件时间.

        Args:
            container (CONTAINER): 容器.
            message (object): 'email.message.Message' 对象.
        """

        def DecodeDateFromReceived() -> None | str:
            """内部函数: 解码邮件时间.

            Returns:
                None | str: 可能解码成功获取到时间.
            """
            tmp = message.get('Received')
            if tmp is None:
                return None
            return tmp[tmp.rfind(';')+1:]

        def DecodeDateFrom_X_QQ_mid() -> None | str:
            """内部函数: 解码 QQ 邮件的时间.

            Returns:
                None | str: 可能解码成功获取到时间.
            """
            tmp = message.get('X-QQ-mid')
            if tmp is None:
                return None
            timeString = re.findall('t[0-9]{10}t', tmp)
            if len(timeString) == 0:
                return None
            time = datetime.datetime.fromtimestamp(
                float(timeString[0][1:-1]),
                datetime.timezone.utc
            )
            transformTime = datetime.datetime.strptime(
                datetime.datetime.strptime(
                    time.strftime('%d %b %Y %H:%M:%S %z'),
                    '%d %b %Y %H:%M:%S %z'
                ).strftime('%Y-%m-%d %H:%M:%S %z'),
                '%Y-%m-%d %H:%M:%S %z'
            ).astimezone(datetime.timezone(datetime.timedelta(hours=8)))
            return transformTime.strftime('%Y-%m-%d %H:%M:%S %z')

        try:
            container.date = message.get('Date')
            if container.date is None:
                container.date = DecodeDateFromReceived()
                if container.date is None:
                    container.date = DecodeDateFrom_X_QQ_mid()
                    if container.date is None:
                        print(f'邮件接收时间解析失败, 主题为:\033[31m {container.subject}\033[0m')
        except:
            container.date = None

    @staticmethod
    def ParseAttachments(
        factory:FACTORY,
        message:object,
        container:CONTAINER,
        dir:str
    ) -> None:
        """静态公有函数: 解析 'email.message.Message' 邮件对象的附件信息.

        Args:
            factory (FACTORY): 附件保存格式对象.
            message (object): 'email.message.Message' 对象.
            container (CONTAINER): 容器垃圾桶对象.
            dir (str): 附件保存路径.
        """
        if message != None:
            for part in message.walk():
                fileNameBytesStream = part.get_filename()
                if fileNameBytesStream:
                    fileName = TRANSFORM.__DecodeMailInformationBytesToString(fileNameBytesStream)
                    data = part.get_payload(decode=True)
                    factory(dir, fileName, data, container).Save()

    @staticmethod
    def AddFilterAttachmentsName(message:object, container:CONTAINER) -> None:
        """静态公有函数: 添加过滤附件名称.

        Args:
            message (object): 'email.message.Message' 对象.
            container (CONTAINER): 容器.
        """
        for part in message.walk():
            fileNameBytesStream = part.get_filename()
            if fileNameBytesStream:
                fileName = TRANSFORM.__DecodeMailInformationBytesToString(fileNameBytesStream)
                container.AddAttachmentName(name=fileName)