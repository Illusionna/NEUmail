/*
System --> Windows & mingw64gcc8.1.0
File ----> scan.c
Author --> Illusionna
Create --> 2024/03/21 22:16:30
'''
-*- Encoding: UTF-8 -*-

Task: 扫描前端网页需要的 static 静态内容的完整性, 如果文件不完整, 则重新从公网下载.
Compiler: gcc ./utils/scan.c -o ./utils/scan.exe
*/


# include <stdio.h>
# include <unistd.h>
# include <stdlib.h>
# include <string.h>
# include <windows.h>


char * GetCurrentWorkingDirectory(){
    // 函数: 获取程序当前工作路径.
    // 参数: 无.
    // 返回值: 获取到后返回字符数组，否则返回 NULL 空指针常量.
    char * cwd = (char*)malloc(1024);
    if (getcwd(cwd, 1024) != NULL){
        return cwd;
    }
    else{
        perror("getcwd() error...");
        return NULL;
    }
}

int CheckFileExists(const char * dir){
    // 函数: 检查文件是否存在.
    // 参数: 文件路径.
    // 返回值: 1 代表存在, 0 代表不存在.
    FILE * file = fopen(dir, "r");
    if (file == NULL){
        return 0;
    }
    fclose(file);
    return 1;
}

void RequestDownload(char * cwd){
    // 函数: 请求下载公网资源.
    // 参数: 资源文件保存路径, 默认为 cwd 当前工作路径.
    // 返回值: 无.
    const char * dir = "./bin/curl.exe";
    SetConsoleOutputCP(65001);
    if (CheckFileExists(dir)){
        printf("\n");
        printf("如果静态资源下载缓慢, 可稍后再重新单独运行 scan.exe 程序.");
        printf("\n");
        char commandIllusionna[1000];
        char paramIllusionna[] = "https://gitee.com/Senu/App/raw/master/static.zip";
        printf("\n");
        sprintf(commandIllusionna, "%s/bin/curl.exe -o %s/static.zip %s", cwd, cwd, paramIllusionna);
        system(commandIllusionna);
        sprintf(commandIllusionna, "%s/bin/unzip.exe %s/static.zip", cwd, cwd);
        system(commandIllusionna);
        char tmpIllusionna[] = "./static.zip";
        remove(tmpIllusionna);

        printf("\n");
        printf("如果静态资源下载缓慢, 可稍后再重新单独运行 scan.exe 程序.");
        char commandOsrrceoy[1000];
        char paramOsrrceoy[] = "https://gitee.com/osrrceoy/NEUmail/raw/master/static.zip";
        printf("\n");
        sprintf(commandOsrrceoy, "%s/bin/curl.exe -o %s/static.zip %s", cwd, cwd, paramOsrrceoy);
        system(commandOsrrceoy);
        sprintf(commandOsrrceoy, "%s/bin/unzip.exe %s/static.zip", cwd, cwd);
        system(commandOsrrceoy);
        char tmpOsrrceoy[] = "./static.zip";
        remove(tmpOsrrceoy);

        printf("\n\033[32mRestart program 重启程序\033[0m...\n");
        system("pause");
    }
    else{
        char * path = GetCurrentWorkingDirectory();
        char command[1000];
        printf("\n");
        sprintf(command, "%s\\bin\\*", path);
        printf("\033[31m缺少\033[0m './bin' 工具包, 下载网址:\n");
        printf("\033[33mhttps://gitee.com/Senu/Sharing/raw/master/bin.zip\033[0m\n");
        printf("解压到程序所在位置:\033[32m %s \033[0m", command);
        printf("\n\n");
        system("pause");
    }
}


int main(){
    system("");
    system("cls");
    char * cwd = GetCurrentWorkingDirectory();
    if (cwd != NULL){
        RequestDownload(cwd);
        free(cwd);
    }
    return 0;
}