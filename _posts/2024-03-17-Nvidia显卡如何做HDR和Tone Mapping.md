---
layout: post
title:  "Nvidia显卡如何做HDR和Tone Mapping"
date:   2024-03-17 17:49:30 -0500
categories: jekyll update
---
- [0.打开HDR](#0打开hdr)
- [1.Nvidia控制面板开启对应功能](#1nvidia控制面板开启对应功能)
- [2.PotPlayer设置](#2potplayer设置)
- [3.其他未设置](#3其他未设置)
***

超分辨是通过软硬件增加画面的分辨率和码率的一种手段。本文只介绍**Windows操作系统**基于**Nvidia显卡+potplayer播放器**的超分辨方式。

### 0.打开HDR
- Windows 设置-系统-屏幕-打开“使用HDR”
- 设置-应用-视频播放-打开“自动处理视频以增强其效果”
- Windows商店下载校色软件，手动校色，保存校色文件。

### 1.Nvidia控制面板开启对应功能
打开Nvidia控制面板，左侧选视频-调整视频图像设置--RTX视频增强-超分辨率，按需勾选质量。

### 2.PotPlayer设置
安装PotPlayer后，选项-视频，
- 视频渲改为“内置 Direct3D 11 视频渲染器”
- 尺寸调整选择“自动选择（推荐）”
- 勾选下方的“D3D11 GPU 超分辨率”
保存配置后重启，播放任意视频时，只要视频比起原本的尺寸有放大，就会自动超分辨率。

### 3.其他未设置
- [tone mapping](https://docs.google.com/document/d/1OIVKk8njrDTELsIZUrTBod_LdPB1sz9FieK6h1DfzF0/edit)