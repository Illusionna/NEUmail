'''
# System --> Windows & Python3.10.0
# File ----> inherit.py
# Author --> Illusionna
# Create --> 2024/03/22 01:15:28
'''
# -*- Encoding: UTF-8 -*-


import os
import sys
import json
import hashlib
import webbrowser
from threading import Timer
from datetime import (datetime, timedelta)
from utils.resource import RESOURCE
from flask import (Flask, render_template, jsonify, request)
from utils.interface import (SCAN_ABSTRACT, PROOFREAD_ABSTRACT, GUIDE_ABSTRACT, USAGE_ABSTRACT)


class SCAN(SCAN_ABSTRACT):
    """继承扫描抽象类.

    Args:
        SCAN_ABSTRACT (_type_): 扫描 Web 前端所需要的 static 静态文件内容完整性.
    """

    def __init__(self) -> None:
        SCAN.Download()
        if not os.path.exists(os.getcwd() + os.sep + './config.json'):
            with open(os.getcwd() + os.sep + './config.json', mode='w', encoding='utf-8') as f:
                json.dump(
                    obj = PROOFREAD.DEFAULT,
                    fp = f,
                    ensure_ascii = False,
                    indent = 4,
                    separators = (',', ': ')
                )
        os.makedirs(os.getcwd() + os.sep + 'templates', exist_ok=True)
        dir: str = os.getcwd() + os.sep + 'templates/intro.html'
        if not os.path.exists(dir):
            with open(dir, mode='w', encoding='utf-8') as f:
                f.write(RESOURCE.INTRO)
        dir: str = os.getcwd() + os.sep + 'templates/config.html'
        if not os.path.exists(dir):
            with open(dir, mode='w', encoding='utf-8') as f:
                f.write(RESOURCE.CONFIG)
        dir: str = os.getcwd() + os.sep + 'templates/download.html'
        if not os.path.exists(dir):
            with open(dir, mode='w', encoding='utf-8') as f:
                f.write(RESOURCE.DOWNLOAD)
        dir: str = os.getcwd() + os.sep + 'templates/advanced.html'
        if not os.path.exists(dir):
            with open(dir, mode='w', encoding='utf-8') as f:
                f.write(RESOURCE.ADVANCED)
        dir: str = os.getcwd() + os.sep + 'templates/error.html'
        if not os.path.exists(dir):
            with open(dir, mode='w', encoding='utf-8') as f:
                f.write(RESOURCE.ERROR)

    @staticmethod
    def SlashBackslash(dir:str, axis:bool=True) -> str:
        """路径斜杠与反斜杠统一函数.

        Args:
            dir (str): 文件路径.
            axis (bool, optional): 统一方向. Defaults to True.

        Returns:
            str: 统一后的路径字符串.
        """
        if axis == True:
            return dir.replace('\\', '/')
        else:
            return dir.replace('/', '\\')

    @staticmethod  
    def RecursiveGetFiles(directory:str) -> list:
        """递归式返回文件夹下所有文件路径.

        Args:
            directory (str): 文件夹目录.

        Returns:
            list: 所有路径列表.
        """
        L = []
        for (root, __, filenames) in os.walk(directory):
            for file in filenames:
                filePath = os.path.join(root, file)
                L.append(filePath)
        return L

    @staticmethod
    def CalculateFileHash(dir:str) -> str:
        tmp: object = hashlib.new('sha256')
        with open(dir, mode='rb') as f:
            while True:
                data = f.read(64 << 10)
                if not data:
                    break
                tmp.update(data)
        return tmp.hexdigest()

    @staticmethod
    def Compare() -> bool:
        judge: bool = os.path.exists(os.getcwd() + os.sep + './static')
        if judge == False:
            return False
        else:
            L: list = SCAN.RecursiveGetFiles(os.getcwd() + os.sep + './static')
            tmp: str = os.getcwd() + os.sep + './static'
            idx: int = tmp.find('static')
            currentDictionary: dict = {}
            for i in L:
                currentDictionary[SCAN.SlashBackslash(i[idx-2:])] = SCAN.CalculateFileHash(i)
            if set(RESOURCE.STANDARD_STATIC_HASH.items()).issubset(currentDictionary.items()):
                return True
            else:
                return False

    @staticmethod
    def Download() -> None:
        os.system('')
        if not SCAN.Compare():
            if os.path.exists(os.getcwd() + os.sep + './utils/scan.exe'):
                os.system(os.getcwd() + os.sep + './utils/scan.exe')
                sys.exit()
            else:
                print('')
                print('\033[31m缺少\033[0m "./utils" 工具包, 下载网址:')
                print('\033[33mhttps://gitee.com/Senu/Sharing/raw/master/utils.zip\033[0m')
                print(f"\033[32m解压到: {os.getcwd() + os.sep + 'utils' + os.sep + '*'}\033[0m")
                print('或者')
                print('编译源码 >>> gcc ./utils/scan.c -o ./utils/scan.exe')
                input('\n按 Enter 键退出...')
                sys.exit()


class PROOFREAD(PROOFREAD_ABSTRACT):
    """继承校对抽象类.

    Args:
        PROOFREAD_ABSTRACT (_type_): 校对 config.json 配置文件的初始化设置.
    """

    SKIP: bool = False

    DEFAULT: dict = {
        'skip': False,
        'emailAddress': '',
        'protocolPassword': '',
        'protocol': 'POP3',
        'serverAddress': '',
        'attachmentSaveDirectory': (
            None if not PROOFREAD_ABSTRACT.GetDesktopPath()
            else SCAN.SlashBackslash(PROOFREAD_ABSTRACT.GetDesktopPath() + os.sep + 'Attachments')
        ),
        'attachmentSaveMode': '所有附件一个文件夹',
        'headSeveralEmail': 1000000,
        'isOverwrite': False,
        'timeZone': 'GMT+8',
        'timePeriodRange': [(datetime.now() - timedelta(days=36500)).strftime('%Y-%m-%d %H:%M:%S'), (datetime.now() + timedelta(days=365)).strftime('%Y-%m-%d %H:%M:%S')],
        'filterEmailAddress': [],
        'filterNickname': [],
        'filterSubject': []
    }

    def __init__(self) -> None:
        PROOFREAD.SkipJudge()

    @staticmethod
    def CreateJson() -> None:
        if not os.path.exists(os.getcwd() + os.sep + './config.json'):
            with open(os.getcwd() + os.sep + './config.json', mode='w', encoding='utf-8') as f:
                json.dump(
                    obj = PROOFREAD.DEFAULT,
                    fp = f,
                    ensure_ascii = False,
                    indent = 4,
                    separators = (',', ': ')
                )

    @staticmethod
    def LoadJson() -> dict:
        with open(os.getcwd() + os.sep + './config.json', mode='r', encoding='utf-8') as f:
            config: dict = json.load(f)
        return config

    @staticmethod
    def WriteJson(config:dict) -> None:
        with open(os.getcwd() + os.sep + './config.json', mode='w', encoding='utf-8') as f:
            json.dump(
                obj = config,
                fp = f,
                ensure_ascii = False,
                indent = 4,
                separators = (',', ': ')
            )

    @staticmethod
    def SkipJudge() -> None:
        PROOFREAD.CreateJson()
        config: dict = PROOFREAD.LoadJson()
        if config['skip'] == False:
            GUIDE()
            GUIDE.SKIP = True
        elif config['skip'] == True:
            USAGE()
            USAGE.SKIP = True
            PROOFREAD.SKIP = config['skip']
        else:
            # 防止 "./config.json" 的 skip 键值对被无意修改成非 bool 类型.
            with open(os.getcwd() + os.sep + './config.json', mode='w', encoding='utf-8') as f:
                json.dump(
                    obj = PROOFREAD.DEFAULT,
                    fp = f,
                    ensure_ascii = False,
                    indent = 4,
                    separators = (',', ': ')
                )


class GUIDE(GUIDE_ABSTRACT):
    """继承引导抽象类.

    Args:
        GUIDE_ABSTRACT (_type_): 用于指导新手完成 config.json 文件配置的前端.
    """

    SKIP: bool = False
    DATA = {}

    def __init__(self) -> None:
        if ((GUIDE.SKIP == False) & (PROOFREAD.SKIP == False)):
            self.Start()

    def Start(self):
        """启动Flask应用和Web引导界面。"""
        self.app = Flask(__name__, static_folder='../static', template_folder='../templates')

        @self.app.route('/')
        def index():
            """根路由：返回引导页面。"""
            return render_template('intro.html')

        @self.app.route('/save-config', methods=['POST'])
        def save_config():
            """保存配置到config.json文件，仅更新提供的字段。"""
            new_data = request.get_json()
            if not new_data:
                return jsonify({"status": "error", "message": "未接收到数据"}), 400
            try:
                # 定位config.json文件的路径
                config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.json')
                
                # 尝试读取现有的配置
                if os.path.exists(config_path):
                    with open(config_path, 'r', encoding='utf-8') as file:
                        data = json.load(file)
                else:
                    data = {}  # 如果文件不存在，初始化为空字典

                # 更新数据：仅对提供了新值的字段进行更新
                for key, value in new_data.items():
                    if value or (isinstance(value, bool)):  # 确保布尔类型的值被正确处理
                        data[key] = value

                # 将更新后的配置写回文件
                GUIDE.DATA = data
                with open(config_path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
                GUIDE.DATA = data

                return jsonify({"status": "success", "message": "配置保存成功"})
            except Exception as e:
                return jsonify({"status": "error", "message": f"保存配置时出错: {e}"}), 500

        @self.app.route('/check-config', methods=['POST'])
        def handle_check_config():
            """处理配置完成的请求，并检查配置状态。"""
            self.check_config()
            return jsonify({"status": "success", "message": "配置检查完成"}), 200

        @self.app.route('/config')
        def config_page():
            """配置页面路由：返回config.html页面。"""
            # 如果config.html位于一个非标准位置，可以使用send_from_directory来返回文件
            # 此处假设config.html位于标准的templates文件夹中
            return render_template('config.html')

        print("正在打开Web引导界面…")
        # webbrowser.open_new('http://localhost:9999')
        Timer(1, lambda: webbrowser.open_new('http://localhost:9999/')).start()
        self.app.run(host='localhost', port=9999, debug=True, use_reloader=False)

    def check_config(self):
        """检查配置完成状态，并执行后续步骤。"""
        try:
            config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.json')
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            self.proceed_after_config()
        except FileNotFoundError:
            print("config.json 文件未找到，请确保配置流程已完成。")

    def proceed_after_config(self):
        """配置完成后的处理流程，使用多进程打开config.html页面。"""
        KEYS = set(GUIDE.DATA.keys())
        for key, value in PROOFREAD.DEFAULT.items():
            if key in KEYS:
                pass
            else:
                GUIDE.DATA[key] = value
        with open(os.getcwd() + os.sep + 'config.json', 'w', encoding='utf-8') as file:
            json.dump(GUIDE.DATA, file, ensure_ascii=False, indent=4)
        import signal
        os.kill(os.getpid(), signal.SIGINT)


class USAGE(USAGE_ABSTRACT):
    """继承使用抽象类.

    Args:
        USAGE_ABSTRACT (_type_): 用于邮箱附件下载的前端.
    """
    
    SKIP: bool = False

    def __init__(self) -> None:
        if USAGE.SKIP == False:
            USAGE.Activate()

    @staticmethod
    def Activate() -> None:
        import usage