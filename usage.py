'''
# System --> Windows & Python3.10.0
# File ----> usage.py
# Author --> Illusionna
# Create --> 2024/03/27 10:48:18
'''
# -*- Encoding: UTF-8 -*-


import os
import csv
import json
import webbrowser
from datetime import datetime
import utils.core.EmailDownload
from utils.inherit import (SCAN, PROOFREAD)
from flask import (Flask, render_template, request, redirect, url_for, jsonify)

with open(os.getcwd() + os.sep + 'config.json', mode='r', encoding='utf-8') as f:
    config = json.load(f)
app = Flask(__name__, static_folder='./static', template_folder='./templates')
exportDir = SCAN.SlashBackslash(PROOFREAD.GetDesktopPath() + os.sep + 'export.csv')

def Adjust(value:str) -> int:
    try:
        value = int(value)
        if value < 0:
            value = 1000000
    except:
        value = 1000000
    return value

config['headSeveralEmail'] = str(Adjust(config['headSeveralEmail']))

class ERROR:
    error = False

def GetIndexParams() -> dict:
    """获取主页捕获的数据, 并且加载 json 里面的高级功能数据.

    Returns:
        dict: 键值对.
    """
    return {
        'emailAddress': request.form['email'],
        'protocolPassword': request.form['password'],
        'protocol': request.form['protocol'],
        'serverAddress': request.form['server'],
        'attachmentSaveDirectory': SCAN.SlashBackslash(request.form['attachment']),
        'attachmentSaveMode': request.form['method'],
        'headSeveralEmail': Adjust(request.form['headSeveralEmail']),
        'isOverwrite': (True if request.form['overwrite'] == '1' else False),
        'timeZone': config['timeZone'],
        'timePeriodRange': config['timePeriodRange'],
        'filterEmailAddress': config['filterEmailAddress'],
        'filterNickname': config['filterNickname'],
        'filterSubject': config['filterSubject']
    }
    
def WriteJson(data:dict) -> None:
    """把字典数据写入 config.json 文件.

    Args:
        data (dict): 键值对.
    """
    with open(os.getcwd() + os.sep + 'config.json', mode='w', encoding='utf-8') as f:
        json.dump(
            obj = data,
            fp = f,
            ensure_ascii = False,
            indent = 4,
            separators = (',', ': ')
        )

@app.route('/')
def Index() -> str:
    """流量器加载首索引 config.html 文件.

    Returns:
        str: 返回主页, 并给主页传入后端的 json 文件数据.
    """
    contextParameters: dict = {
        'emailAddress': config['emailAddress'],
        'protocolPassword': config['protocolPassword'],
        'serverAddress': config['serverAddress'],
        'protocol': config['protocol'],
        'isOverwrite': config['isOverwrite'],
        'attachmentSaveDirectory': SCAN.SlashBackslash(config['attachmentSaveDirectory']),
        'attachmentSaveMode': config['attachmentSaveMode'],
        'headSeveralEmail': config['headSeveralEmail']
    }
    return render_template('config.html', **contextParameters)

@app.route('/capture', methods=['GET', 'POST'])
def IndexCapture() -> str:
    """主索引页 config.html 捕获前端内容传给后端.

    Returns:
        str: 返回主页捕获的数据, 并返回 config.json 文件的高级功能数据.
    """
    ERROR.error = False
    if request.method == "POST":
        try:
            indexParams: dict = GetIndexParams()
            config.update(indexParams)
            WriteJson(data=config)
            global args
            global products
            global attachmentSaveDirectory
            attachmentSaveDirectory = config['attachmentSaveDirectory']
            config['isOverwrite'] = config['isOverwrite']
            instance = utils.core.EmailDownload.EMAIL(**config)
            (tmp, args) = instance.Download()
            products = []
            for file in tmp:
                pos = 0
                while pos < len(file[1]):
                    products.append([file[0], file[1][pos], file[2], file[3]])
                    pos = -~pos
            return redirect(url_for('Download'))
        except:
            ERROR.error = True
            return render_template('error.html')
    return render_template('config.html', error=False)

@app.route('/progress')
def Progress() -> object:
    """主页 config.html 的进度条.

    Returns:
        object: Response 对象.
    """
    if ERROR.error:
        ERROR.error = False
        return jsonify({'error': True, 'message': '无法连接到邮箱服务器'})
    return jsonify(
        {'res': (
            utils.core.EmailDownload.EMAIL.PROGRESS
            if utils.core.EmailDownload.EMAIL.PROGRESS <= 100
            else 100
        )}
    )

@app.route('/advanced')
def Advanced() -> str:
    """高级配置页面.

    Returns:
        str: 返回高级配置.
    """
    return render_template(
        template_name_or_list = 'advanced.html',
        timeZone = config['timeZone'],
        startTime = config['timePeriodRange'][0],
        terminalTime = config['timePeriodRange'][1],
        filterEmailAddress = config['filterEmailAddress'],
        filterSubject = config['filterSubject'],
        filterNickname = config['filterNickname']
    )

@app.route('/download')
def Download() -> str:
    """下载完成页面.

    Returns:
        str: 给完成页面传入的参数数据.
    """
    return render_template(
        template_name_or_list = 'download.html',
        parseNumber = args['parseNumber'],
        increaseNumber = args['increaseNumber'],
        filterNumber = args['filterNumber'],
        diskFilesNumber = args['diskFilesNumber'],
        spaceUsage = args['spaceUsage'],
        exportDir = exportDir,
        attachmentSaveDirectory = SCAN.SlashBackslash(attachmentSaveDirectory),
        products = products
    )

@app.route('/export')
def Export() -> str:
    """导出下载完成后的文件表格.

    Returns:
        str: 反馈给前端.
    """
    products.insert(0, ['邮箱地址', '附件', '主题', '收件时间'])
    with open(exportDir, mode='w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerows(products)
    del products[0]
    return render_template(
        template_name_or_list = 'download.html',
        parseNumber = args['parseNumber'],
        increaseNumber = args['increaseNumber'],
        filterNumber = args['filterNumber'],
        diskFilesNumber = args['diskFilesNumber'],
        spaceUsage = args['spaceUsage'],
        attachmentSaveDirectory = SCAN.SlashBackslash(attachmentSaveDirectory),
        exportDir = exportDir,
        products = products
    )

@app.route('/save', methods=['POST'])
def Save() -> object:
    """保存所有配置, 包括高级以及基础.

    Returns:
        object: Response 对象.
    """
    tmp: dict = request.json
    try:
        a: str = datetime.strptime(
            tmp['startTime'].replace('T', ' '),
            (
                '%Y-%m-%d %H:%M:%S' if len(tmp['startTime'].replace('T', ' ')) > 16
                else '%Y-%m-%d %H:%M'
            )
            ).replace(second=0).strftime('%Y-%m-%d %H:%M:%S'
        )
    except:
        a = '1949-12-31 23:59:59'
    try:
        b: str = datetime.strptime(
            tmp['endTime'].replace('T', ' '),
            (
                '%Y-%m-%d %H:%M:%S' if len(tmp['endTime'].replace('T', ' ')) > 16
                else '%Y-%m-%d %H:%M'
            )
            ).replace(second=0).strftime('%Y-%m-%d %H:%M:%S'
        )
    except:
        b = '2099-12-31 23:59:59'
    timePeriodRange = [a, b]
    del tmp['startTime'], a
    del tmp['endTime'], b
    tmp['timePeriodRange'] = timePeriodRange
    config.update(tmp)
    WriteJson(data=config)
    return jsonify({'message': 'Success'})


webbrowser.open('http://localhost:8888')
app.run(host='localhost', port=8888, debug=False)